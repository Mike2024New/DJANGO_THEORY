from django.shortcuts import render,redirect

"""
В этом примере показывается обработка post запроса, то есть прием данных из формы (которая определена в index см. form1)
В функции index если был выполнен post запрос (то есть нажата кнопка "отправить" на форме в html), выполняется отлов данных из полей, 
эти данные записываются в сессию request.session['data'].

То есть в данном примере общение между index и show_result выполняется с помощью объекта session (ключа data)

---------------------------------------------------------------------------------------
Для того, чтобы сессия работала, нужно сделать первичную миграцию:
python manage.py makemigrations
python manage.py migrate
"""

def show_result(request):
    """Вывод данных из сессии на страницу с результатом"""
    data = request.session.get('data', None)  # Получаем данные из сессии безопасно
    print(f"==>{data}")
    context = {
        'title': 'Просмотр данных переданных в POST запрос',
        'data': data
    }
    return render(request, 'lesson3/result.html', context)

def index(request):
    # Инициализация ключа сессии, если его еще нет
    if 'data' not in request.session:
        request.session['data'] = {'name': None, 'family': None}

    # Отлавливаем POST запрос
    if request.method == 'POST':
        if 'field_name' in request.POST and 'field_family' in request.POST:
            # Записываем значения из POST запроса в сессию
            request.session['data']['name'] = request.POST['field_name']
            request.session['data']['family'] = request.POST['field_family']
            request.session.modified = True # важно после изменения данных в сессии применять modified = True иначе сессия не перезаписывается
            print("Сохраненные данные в сессии:", request.session['data'])  # Отладочное сообщение
            return redirect('lesson3:show_result')

    # Если запрос не был POST, загружается страница index.html
    context = {
        'title': 'POST запросы, передача данных',
    }

    return render(request, 'lesson3/index.html', context)