from django.urls import path
from . import views # Current directory

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]