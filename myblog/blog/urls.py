from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_create, name='post_create'),
    path('apply/', views.apply, name='apply'),
    # path('', views.post_list, name='post_list'),

]
