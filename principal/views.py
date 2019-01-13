from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Diario, Noticia, Autor
from django.db.models import Count
from .forms import DiarioForm, UsuarioForm, NoticiaForm, AutorForm, SearchForm


def paises(request):
    diarios = Diario.objects.all()
    paises = []
    for d in diarios:
        if not d.pais in paises:
            paises.append(d.pais)
    diccio = {}
    for p in paises:
        diccio[p] = Diario.objects.all().filter(pais=p)
    return render(request, 'paises.html', {'paises': diccio})


def interes(request):
    noticias = Noticia.objects.annotate(interesados=Count('usuarios')).order_by('-interesados')
    return render(request, 'interes.html', {'noticias': noticias})


def index(request):
    return render(request, 'index.html')


def nuevodiario(request):
    if request.method == 'POST':
        formulario = DiarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = DiarioForm()
    return render(request, 'formulario.html', {'titulo': 'Nuevo diario', 'formulario': formulario})


def nuevousuario(request):
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UsuarioForm()
    return render(request, 'formulario.html', {'titulo': 'Nuevo usuario', 'formulario': formulario})


def nuevanoticia(request):
    if request.method == 'POST':
        formulario = NoticiaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = NoticiaForm()
    return render(request, 'formulario.html', {'titulo': 'Nueva noticia', 'formulario': formulario})


def nuevoautor(request):
    if request.method == 'POST':
        formulario = AutorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = AutorForm()
    return render(request, 'formulario.html', {'titulo': 'Nuevo autor', 'formulario': formulario})


def buscar(request):
    if request.method == 'POST':
        formulario = SearchForm(request.POST)
        if formulario.is_valid():
            autor = get_object_or_404(Autor, nombre=formulario.cleaned_data["clave"])
            noticias = autor.noticia_set.all()
            return render(request, 'autor.html', {'noticias': noticias})
    else:
        formulario = SearchForm()
    return render(request, 'formulario.html', {'titulo': 'Buscar por autor', 'formulario': formulario})
