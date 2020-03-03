from django.urls import path
from . import views

urlpatterns = [
  path('api/notecards/', views.NotecardsListCreate.as_view() ),
]