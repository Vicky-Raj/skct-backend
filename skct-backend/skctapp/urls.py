from django.urls import path
from . import views

urlpatterns = [
    path("<str:name>/home/",views.HomeView.as_view()),
    path("<str:name>/academics/",views.AcademicsView.as_view()),
    path("<str:name>/best/",views.BestPraticesView.as_view()),
    path("<str:name>/faculty/",views.FacultyView.as_view()),
    path("<str:name>/lab/",views.LabView.as_view()),
    path("<str:name>/research/",views.ResearchView.as_view()),
    path("<str:name>/placement/",views.PlacementView.as_view()),
    path("<str:name>/events/",views.EventsView.as_view()),
    path("<str:name>/club/",views.ClubView.as_view()),
    path("<str:name>/gallery/",views.GalleryView.as_view()),
    path("<str:name>/hod/",views.HodView.as_view())
    # path("coe/",views.HomeView.as_view()),
    # path("management/",views.HomeView.as_view()),
    # path("feedback/",views.HomeView.as_view()),
]
