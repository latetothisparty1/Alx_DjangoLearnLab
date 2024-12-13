# Create your views here.

from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def get_object(self):
        # Ensure the notification belongs to the authenticated user
        notification = super().get_object()
        if notification.recipient != self.request.user:
            raise PermissionDenied("You do not have permission to access this notification.")
        return notification

    def patch(self, request, *args, **kwargs):
        notification = self.get_object()
        notification.read = True  # Assuming you have a 'read' field in your Notification model
        notification.save()
        return Response({"message": "Notification marked as read."}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        notification = self.get_object()
        notification.delete()
        return Response({"message": "Notification deleted."}, status=status.HTTP_204_NO_CONTENT)