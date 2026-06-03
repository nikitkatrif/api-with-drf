from rest_framework import viewsets
from .models import Platform, Genre, Game
from .serializers import PlatformSerializer, GenreSerializer, GameSerializer

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        platform_id = self.request.query_params.get('platform_id')
        title = self.request.query_params.get('title')
        if platform_id:
            qs = qs.filter(platform_id=platform_id)
        if title:
            qs = qs.filter(title__icontains=title)
        return qs