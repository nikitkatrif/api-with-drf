from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlatformViewSet, GenreViewSet, GameViewSet

router = DefaultRouter()
router.register(r'platforms', PlatformViewSet, basename='platform')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'games', GameViewSet, basename='game')

urlpatterns = [
    path('', include(router.urls)),
]