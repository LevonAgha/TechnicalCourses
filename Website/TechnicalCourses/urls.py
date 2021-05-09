from django.urls import path
from . import views

urlpatterns = [
    path('', views.Courses, name='home_page'),
]
