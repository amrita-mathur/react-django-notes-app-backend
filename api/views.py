from django.shortcuts import render, get_object_or_404
from rest_framework import response, serializers
from rest_framework.decorators import api_view
from .models import Note, NoteUser
from .serializers import NoteSerializer, UserSerializer
from rest_framework import status



# Create your views here.

def getRoutes(request):
    return response.Response('Our API', safe=False)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return response.Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return response.Response(serializer.data)


@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)
    if serializer.is_valid():
        serializer.save()
    return response.Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    Note.objects.get(id=pk).delete()
    
    return response.Response("The note was deleted")

@api_view(['POST'])
def addNote(request):
    data = request.data
    noteuser = NoteUser(id=data["userId"])
    note = Note.objects.create(body = data['body'], userId = noteuser)
    serializer = NoteSerializer(note, many=False)
    return response.Response(serializer.data)


@api_view(['GET'])
def getUsers(request):
    users = NoteUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return response.Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
    user = NoteUser.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return response.Response(serializer.data)

@api_view(['PUT'])
def updateUser(request, pk):
    data = request.data
    user = NoteUser.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=data)
    if serializer.is_valid():
        serializer.save()
    return response.Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
    NoteUser.objects.get(id=pk).delete()
    
    return response.Response("The note was deleted")


@api_view(['POST'])
def addUser(request):
    
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return response.Response(serializer.data)

