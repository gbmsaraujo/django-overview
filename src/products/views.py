from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm, CadastroForm


def product_create_view(request):
    my_form = CadastroForm()
    context = {"form": my_form}
    if request.method == 'POST':
        my_form = CadastroForm(request.POST)
        if my_form.is_valid():
            # aqui é executada todas as funções com prefixo clean
            # dentro da classe CadastroForm
            # Se o formulário for válido, acesse os dados limpos
            nome = my_form.cleaned_data["nome"]
            email = my_form.cleaned_data["email"]
            cpf = my_form.cleaned_data["cpf"]
            data_nascimento = my_form.cleaned_data["data_nascimento"]

            # Aqui você pode salvar os dados no banco de dados ou realizar outras ações
            # Exemplo: MeuModelo.objects.create(nome=nome, email=email, ...)

            # Renderize uma página de sucesso
        else:
            context = {"form": my_form}
            return render(request, "product/product_create.html", context)
            # form = CadastroForm(request.POST)
    return render(request, "product/product_create.html", context)


def product_detail_view(request, id:int):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    
    
    context = {
        "title": product.title,
        "description": product.description,
    }

    return render(request, "product/detail.html", context)
