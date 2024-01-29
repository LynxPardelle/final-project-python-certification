from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm, AccountForm
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def author():
    return HttpResponse("<p>This is app was made by <strong>Lynx Pardelle</strong>, you can watch my work on <a href='https://lynxpardelle.com' target='_blank' >lynxpardelle.com</a><p>")


def login_request(request):
    errStatus = 500
    try:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    print(user)
                    account = Account.objects.get(user=user)
                    if not account:
                        raise Exception("No existe la cuenta")
                    print(account)
                    messages = []
                    messages.append("Inicio de sesión correcto")
                    return render(request, "home.html", {'messages': messages})
                else:
                    return render(request, "login.html", {"form": form, "error": "No existe el usuario"})
            else:
                return render(request, "login.html", {"form": form})
        else:
            form = AuthenticationForm()
            return render(request, "login.html", {"form": form})
    except Exception as e:
        print('An exception occurred')
        print(e)
        return render(request, 'error.html', {
            'status': errStatus,
            'statusMessage': 'Error',
            'data': {
                'method': request.method,
                'path': request.path,
                'body': request.body.decode('utf-8'),
                'headers': dict(request.headers),
            },
            'message': "Error: %s" % e})


def register(request):
    errStatus = 500
    try:
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                print(form.cleaned_data.get('password1'))
                print(form.cleaned_data.get('password2'))
                if form.cleaned_data.get('password1') != form.cleaned_data.get('password2'):
                    raise Exception("Las contraseñas no coinciden")
                user = form.save()
                login(request, user)
                account = Account(user=user)
                account.save()
                if not account:
                    raise Exception("No existe la cuenta")
                messages = []
                messages.append("Usuario creado correctamente")
                return render(request, "home.html", {'messages': messages})
            else:
                messages = []
                for msg in form.error_messages:
                    print(form.error_messages[msg])
                    messages.append(form.error_messages[msg])
                return render(request, "signup.html", {"form": form, 'messages': messages})
        else:
            form = UserForm()
            return render(request, "signup.html", {"form": form})
    except Exception as e:
        print('An exception occurred')
        return render(request, 'error.html', {
            'status': errStatus,
            'statusMessage': 'Error',
            'data': {
                'method': request.method,
                'path': request.path,
                'body': request.body.decode('utf-8'),
                'headers': dict(request.headers),
            },
            'message': "Error: %s" % e})


@login_required(login_url='/login')
def logout_request(request):
    logout(request)
    messages = []
    messages.append("Usuario ha cerrado sesión correctamente")
    return render(request, "home.html", {'messages': messages})


@login_required(login_url='/login')
def updateUser(request, id=None, type=None):
    print(id)
    print(request.method)
    if request.method == "POST":
        form = UserForm(request.POST)
        accountForm = AccountForm(request.POST, request.FILES)
        if form.is_valid() and (type == None or type != 'account'):
            print('type', type)
            if form.cleaned_data.get('password1') != form.cleaned_data.get('password2'):
                raise Exception("Las contraseñas no coinciden")
            if not id:
                raise Exception("No existe el usuario")
            user = User.objects.get(id=id)
            print('user', user)
            print('password', user.password)
            if not user:
                raise Exception("No existe el usuario")
            account = Account.objects.get(user=user)
            if not account:
                raise Exception("No existe la cuenta")
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            # TODO: Make something to change password only when they really need it
            # user.password = form.cleaned_data.get('password1')
            user.save()
            account.description = accountForm.cleaned_data.get(
                'descripción') or account.description
            account.web_page = accountForm.cleaned_data.get(
                'web_page') or account.web_page
            account.avatar = accountForm.cleaned_data.get(
                'avatar') or account.avatar
            account.save()
            return render(request, "home.html")
        elif accountForm.is_valid() and type != None and type == 'account':
            print('type', type)
            print(form.cleaned_data)
            print(form.cleaned_data.get('password1'))
            print(form.cleaned_data.get('password2'))
            print(form.errors)
            print(form.error_messages)
            if not id:
                raise Exception("No existe el usuario")
            user = User.objects.get(id=id)
            if not user:
                raise Exception("No existe el usuario")
            account = Account.objects.get(user=user)
            if not account:
                raise Exception("No existe la cuenta")
            account.description = accountForm.cleaned_data.get('description')
            account.web_page = accountForm.cleaned_data.get('web_page')
            account.avatar = accountForm.cleaned_data.get('avatar')
            account.save()
            return render(request, "home.html")
        else:
            print('type', type)
            messages = []
            print(form.cleaned_data)
            print(form.cleaned_data.get('password1'))
            print(form.cleaned_data.get('password2'))
            print(form.errors)
            print(accountForm.changed_data)
            print(accountForm.errors)
            for msg in form.error_messages:
                print(form.error_messages[msg])
                messages.append(form.error_messages[msg])
            """ for msg in accountForm.error_messages:
                print(accountForm.error_messages[msg])
                messages.append(accountForm.error_messages[msg]) """
            return render(request, "update_profile.html", {"form": form, "account_form": accountForm, 'messages': messages, 'id': id})
    else:
        if not id:
            raise Exception("No existe el usuario")
        user = User.objects.get(id=id)
        if not user:
            raise Exception("No existe el usuario")
        account = Account.objects.get(user=user)
        if not account:
            raise Exception("No existe la cuenta")
        form = UserForm(initial={
            'username': user.username,
            'email': user.email,
        })
        accountForm = AccountForm(initial={
            'description': account.description,
            'web_page': account.web_page,
            'avatar': account.avatar,
        })
        return render(request, "update_profile.html", {"form": form, "account_form": accountForm, 'id': id})


def getUser(request, id):
    errStatus = 500
    try:
        if request.method == "GET":
            if not id:
                raise Exception("No existe el usuario")
            user = User.objects.get(id=id)
            if not user:
                raise Exception("No existe el usuario")
            account = Account.objects.get(user=user)
            if not account:
                raise Exception("No existe la cuenta")
            profile = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'description': account.description,
                'web_page': account.web_page,
                'avatar': account.avatar,
            }
            return render(request, "profile.html", {"profile": profile})
        else:
            raise Exception("No existe el usuario")
    except Exception as e:
        print('An exception occurred')
        return render(request, 'error.html', {
            'status': errStatus,
            'statusMessage': 'Error',
            'data': {
                'method': request.method,
                'path': request.path,
                'body': request.body.decode('utf-8'),
                'headers': dict(request.headers),
            },
            'message': "Error: %s" % e})
