from django.urls import path
from . import views

urlpatterns = [
    path("<str:dept>/home/",views.HomeView.as_view()),
    path("<str:dept>/faculty/",views.FacultyView.as_view(),name='faculty') ,
        path("<str:dep>/feedback/",views.FeedBackView.as_view()),
    path('event/<int:pk>/',views.EventDetailView.as_view()),
    path('main/',views.MainView.as_view()),
    path('events/',views.UpcomingEventsView.as_view())
]
