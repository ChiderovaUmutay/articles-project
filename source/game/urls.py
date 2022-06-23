from django.urls import path

from game.views import index_views, get_stat

urlpatterns = [
    path('', index_views),
    path('stat/', get_stat),
]