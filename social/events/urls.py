from django.contrib import admin
from django.urls import path, include
from . import views
from .views import EventListView, UserEventsListView

urlpatterns=[
    path('events', EventListView.as_view(), name='events'),
    path('event/new/', views.create_event, name='event-create'),
    path('event/delete/<int:event_id>', views.event_delete, name='event-delete'),
    path('event/<int:event_id>/', views.event_details, name='event-detail'),
    path('search_events/', views.search_events, name='search_events'),
    path('event/<int:pk>/members/', views.members_list, name='event-members'),
    path('event/members/delete/<int:user_id>/<int:event_id>/', views.delete_member, name='delete-members'),
    path('event/members/add/<int:user_id>/<int:event_id>/', views.add_member, name='add-members'),
    path('user_events/<str:username>', UserEventsListView.as_view(), name='user-events'),
]
