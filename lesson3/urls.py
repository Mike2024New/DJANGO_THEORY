from django.urls import path
from lesson3 import views

app_name = "lesson3"

urlpatterns = [
    path('lsn3/',view=views.index, name='index'),
    path('lsn3/show_result/',view=views.show_result, name='show_result'),
]
