
from rest_framework import serializers
from task_project.models import ToDo_list

class TaskSerializer(serializers.Serializer):

    class Meta:
        model = ToDo_list
        fields = '__all__'

