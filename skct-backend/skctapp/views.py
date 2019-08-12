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
    def get(self,request,name):
        dept =get_object_or_404(Department,name=name)
        return Response({
        'name':dept.name,
        'certificate':dept.certificate,
        'image':dept.dep_image.url,
        'video':dept.video,
        'about':dept.about,
        'vision':dept.vision,
        'mission':dept.mission,
        'hod':{
            'name':dept.hod.name,
            'email':dept.hod.email,
            'image':dept.hod.image.url,
            'phone_num':dept.hod.phone_num,
            'thought':dept.hod.thought,
        },
        'events':[{
            'pk':event.pk,
            'name':event.name,
            'img':event.image.url,
            'date':event.date,
            'description':event.description,
            'contact':event.contact,
            'email':event.email

        }


        for event in  dept.events.all()],


        })


class AcademicsView(APIView):
    def get(self,request,name):
        dept= get_object_or_404(Department,name=name)
        return Response([{
        'name':academics.name,
        'details':academics.details
        }for academics in dept.academics.all()
        ])

class BestPraticesView(APIView):
    def get(self,request,name):
        dept =get_object_or_404(Department,name=name)
        return Response([
            {
                'name':bp.name,
                'details':bp.details
            }
        for bp in dept.bp.all()])
    

class FacultyView(APIView):
    def get(self,request,name):
        dept=get_object_or_404(Department,name=name)
        return Response(

        [
            {   
                'name':faculty.name,
                'image':faculty.img.url,
                'pos':faculty.pos,
                 'email': faculty.email,
                 'file':faculty.pdf_file.url,

            }
        for faculty in dept.facultys.all()
        ]
    )


class LabView(APIView):
    def get(self,request,name):
        dept= get_object_or_404(Department,name=name)
        return Response(
            [
            
            {    'name':lab.name,
                'description':lab.description,
                'image':lab.image.url

            }

            for lab in dept.labs.all()]
            )
        
class ResearchView(APIView):
    def get(self,request,name):
        dept=get_object_or_404(Department,name=name)
        return Response([
            file.file_name.url
        ]for file in dept.researches.all())

class PlacementView(APIView):
    def get(self,request,name):
        dept= get_object_or_404(Department,name=name)
        return Response(
            [
                {
                    'year':placement.year,
                    'companies':
                        [
                            {
                                'name':company.name,
                                'logo':company.logo.url,
                                'students':
                                    [
                                        {
                                            'name':student.name,
                                            'image':student.photo.url

                                        }
                                for student in company.students.all()
                                ]
                            }

                        for company in placement.companys.all()]
                    

                }
            for placement in dept.placement.all()
            
        ])


class EventsView(APIView):
    def get(self,request,name):
        dept =get_object_or_404(Department,name=name)
        return Response({
            [
                {
                    'name':event.name,
                    'image':event.image.url,
                    'date':event.date,
                    'description':event.description,
                    'contact':event.contact,
                    'email':event.email,

                }
             for event in dept.events.all()]
        })

class ClubView(APIView):
    def get(self,request,name):
        dept=get_object_or_404(Department,name=name)

        return Response([
        {
            'name':club.club_name,
            'details':club.club_details,
            'photo':club.club_photo.url

        }for club in dept.club.all()
        ])

class GalleryView(APIView):
    def get(self,request,name):
        dept = get_object_or_404(Department,name=name)

        return Response({
            'photos':[img.image.url for img in dept.gallery.all()]
        })


class HodView(APIView):
    def get(self,request,name):
        dept = get_object_or_404(Department,name=name)

        return Response({
            'name':dept.hod.name,
            'email':dept.hod.email,
            'image':dept.hod.image.url,
            'phone_num':dept.hod.phone_num,
            'thought':dept.hod.thought
        })

class CoeView(APIView):
    pass
        

class ManagementView(APIView):
    pass