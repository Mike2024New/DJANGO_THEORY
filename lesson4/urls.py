from django.urls import path
from lesson4 import views

app_name = 'lesson4'

urlpatterns = [
    path('lsn4/', view=views.index, name='index')
]
