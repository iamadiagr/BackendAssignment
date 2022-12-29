from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from rest_framework import generics

# Create your views here.

@api_view(['GET'])
def get_api(request):
    go_to = [
        '',
        '/videos',
    ]
    return Response(go_to)


class VideoListView(generics.ListAPIView):
    search_fields = ['title', 'description']
    # filter_backends = (filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter)
    # filterset_fields = ['id','title']
    ordering = ('-published')
    queryset = Video.objects.all()
    serializer_class = VideoSerializer