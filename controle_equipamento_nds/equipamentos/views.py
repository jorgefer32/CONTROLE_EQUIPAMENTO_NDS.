from django.shortcuts import render
from django.views.generic import ListView
from .models import EquipamentoNDS
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import EmprestimoForm
from django.views.generic import DetailView
from .models import Emprestimo


class EquipamentoListView(ListView):
    model = EquipamentoNDS
    template_name = 'equipamentos/equipamento_list.html'
    context_object_name = 'equipamentos'


def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

class UsuarioCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'usuario_form.html'
    success_url = reverse_lazy('equipamentos:usuario_form')

class EmprestimoCreateView(CreateView):
    form_class = EmprestimoForm
    template_name = 'emprestimo_form.html'
    success_url = reverse_lazy('equipamentos:emprestimo_form')

class EmprestimoDetailView(DetailView):
    model = Emprestimo
    template_name = 'emprestimo_detail.html'
    context_object_name = 'emprestimo'
