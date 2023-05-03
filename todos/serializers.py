from rest_framework import serializers

from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "user", "done", "task", "created_at", )
        model = ToDo