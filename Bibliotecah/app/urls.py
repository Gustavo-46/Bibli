from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *
urlpatterns = [
path('admin/', admin.site.urls),
path('', IndexView.as_view(), name='index'),
path('editar/<int:id>/', EditarLivroView.as_view(),
name='editar'),
path('editar/<int:pk>/', EditarLivroView.as_view(), name='editar'),


]

