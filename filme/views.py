from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaForm, AcessarForm
from django.http import HttpResponseRedirect


class Homepage(FormView):
    template_name = "homepage.html"
    form_class = AcessarForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("filme:homefilmes")
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)

        if usuarios:
            return reverse("filme:login")
        return reverse("filme:criarconta")


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filmes = Filme.objects.all()

        context["filme_destaque"] = filmes.first()
        context["lista_filmes_recentes"] = filmes.order_by("-data_criacao")
        context["lista_filmes_emalta"] = filmes.order_by("-visualizacoes")

        return context


class DetalhesView(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()

        usuario = request.user
        usuario.filmes_vistos.add(filme)

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filmes_relacionados"] = Filme.objects.filter(
            categoria=self.get_object().categoria
        )[:5]
        return context


class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):
        termo = self.request.GET.get("query")

        if termo:
            return Filme.objects.filter(titulo__icontains=termo)

        return Filme.objects.none()


class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ["first_name", "last_name", "email"]

    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.kwargs["pk"]:
            return redirect(
                reverse(
                    "filme:editarperfil",
                    kwargs={"pk": request.user.id},
                )
            )

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("filme:homefilmes")


class CriarConta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("filme:login")