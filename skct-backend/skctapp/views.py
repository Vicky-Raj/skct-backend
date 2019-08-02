from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import get_object_or_404
import smtplib
import threading
from .models import *
from django.urls import reverse
import socket
def send_mail(to,subject,text):
    # Gmail Sign In
    gmail_sender = 'vickylab2000@gmail.com'
    gmail_passwd = 'passwordai'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    body = '\r\n'.join(['To: %s' % to,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % subject,
                        '',text])

    try:
        server.sendmail(gmail_sender, [to], body)
        print ('email sent')
    except:
        print ('error sending mail')

    server.quit()

class HomeView(APIView):
    def get(self, request, dept):
        dept = get_object_or_404(Department,name=dept)
        return Response({
            'name':dept.name.upper(),
            'having':dept.having,
            'bg_img':dept.bg_img.url,
            'about':dept.about,
            'vision':dept.vision,
            'mission':dept.mission,
            'faculty_count':dept.faculty.count(),
            'student':dept.student,
            'strength':dept.faculty.count() + dept.student,
            'gallery':[gal.image.url for gal in dept.gallery.all()],
            'aluminis':[
            {
                'img':alumini.img.url,
                'name':alumini.name,
                'thought':alumini.thought
            }for alumini in dept.aluminis.all()
            ],
            'labs':[
                {
                    'name':lab.name,
                    'img':lab.image.url,
                    'description':lab.description,
                }
                for lab in dept.labs.all()
            ],
            'class_strength':dept.class_strength,
               'events':[
                {
                    'pk':event.pk,
                    'name':event.name,
                    'image':event.image.url,
                    'date':event.date,
                    'description':event.description,
                    'contact':event.contact,
                    'email':event.email
                }
                for event in dept.events.all()
            ],
            'thought':dept.thought,
            'thought_author':dept.thought_name,
            'thought_photo':dept.thought_photo.url,
            'hod_name':dept.hod_name,
            'hod_num':dept.hod_num,
            'hod_email':dept.hod_email
        })

class FacultyView(APIView):
    def get(self, request, dept):
        dep = get_object_or_404(Department,name=dept)
        return Response({
            'faculty':[
                {
                    'img':fac.img,
                    'name':fac.name,
                    'pos':fac.pos,
                    'email':fac.email,
                    'pdf':f'http://{request.get_host()}{fac.pdf_file.url}/ '
                }
                for fac in dep.faculty.all() 
            ]
        })

class EventDetailView(APIView):
    def get(self,request,pk):
        event=Events.objects.get(pk=pk)
        return Response({
            'name':event.name,
            'image':event.image.url,
            'date':event.date,
            'description':event.description,
            'contact':event.contact,
            'email':event.email
        })

class FeedBackView(APIView):
    def post(self,request,dep):
        message = "Thank you for your feedback...\nStay tuned"
        thread = threading.Thread(target=send_mail,args=(request.POST.get('gmail'),"feedback",message))
        thread.start()
        return Response()

class MainView(APIView):
    def get(self,request):
        announcements=Announcement.objects.all()
        return Response({
            [
                {
                    'img':a.img.image.url,
                    'description':a.description
                }
            for a in announcements]
        })

class UpcomingEventsView(APIView):
     def get(self,request):
         event=UpcomingEvents.objects.all()
         return Response({
             [
                 {
                'img':event.img.image.url,
                'date':event.date,
                'name':event.name
            
                 }
              for event in event]
         })

