from django.urls import path
from events import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('create/', views.event_create, name='event_create'),
    path('delete/<int:pk>/', views.event_delete, name='event_delete'),
]
