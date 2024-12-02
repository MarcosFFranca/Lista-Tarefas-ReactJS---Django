'''Aqui especificamos o modelo com o qual queremos trabalhar e os campos que desejamos converter para JSON.'''

from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')