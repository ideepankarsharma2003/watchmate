from rest_framework import serializers
from ..models import WatchList, StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        exclude = ['created_at', 'updated_at', ]



class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist= WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        # fields = '__all__'
        exclude = ['created_at' ]