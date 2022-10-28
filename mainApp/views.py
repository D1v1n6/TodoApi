from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

#CRUD Operations

class ListTodo(generics.ListAPIView):                #Read
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailTodo(generics.RetrieveUpdateAPIView):     #Update
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateTodo(generics.CreateAPIView):              #Create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteTodo(generics.DestroyAPIView):              #Delete
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer