from django.urls import path
from . import views

urlpatterns = [
    path('match/<int:match_id>/', views.scoreboard, name='scoreboard'),
    path('api/match/create/', views.create_match, name='create_match'),
    path('api/match/<int:match_id>/', views.match_detail, name='match_detail'),
    path('api/match/<int:match_id>/point/', views.add_point, name='add_point'),
]