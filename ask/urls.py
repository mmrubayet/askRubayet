from django.urls import path

from . import views


urlpatterns = [
    # path('', views.home, name='ask-home'),
    path('', views.ques_list, name='ques_list'),
    path('about/', views.about, name='ask-about'),
    path('question/<int:pk>/', views.ques_detail, name = 'ques_detail'),


]
