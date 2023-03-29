from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from shortner.models import URLCollection
from .serializers import *


def unwrap_urlcollection_data(obj):
    return {
        'id': obj.id,
        'short_url': obj.short_url,
        'url_name': obj.url_name,
        'redirect_url': obj.redirect_url,
        'redirect_count': obj.redirect_count
    }


class URLCollectionListCreateView(APIView):
    def get(self, request):
        collections = list(URLCollection.objects.all().values())
        return Response(data=collections)
    
    def post(self, request):
        data = request.data
        serializer = URLCollectionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()

        return Response(data=unwrap_urlcollection_data(obj))


class URLCollectionUpdateDeleteView(APIView):
    def put(self, request, id):
        obj = get_object_or_404(URLCollection, pk=id)
        data = request.data
        serializer = URLCollectionSerializer(instance=obj, data=data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response(data=unwrap_urlcollection_data(obj))
    
    def delete(self, request, id):
        obj = get_object_or_404(URLCollection, pk=id)
        obj.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    