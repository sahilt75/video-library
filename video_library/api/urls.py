from api.views import VideoListSet, VideoSearchListView
from rest_framework import routers

# Endpoints for video API
video_router = routers.DefaultRouter()
video_router.register(r'list', VideoListSet, basename="list")
video_router.register(r'search', VideoSearchListView, basename="search")

