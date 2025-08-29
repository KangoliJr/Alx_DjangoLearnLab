from rest_framework import serializers
from posts.models import Post
from .models import Notification
from django.contrib.contenttypes.models import ContentType


class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    target_title = serializers.SerializerMethodField()
    
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'target_title', 'read', 'timestamp']

    def get_target_title(self, obj):
        if isinstance(obj.target, Post):
            return obj.target.title
        return 'N/A'