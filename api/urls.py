from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes/', views.getNotes, name="notes"),
    path('notes/<str:pk>', views.getNote, name="note"),
    path('notes/<str:pk>/update/', views.updateNote, name="update-note"),
    path('notes/<str:pk>/delete/', views.deleteNote, name="delete-note"),
    path('notes/add/', views.addNote, name="add-note"),
    path('users/', views.getUsers, name="users"),
    path('users/<str:pk>', views.getUser, name="user"),
    path('users/<str:pk>/update/', views.updateUser, name="update-user"),
    path('users/<str:pk>/delete/', views.deleteUser, name="delete-user"),
    path('users/add/', views.addUser, name="add-note"),
]