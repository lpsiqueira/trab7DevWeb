from django import forms

class AdicionaItem(forms.Form):
    projeto_id = forms.CharField(
        widget=forms.HiddenInput(),
        required=True
    )