from rest_framework.serializers import ModelSerializer

from shortner.models import URLCollection


class URLCollectionSerializer(ModelSerializer):
        class Meta:
            model = URLCollection
            fields = ['url_name', 'redirect_url']