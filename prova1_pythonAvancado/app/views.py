from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.hashers import make_password

from django.shortcuts import get_object_or_404

from .models import *
from .forms import *

# Create your views here.
def home(request):
    imagens = Imagem.objects.all()
    contexto = {"imagens":imagens}
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(user_ptr_id = request.user.id)
        imagens_galeria = list(usuario.galeria.all())
        contexto["imagem_galeria"] = imagens_galeria
    return render(request,"home.html",contexto)


def add_imagem(request):
    form = FormImagem()
    contexto = {"form_imagem":form}
    return render(request,"add_imagem.html",contexto)


def form_imagem(request):
    form = FormImagem(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("add_imagem"))
    return HttpResponseRedirect(reverse("home"))



def perfil(request):
    if  request.user.is_authenticated:
        form = FormUsuario(instance=request.user)
    else:
        form = FormUsuario()

    contexto = {"form_usuario": form}
    return render(request,"perfil.html",contexto)





def login (request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user:
            auth_login(request,user)
    return HttpResponseRedirect(reverse('home'))

def logout (request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))



def editar_perfil(request):
    if request.method == "POST":
        usuario = Usuario.objects.get(user_ptr_id = request.user.id)
        novo_usuario = request.POST.copy()
        novo_usuario["password"] = usuario.password
        form = FormUsuario(instance=usuario,data=novo_usuario)
        if form.is_valid:
            form.save()

        return HttpResponseRedirect(reverse('perfil'))
    return HttpResponseRedirect(reverse('home'))


def cadastro(request):
    if request.method=="POST":
        form_usuario = FormUsuario(request.POST)
        if form_usuario.is_valid():
            if request.POST.get("password")!=request.POST.get("confirmacao"):
                form_usuario.add_error("password","As senhas devem ser iguais")
            else:
                form_usuario = form_usuario.save(commit=False)
                form_usuario.password = make_password(form_usuario.password)
                form_usuario.save()
                return HttpResponseRedirect(reverse("home"))

    form_usuario = FormUsuario()
    contexto = {"form_usuario":form_usuario}
    return render(request,"cadastro.html",contexto)


def add_galeria(request, id):
    if request.user.is_authenticated and not request.user.is_superuser:
        imagem = Imagem.objects.get(id=id)
        usuario = Usuario.objects.get(user_ptr_id=request.user.id)

        imglist = list(usuario.galeria.all())
        imglist.append(imagem)

        usuario.galeria.set(imglist)
        usuario.save()

    return HttpResponseRedirect(reverse('home'))

def remover_galeria(request, id):
    if request.user.is_authenticated and not request.user.is_superuser:
        imagem = Imagem.objects.get(id=id)
        usuario = Usuario.objects.get(user_ptr_id=request.user.id)

        imglist = list(usuario.galeria.all())
        imglist.remove(imagem)

        usuario.galeria.set(imglist)
        usuario.save()

    return HttpResponseRedirect(reverse('galeria'))



def galeria(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        usuario = Usuario.objects.get(user_ptr_id=request.user.id)
        imagens = list(usuario.galeria.all()) 
        contexto = {"imagens": imagens} 
        return render(request, "galeria.html", contexto)
    return HttpResponseRedirect(reverse('perfil'))


