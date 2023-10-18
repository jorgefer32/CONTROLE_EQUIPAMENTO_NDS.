from django import forms
from .models import Emprestimo

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['equipamento', 'usuario', 'data_devolucao']
