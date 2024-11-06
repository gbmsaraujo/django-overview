import datetime
import re
from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "price"]


# class RawProductForm(forms.Form):
#     title = forms.CharField(
#         label="Nome do produto",
#         error_messages={"required": "Insira o nome de um produto"},
#     )
#     description = forms.CharField()
#     price = forms.DecimalField()


def validar_cpf(cpf):
    # Remove caracteres especiais
    cpf = re.sub(r"[^0-9]", "", cpf)

    if len(cpf) != 11 or not cpf.isdigit():
        raise forms.ValidationError("CPF inválido. Deve ter 11 dígitos numéricos.")

class CadastroForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label="Nome Completo",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Seu nome"}
        ),
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Seu e-mail"}
        ),
    )
    cpf = forms.CharField(
        max_length=14,
        label="CPF",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "XXX.XXX.XXX-XX"}
        ),
        validators=[validar_cpf],
    )
    data_nascimento = forms.DateField(
        label="Data de Nascimento",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),

    )

    # Validação adicional para a data de nascimento
    def clean_data_nascimento(self):
        data = self.cleaned_data["data_nascimento"]
        hoje = datetime.date.today()

        if data > hoje:
            raise forms.ValidationError("A data de nascimento não pode ser no futuro.")

        if hoje.year - data.year > 120:
            raise forms.ValidationError(
                "A idade deve ser razoável (menos de 120 anos)."
            )

        return data

    # Validação adicional para o nome
    def clean_nome(self):
        nome = self.cleaned_data["nome"]
        if  nome == 'xereca':
            raise forms.ValidationError("O nome não pode conter xereca.")
        return nome


