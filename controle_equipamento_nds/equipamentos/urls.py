from django.urls import path
from . import views

app_name = 'equipamentos'

urlpatterns = [
    path('cadastro/usuario/', views.UsuarioCreateView.as_view(), name='usuario_form'),
    path('cadastro/emprestimo/', views.EmprestimoCreateView.as_view(), name='emprestimo_form'),
    path('emprestimo/<int:pk>/', views.EmprestimoDetailView.as_view(), name='emprestimo_detail'),
    path('', views.pagina_inicial, name='pagina_inicial'),
]
