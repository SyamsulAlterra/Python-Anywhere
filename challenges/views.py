from django.shortcuts import render, get_object_or_404
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def blog(request):
    daftar_article=Article.objects.all()
    return render(request, 'blog.html', {'daftar_article':daftar_article})

def mentee(request):
    daftar_mentee=Mentee.objects.all()
    return render(request, 'mentee.html', {'daftar_mentee':daftar_mentee})

def mentor(request):
    daftar_mentor=Mentor.objects.all()
    return render(request, 'mentor.html', {'daftar_mentor':daftar_mentor} )

def author(request):
    return render(request, 'author.html')

def input_mentor(request):
    if request.method == 'POST':
        form=data_mentor(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = data_mentor()

    return render(request, 'form_mentor.html', {'form':form} )

def input_mentee(request):
    if request.method == 'POST':
        form=data_mentee(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=data_mentee()

    return render(request, 'form_mentee.html', {'form':form} )

def input_article(request):
    if request.method == 'POST':
        form=data_article(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=data_article()

    return render(request, 'form_article.html', {'form':form} )

def detail_blog(request, pk_id):
    article=get_object_or_404(request, pk=pk_id)
    return render(request, 'detail_blog.html', {'article':article})

