from django.shortcuts import render
from descriptions import descriptions_list


def index(request):
    context = {
        'title' : 'Содержание:',
        'descriptions' : descriptions_list,
    }
    

    return render(request,'main/index.html',context)

def handle_page_not_found(request, exception):
    """обработчик страницы 404"""
    print(f"ошибка запрашиваемой страницы не существует, {exception}")
    return render (request, '404.html', status=404)

def handle_error_server(request, exception):
    """обработка страницы 500 ошибка сервера"""
    print(f"ошибка на стороне сервера, {exception}")
    return render (request, '500.html', status=500)