from django.contrib import admin
from django.urls import path, include
from proba.views import *

app_name = 'prob'
urlpatterns = [
    path('prob/create/', ProbCreateView.as_view()),
    path('all/', ProbaListView.as_view()),
    path('prob/detail/<int:pk>/', ProbDetailView.as_view()),

]