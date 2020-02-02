from django.urls import path

from . import views


urlpatterns = [
    # path('', views.home, name='ask-home'),
    path('', views.ques_list, name='ques_list'),
    path('about/', views.about, name='ask-about'),
    path('question/<int:pk>/', views.ques_detail, name = 'ques_detail'),
    path('question/new/', views.ques_new, name = 'ques_new'),
    path('question/<int:pk>/edit/', views.ques_edit, name = 'ques_edit'),
    path('drafts/', views.ques_draft_list, name='ques_draft_list'),
    path('question/<pk>/publish/', views.ques_publish, name='ques_publish'),
    path('question/<pk>/remove/', views.ques_remove, name='ques_remove'),


]
