from . import views
from .views import post_detailed
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name= "about"),
    path("the-writer/", views.writer_preview, name = 'the_writer'),
    path("the-writer/<slug:slug>", views.post_detailed, name = "post_detailed" )
]
