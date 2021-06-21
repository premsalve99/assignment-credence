from django.contrib import admin
from django.urls import path, include
from myapp import views
from .views import MovieList, MovieDetail

urlpatterns = [
    path("", views.MovieList.as_view()),
    path("<int:pk>",views.MovieDetail.as_view()),
    
]
