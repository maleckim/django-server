from django.shortcuts import render
from .models import Notecards
from .serializers import NotecardsSerializer
from rest_framework import generics


class NotecardsListCreate(generics.ListCreateAPIView):
  queryset = Notecards.objects.all()
  serializer_class = NotecardsSerializer
