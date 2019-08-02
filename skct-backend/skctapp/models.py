from django.db import models
from django.contrib.auth.models import User

class Faculty(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    pos = models.CharField(max_length=30,null=True)
    email=models.EmailField()
    pdf_file = models.FileField(null=True,default=None)
    def __str__(self):
        return f"{self.name}"

class Images(models.Model):
    image=models.ImageField(upload_to="image")

class Lab(models.Model):
    name = models.CharField(max_length=50,null=True)
    description=models.TextField()
    image=models.ImageField(upload_to='image')

class Alumini(models.Model):
    img = models.ImageField(upload_to="image")
    name = models.CharField(max_length=50)
    thought = models.CharField(max_length=500)


class Events(models.Model):
    name=models.CharField(max_length=20)
    image = models.ImageField(upload_to="image",blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    contact=models.CharField(max_length=10)
    email=models.EmailField()

class Department(models.Model):
    name=models.CharField(max_length=200)
    having = models.BooleanField(null=True)
    about = models.TextField()
    vision=models.TextField()
    mission=models.TextField()
    faculty=models.ManyToManyField(Faculty)
    student=models.IntegerField()
    bg_img=models.ImageField(upload_to='image')
    gallery=models.ManyToManyField(Images,related_name="gallery_set")
    aluminis = models.ManyToManyField(Alumini)
    labs = models.ManyToManyField(Lab)
    hod_name=models.CharField(max_length=150,blank=True,null=True)
    hod_num = models.CharField(max_length=10,blank=True,null=True)
    hod_email=models.EmailField(blank=True,null=True)
    events = models.ManyToManyField(Events)
    class_strength = models.IntegerField(null=True)
    thought = models.TextField(null=True)
    thought_name = models.CharField(max_length=20,null=True)
    thought_photo = models.ImageField(upload_to="image",null=True)
    def __str__(self):
       return f"{self.name}" 

class Announcement(models.Model):
    img =models.ImageField()
    description=models.TextField()  
    def __str__(self):
        return self.description     

class UpcomingEvents(models.Model):
    img=models.ImageField()
    date=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name
    