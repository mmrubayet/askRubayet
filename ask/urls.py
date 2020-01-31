from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='ask-home'),
    path('about/', views.about, name='ask-about'),


]
