from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    print(request, args, kwargs)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html")


def contact_view(request, *args, **kwargs):
    print(request.__dict__)
    return render(request, "contact.html")


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 15,
        "fruits": ["banana", "maçã", "uva"],
        "numbers": range(1, 11),
    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    return render(request, "social.html")
