from django.urls import path
from . import views

app_name = 'APP_FINAL'

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/remover/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('carrinho/modal/', views.ver_carrinho_modal, name='ver_carrinho_modal'),
]
