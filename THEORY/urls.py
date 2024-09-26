"""
URL configuration for THEORY project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from main import views # импорт функции отвечающей за обработку 404 страницы
handler404 = views.handle_page_not_found # привязка обработчика для 404 страницы
handler505 = views.handle_error_server # привязка обработчика для 500 ошибка на стороне сревера

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls',namespace='main')),
    path('',include('lesson1.urls',namespace='lesson1')),
    path('',include('lesson2.urls',namespace='lesson2')),
    path('',include('lesson3.urls',namespace='lesson3')),
    path('',include('lesson4.urls',namespace='lesson4')),
    path('',include('lesson5.urls',namespace='lesson5')),
]
