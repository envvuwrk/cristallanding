from . import views
from django.urls import path

app_name = 'c4capp'

urlpatterns = [
    path('', views.index, name='index'),


]
