from django.urls import path

from .views import CreateEventView, event_list_view

urlpatterns = [
    path('', event_list_view),
    path('create/', CreateEventView.as_view(), name='create-event'),
    ]