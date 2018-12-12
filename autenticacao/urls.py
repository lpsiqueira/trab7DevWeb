from django.urls import path
from . import views

app_name = 'autenticacao'

urlpatterns = [
    path('signin/', views.signin, name='signin')
]