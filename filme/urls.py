# url - view - template
from tempfile import template

from django.urls import path, include, reverse_lazy
from setuptools.extern import names

from .views import Homepage, Homefilmes, DetalhesView, PesquisaFilme, EditarPerfil, CriarConta
from django.contrib.auth import views as auth_view

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', DetalhesView.as_view(), name='detalhesfilme'),
    path('pesquisa/', PesquisaFilme.as_view(), name='pesquisafilme'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', EditarPerfil.as_view(), name='editarperfil'),
    path('criarconta/', CriarConta.as_view(), name='criarconta'),
    path('mudarsenha', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy('filme:homefilmes')), name='mudarsenha'),
]
