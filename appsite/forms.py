from decimal import Decimal
from django import forms
from django.core.validators import RegexValidator
from projeto import settings
from .models import Projeto, Language

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ('projeto_id', 'autor', 'linguagem', 'nomeProjeto')


    projeto_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    autor = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '120'}),
    )

    linguagem = forms.ModelMultipleChoiceField(queryset=Language.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'list-unstyled', 'maxlength': '120'})
    )    

    nomeProjeto = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '120'}),
    )

class RemoveProdutoForm(forms.Form):
    class Meta:
        fields = ('projeto_id')

    projeto_id = forms.CharField(widget=forms.HiddenInput(), required=True)