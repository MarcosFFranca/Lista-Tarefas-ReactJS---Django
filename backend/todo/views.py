from django.shortcuts import render


#A classe viewset fornece a implementação padrão para operações CRUD. Tudo o que precisamos fazer foi especificar a classe serializer e o conjunto de consultas.

from rest_framework import viewsets         
from .serializers import TodoSerializer     
from .models import Todo                   


class TodoView(viewsets.ModelViewSet):       
    serializer_class = TodoSerializer          
    queryset = Todo.objects.all()      
