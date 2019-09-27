from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/', views.read),
    path('<int:article_pk>/update/', views.update),
    path('<int:article_pk>/read_update/', views.read_update),
    path('<int:article_pk>/detail/', views.detail),
    path('<int:article_pk>/delete/', views.delete),
    path('jiyoung/', views.jiyoung),
    path('choice/', views.choice),
]