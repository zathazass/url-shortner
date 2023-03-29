from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/shortner/', include('shortner.api.urls')),
    path('', include('shortner.urls')),
]
