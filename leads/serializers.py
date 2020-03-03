from rest_framework import serializers
from .models import Lead, Friend

class LeadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lead
    fields = ('id', 'name', 'email', 'message')

class FriendSerializer(serializers.ModelSerializer):
  class Meta:
    model = Friend
    fields = ('name', 'birthday')