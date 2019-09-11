from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('delete/',views.delete, name='delete')
]   