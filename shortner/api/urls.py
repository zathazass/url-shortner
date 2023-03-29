from django.urls import path
from . import views

urlpatterns = [
    path('', views.URLCollectionListCreateView.as_view()),
    path('<int:id>', views.URLCollectionUpdateDeleteView.as_view())
]