from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *
from django.urls import path, include


urlpatterns = [
path('admin/', admin.site.urls),
path('', IndexView.as_view(), name='index'),
path('livros/', LivrosView.as_view(), name='livros'),
path('reserva/', EmprestimoView.as_view(),
name='reserva'),
path('delete/<int:id>/', DeleteLivroView.as_view(),
name='delete'),
path('cidade/', CidadesView.as_view(),
name='cidade'),
path('autor/', AutoresView.as_view(), name='autor'),
path('editor/', EditorasView.as_view(),
name='editora'),
path('leitor/', LeitoresView.as_view(),
name='leitor'),
path('genero/', GenerosView.as_view(),
name='genero'),

path('editar/<int:pk>/', EditarLivroView.as_view(), name='editar'),

]
