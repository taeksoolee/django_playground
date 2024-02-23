from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list, name='list'),
    path('detail/<int:board_id>', views.detail, name='detail'),
]