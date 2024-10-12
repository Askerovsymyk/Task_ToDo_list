from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import  api_view
from task_project.models import ToDo_list
from task_project.taskserializer import TaskSerializer
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def task_list(request):
    tasks = ToDo_list.objects.all()
    serializer = TaskSerializer(tasks, many=True).data
    return Response(serializer)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def task_detail(request, pk):
    try:
        task = ToDo_list.objects.get(pk=pk)
    except TaskSerializer.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def task_update(request, pk):
    try:
        task = ToDo_list.objects.get(pk=pk)
    except TaskSerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def task_delete(request, pk):
    try:
        task = ToDo_list.objects.get(pk=pk)
    except ToDo_list.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)