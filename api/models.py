from django.db import models

# Create your models here.
class NoteUser(models.Model):
    username = models.TextField(unique=True)    
    name = models.TextField()
    password = models.TextField()
    email = models.EmailField()


    def __str__(self):
        return self.username
    

class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    userId = models.ForeignKey(NoteUser, on_delete=models.CASCADE, default=1, db_column="noteuser_id")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[0:50]
    



