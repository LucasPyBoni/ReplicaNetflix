from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaForm, AcessarForm
from django.http import HttpResponseRedirect
# Create your views here.

# def homepage(request):
#    return render(request, "homepage.html")
class Homepage(FormView):
    template_name = "homepage.html"
    form_class = AcessarForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("filme:homefilmes")
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')

# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, 'homefilmes.html', context)
class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme
    #object_list

class DetalhesView(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    #object

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetalhesView, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context

class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None

class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.id != self.kwargs['pk']:  # Verifica se o usuário está tentando editar outro perfil
                return self.redirect_to_own_profile()
        else:
            return HttpResponseRedirect(reverse('filme:login'))  # Se não estiver autenticado, redireciona para login
        return super().dispatch(request, *args, **kwargs)

    def redirect_to_own_profile(self):
        own_profile_url = reverse('filme:editarperfil', kwargs={'pk': self.request.user.id})
        return redirect(own_profile_url)  # Usa 'redirect' para redirecionar de forma mais simples

    def get_success_url(self):
        return reverse('filme:homefilmes')  # Redireciona após sucesso na edição do perfil

class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')