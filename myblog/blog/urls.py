from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_create, name='post_create'),
    # path('create/', views.post_create, name='post_create'),
    # path('', views.post_list, name='post_list'),

]
