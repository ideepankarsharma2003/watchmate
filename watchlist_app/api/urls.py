from django.urls import path, include

from .views import WatchListAPI, WatchListDetail, StreamPlatformAPI, StreamPlatformDetail # Class Based Views

urlpatterns = [

    # Class Based Views
    path('list/', WatchListAPI.as_view(), name='movie-list'),
    path('detail/<int:pk>/', WatchListDetail.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAPI.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetail.as_view(), name='stream-detail'),
]
