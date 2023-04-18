from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('сreate_a', views.create_a, name='create_a'),
    path('сreate_pb', views.create_pb, name='create_pb'),
    path('сreate_b', views.create_b, name='create_b'),
    path('update/<int:id>/', views.view_edit, name="update"),
    path('view_a', views.view_a, name="view_a"),
    path('view_b', views.view_b, name="view_b"),
    path('view_ph', views.view_ph, name="view_ph"),

]
