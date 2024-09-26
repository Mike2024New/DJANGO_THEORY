from django.urls import path
from lesson5 import views

app_name = 'lesson5'

urlpatterns = [
    path('lsn5/',view=views.index, name='index')
]
