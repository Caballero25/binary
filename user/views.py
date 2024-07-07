from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from archivos.models import ArchivosCatalogo
# Create your views here.

def userLogin(request):
    context = {}
    if request.method == "GET":
        return render(request, "login.html", context)
    elif request.method == "POST":
        userUsername = request.POST.get('username')
        userPassword = request.POST.get('password')
        userAuth = authenticate(request, username=userUsername, password=userPassword)
        if userAuth:
            login(request,userAuth)
            return redirect('menu-principal')
        else:
            context['error'] = "Credenciales Incorrectas, por favor, solicite soporte."
            return render(request, "login.html", context)
        
@login_required
def menu(request):
    num_archivos = len(ArchivosCatalogo.objects.filter(publico=True))
    context = {'archivosDisponibles': num_archivos}
    return render(request, "main.html", context)


def logout_view(request):
    logout(request)
    return redirect('userLogin')