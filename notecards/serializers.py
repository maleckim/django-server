from rest_framework import serializers
from .models import Notecards

class NotecardsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Notecards
    fields = ('title', 'content')