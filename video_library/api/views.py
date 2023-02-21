from rest_framework import viewsets, filters, generics
from .models import Video
from .serializers import VideoSerializer
from rest_framework import permissions


class VideoListSet(viewsets.ModelViewSet):
    """
    API endpoint that returns list of videos
    """
    queryset = Video.objects.all().order_by('-published_at')
    serializer_class = VideoSerializer
    # permission_classes = [permissions.IsAuthenticated]

class VideoSearchListView(generics.ListAPIView, viewsets.GenericViewSet):
    """
    API endpoint that returns list of videos based on search
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
