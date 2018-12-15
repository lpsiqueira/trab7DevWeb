from django import forms

class AdicionaItem(forms.Form):
    projeto_id = forms.CharField(
        widget=forms.HiddenInput(),
        required=True
    )

class RemoveItem(forms.Form):
    item_id = forms.CharField(
        widget=forms.HiddenInput(),
        required=True
    )

    remover = forms.BooleanField(
        initial=False,
        widget=forms.HiddenInput()
    )

    quantidade = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'w-25'})
    )    