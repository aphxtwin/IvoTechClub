from . import views
from .views import post_detailed
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name= "about"),
    path('inventions/', views.inventions, name = 'inventions'),
    path("articles/", views.writer_preview, name = 'the_writer'),
    path("articles/<slug:slug>", views.post_detailed, name = "post_detailed" )
]
