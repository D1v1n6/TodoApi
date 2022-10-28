from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('list', ListTodo.as_view(), name='List'),
    path('create', CreateTodo.as_view(), name='create'),
    path('delete/<int:pk', DeleteTodo.as_view()),
    path('', views.home, name='home')
]