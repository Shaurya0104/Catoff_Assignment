from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pro",views.pro_players,name="pro"),
    path("get_stats",views.players,name="get_stats"),
    # path('verify-stats/', views.verify_stats, name='verify_stats'),
]