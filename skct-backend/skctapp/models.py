from django.db import models
from django.contrib.auth.models import User

class Faculty(models.Model):
    img = models.ImageField(upload_to="image")
    name = models.CharField(max_length=100)
    pos = models.CharField(max_length=30,null=True)
    email=models.EmailField()
    pdf_file = models.FileField(null=True,default=None)
    def __str__(self):
        return f"{self.name}"

class Student(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="image")

class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="image")
    students = models.ManyToManyField(Student)

class Placement(models.Model):
    year = models.CharField(max_length=20)
    companys = models.ManyToManyField(Company)
    

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

class Club(models.Model):
    club_name = models.CharField(max_length=50)
    club_details = models.TextField()
    club_photo = models.ImageField(upload_to="image")

class Academics(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()

class BestPratices(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()

class Pdf(models.Model):
    file_name = models.FileField(upload_to="files")

class Events(models.Model):
    name=models.CharField(max_length=20)
    image = models.ImageField(upload_to="image",blank=True,null=True)
    date=models.DateTimeField(blank=True)
    description=models.TextField()
    contact=models.CharField(max_length=10)
    email=models.EmailField()

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

class Hod(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to="image",null=True)
    phone_num = models.CharField(max_length=10)
    thought = models.TextField(null=True)

class Department(models.Model):
    name = models.CharField(max_length=50,null=True)
    certificate = models.CharField(max_length=100,null=True)
    dep_image = models.ImageField(upload_to="image",null=True)
    video = models.URLField(null=True)
    about = models.TextField(null=True)
    vision = models.TextField(null=True)
    mission = models.TextField(null=True)
    hod = models.OneToOneField(Hod,on_delete=models.CASCADE)
    academics = models.ManyToManyField(Academics)
    bp = models.ManyToManyField(BestPratices)
    facultys = models.ManyToManyField(Faculty)
    labs = models.ManyToManyField(Lab)
    researches = models.ManyToManyField(Pdf)
    placement = models.ManyToManyField(Placement)
    events = models.ManyToManyField(Events)
    club = models.ManyToManyField(Club)
    gallery = models.ManyToManyField(Images)
    def __str__(self):
        return f"{self.name}"
