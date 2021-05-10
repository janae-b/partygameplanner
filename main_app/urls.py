from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('games/', views.games_index, name='index'),
  path('games/<int:game_id>/', views.games_detail, name='detail'),
  path('games/create/', views.GameCreate.as_view(), name='games_create'),
  path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
  path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
  path('games/<int:game_id>/add_planning/', views.add_planning, name='add_planning'),
  path('games/<int:game_id>/add_photo/', views.add_photo, name='add_photo'),
  path('games/<int:game_id>/assoc_event/<int:event_id>/', views.assoc_event, name='assoc_event'),
  path('events/<int:pk>/', views.EventDetail.as_view(), name='events_detail'),
  path('events/create/', views.EventCreate.as_view(), name='events_create'),
  path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
  path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),
  path('events/', views.EventList.as_view(), name='events_index'),
]