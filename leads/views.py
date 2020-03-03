from django.shortcuts import render
from .models import Lead, Friend
from .serializers import LeadSerializer, FriendSerializer
from rest_framework import generics

# Create your views here.

class LeadListCreate(generics.ListCreateAPIView):
  queryset = Lead.objects.all()
  serializer_class = LeadSerializer

class FriendListCreate(generics.ListCreateAPIView):
  queryset = Friend.objects.all()
  serializer_class = FriendSerializer
