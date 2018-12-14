from django.urls import path
from . import views

app_name = 'carrinho'

urlpatterns = [
    path('', views.carrinho, name='carrinho'),
    path('atualizacao/quantidade/', views.carrinho, name='atualizacao')
]