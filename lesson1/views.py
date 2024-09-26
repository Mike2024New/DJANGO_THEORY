from django.shortcuts import render

def index(request):
    context={
        'title':'Home Page'
    }
    return render(request, 'lesson1/index.html',context)


def show_result_html(request,title):
    """отправка страницы с результатом"""
    context = {
        'title':title,
    }
    return render(request, 'lesson1/result.html', context)


def categories_by_id(request,cat_id):
    title=f'в url введена категория id: {cat_id}, тип конвертера int'
    return show_result_html(request, title)

def categories_by_uuid(request, cat_uuid):
    title = f'в url введена категория uuid: {cat_uuid}, тип конвертера uuid (уникальный идентификатор)'
    return show_result_html(request, title)


def categories_by_slug(request, cat_slug):
    title=f'в url введена категория slug: {cat_slug}, тип конвертера slug'
    return show_result_html(request, title)


def categories_by_str(request, cat_str):
    title=f'в url введена строка (str): {cat_str}, тип конвертера str'
    return show_result_html(request, title)


def categories_by_path(request, cat_path):
    title=f'в url введен путь: {cat_path}, тип конвертера path'
    return show_result_html(request, title)


def categories_by_regex(request, number):
    title=f'в url введено регулярное выражение: {number}, тип конвертера regex'
    return show_result_html(request, title)


def categories_by_year(request, year):
    title=f'в url введено регулярное выражение year4: {year}, тип конвертера regex -> класс year4 (свой класс конвертер)'
    return show_result_html(request, title)


def categories_by_phone(request, phone):
    title=f'в url введено регулярное выражение phone: {phone}, тип конвертера regex -> класс phone (свой класс конвертер)'
    return show_result_html(request, title)
