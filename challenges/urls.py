from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    # path('home.html/', views.home),
    # path('blog.html/',views.blog,name='blog'),
    path('blog/<int:pk>/',views.detail_blog, name='detail_blog'),
    # path('blog.html/form_article.html',views.input_article),
    # path('mentee.html/',views.mentee,name='mentee'),
    # path('form_mentee.html',views.input_mentee),
    # path('mentor.html/',views.mentor,name='mentor'),
    # path('form_mentor/',views.input_mentor),
    # path('author.html/',views.author,name='author'),
    path('blog/',views.blog,name='blog'),
    path('mentee/',views.mentee,name='mentee'),
    path('mentor/',views.mentor,name='mentor'),
    path('author/',views.author,name='author'),
    path('input_mentor/', views.input_mentor, name='input_mentor'),
    path('input_mentee/', views.input_mentee, name='input_mentee'),
    path('input_article/',views.input_article, name='input_article'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)