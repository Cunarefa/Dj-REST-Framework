from .views import *
from django.urls import include, path

urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('all/', CarListView.as_view()),
    path('car/detail/<int:pk>/', CarDetailView.as_view()),
]