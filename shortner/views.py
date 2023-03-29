from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest

from .models import URLCollection


def home(request):
    return render(request, 'shortner/home.html', {})


def url_redirect(request, url):
    try:
        obj = URLCollection.objects.get(short_url=url)
    except URLCollection.DoesNotExist:
        return HttpResponseBadRequest('Short URL Not match')
    
    obj.redirect_count += 1
    obj.save()

    return HttpResponseRedirect(obj.redirect_url)