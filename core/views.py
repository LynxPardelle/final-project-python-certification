from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def author():
    return HttpResponse("<p>This is app was made by <strong>Lynx Pardelle</strong>, you can watch my work on <a href='https://lynxpardelle.com' target='_blank' >lynxpardelle.com</a><p>")


def home(request):
    return render(request, "home.html", {'title': "Home"})


def about(request):
    return render(request, "about.html", {'title': "About"})
