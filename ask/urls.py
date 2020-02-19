from django.urls import path

from . import views


urlpatterns = [
    # path('', views.home, name='ask-home'),
    # path('', views.question_list, name='question_list'),
    path('', views.QuestionListView.as_view(), name='question_list'),
    path('about/', views.about, name='ask-about'),
    path('question/<int:pk>/', views.question_detail, name = 'question_detail'),
    path('question/new/', views.question_new, name = 'question_new'),
    path('question/<int:pk>/edit/', views.question_edit, name = 'question_edit'),
    path('drafts/', views.question_draft_list, name='question_draft_list'),
    # path('drafts/', views.QuestionDraftListView.as_view(), name='question_draft_list'),
    path('question/<pk>/publish/', views.question_publish, name='question_publish'),
    path('question/<pk>/remove/', views.QuestionDeleteView.as_view(), name='question_remove'),
    path('question/<int:pk>/answer/', views.add_answer_to_que, name='add_answer_to_que'),
    path('question/<int:pk>/answer/approve/', views.answer_approve, name='answer_approve'),
    # path('question/<int:pk>/answer/remove/', views.answer_remove, name='answer_remove'),
    path('question/<int:pk>/answer/remove/', views.AnswerDeleteView.as_view(), name='answer_remove'),
    path('question/<int:pk>/answer/hide/', views.answer_hide, name='answer_hide'),
    path('user/<str:username>', views.UserQuestionListView.as_view(), name='user_question_list'),




]
