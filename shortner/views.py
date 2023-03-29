from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'shortner/home.html', {})


def url_redirect(request, url):
    return HttpResponseRedirect('https://zathazass.github.io/portfolio/')