from django.contrib import admin

# Register your models here.
from .models import Note, NoteUser
admin.site.register(Note)
admin.site.register(NoteUser)

