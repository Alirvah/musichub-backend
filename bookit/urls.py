from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'room', api.RoomViewSet)
router.register(r'event', api.EventViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Room
    path('bookit/room/', views.RoomListView.as_view(), name='bookit_room_list'),
    path('bookit/room/create/', views.RoomCreateView.as_view(), name='bookit_room_create'),
    path('bookit/room/detail/<int:pk>/', views.RoomDetailView.as_view(), name='bookit_room_detail'),
    path('bookit/room/update/<int:pk>/', views.RoomUpdateView.as_view(), name='bookit_room_update'),
)

urlpatterns += (
    # urls for Event
    path('bookit/event/', views.EventListView.as_view(), name='bookit_event_list'),
    path('bookit/event/create/', views.EventCreateView.as_view(), name='bookit_event_create'),
    path('bookit/event/detail/<int:pk>/', views.EventDetailView.as_view(), name='bookit_event_detail'),
    path('bookit/event/update/<int:pk>/', views.EventUpdateView.as_view(), name='bookit_event_update'),
)

