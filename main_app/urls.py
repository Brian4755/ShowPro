from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('shows/', views.shows_index, name='shows_index'),
  path('shows/<int:show_id>/', views.shows_detail, name='shows_detail'),
  path('shows/create', views.ShowCreate.as_view(), name='show_create'),
  path('shows/<int:pk>/update/', views.ShowUpdate.as_view(), name='shows_update'),
  path('shows/<int:pk>/delete/', views.ShowDelete.as_view(), name='shows_delete'),
]