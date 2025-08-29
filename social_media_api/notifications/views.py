from django.shortcuts import render
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Retrieve notifications for the current user, ordered by timestamp
        return Notification.objects.filter(recipient=user).order_by('-timestamp')