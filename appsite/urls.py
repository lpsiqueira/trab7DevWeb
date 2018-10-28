from django.urls import path
from . import views

app_name = 'appsite'

urlpatterns = [
    path('', views.teste, name='teste'),
    path('index/', views.index, name='index'),
    path('signin/', views.signIn, name='signin'),
    path('signup/', views.signUp, name='signup'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('exibe/', views.exibe, name='exibe'),
    path('edita/', views.edita, name='edita'),
    path('remove/', views.remove, name='remove'),
]