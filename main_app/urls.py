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
  path('games/<int:game_id>/add_party/', views.add_party, name='add_party'),
  path('games/<int:game_id>/add_photo/', views.add_photo, name='add_photo'),
  path('games/<int:game_id>/assoc_plan/<int:plan_id>/', views.assoc_plan, name='assoc_plan'),
  path('plans/<int:pk>/', views.PlanDetail.as_view(), name='plans_detail'),
  path('plans/create/', views.PlanCreate.as_view(), name='plans_create'),
  path('plans/<int:pk>/update/', views.PlanUpdate.as_view(), name='plans_update'),
  path('plans/<int:pk>/delete/', views.PlanDelete.as_view(), name='plans_delete'),
  path('plans/', views.PlanList.as_view(), name='plans_index'),
  path('accounts/signup/', views.signup, name='signup'),
]