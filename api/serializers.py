from rest_framework.serializers import ModelSerializer
from .models import Note, NoteUser

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = NoteUser  
        fields = '__all__'      


