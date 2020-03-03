from django.urls import path
from . import views

urlpatterns = [
  path('api/lead/', views.LeadListCreate.as_view() ),
  path('api/friend/', views.FriendListCreate.as_view())
]