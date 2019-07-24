from django.db import models
from django.utils import timezone

class Mentor(models.Model):
    nama=models.CharField(max_length=25)
    prof_pic=models.ImageField(upload_to='static/img/mentor_image')
    sebutan=models.CharField(max_length=50)
    pengalaman=models.IntegerField()
    quote=models.TextField()

    def __str__(self):
        return self.nama

class Mentee(models.Model):
    nama=models.CharField(max_length=25)
    prof_pic=models.ImageField(upload_to='static/img/mentee_image')
    kesan=models.TextField()

    def __str__(self):
        return self.nama

class Article(models.Model):
    title=models.CharField(max_length=200)
    headline_pic=models.ImageField('Headline Picture', upload_to='static/img/headline_image')
    today=timezone.now()
    created_date=models.DateField(default=today)
    comment=models.IntegerField(default=0)
    content=models.TextField()

    def __str__(self):
        return self.title

