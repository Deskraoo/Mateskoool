from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect 

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {"posts":posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def inicio(request):
    return render(request, 'blog/inicio.html')

def agrupacion_numerica(request):
    return render(request, 'blog/Agrupacion-Numerica.html')

def clasificacion_numerica(request):
    return render(request, 'blog/Clasificacion-Numerica.html')

def clasificacion_seriacion(request):
    return render(request, 'blog/Clasificacion-Seriacion.html')

def figuras_geometricas(request):
    return render(request, 'blog/Figuras-Geometricas.html')

def contacto(request):
    return render(request, 'blog/contacto.html')

def multiplicacion_division(request):
    return render(request, 'blog/Multiplicacion-Division.html')

def numeros(request):
    return render(request, 'blog/Numeros.html')

def par_impar(request):
    return render(request, 'blog/Par-Impar.html')

def suma_resta(request):
    return render(request, 'blog/Suma-Resta.html')

