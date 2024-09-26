from django.urls import path
from lesson2 import views

app_name = "lesson2"

urlpatterns = [
    path('lsn2/',view=views.index, name = 'index'),
    path('lsn2/show_result/<str:data>/',view=views.show_result, name = 'show_result'),
]
