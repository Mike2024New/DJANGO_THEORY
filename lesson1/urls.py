from django.urls import path,re_path, register_converter
from lesson1 import views
from lesson1 import converters

app_name = "lesson1"
register_converter(converters.FourDigitYearConverter, "year4") # в импортируемом конвертере прописано регулярное выражение, используем year4 Ниже в маршруте categories_by_year
register_converter(converters.PhoneExtractConverter, "phone")

urlpatterns = [
    # важно порядок расположения маршрутов внизу имеет важное значение, например int, re_path и slug это частные случаи строки поэтому их нужно расположить перед строкой
    path('lsn1/',view=views.index, name='index'), # главная страница этого приложения
    path('lsn1/<year4:year>/', view=views.categories_by_year, name='categories_by_year'), # конвертер более кастомный чем регулярка внизу и рекомендуется делать именно так
    path('lsn1/<phone:phone>/', view=views.categories_by_phone, name='categories_by_phone'), # конвертер более кастомный чем регулярка внизу и рекомендуется делать именно так
    path('lsn1/<int:cat_id>/', view=views.categories_by_id, name='categories_by_id'), # конвертер по типу int (принимает числа в Url)
    # path('lsn1/<uuid:cat_uuid>/', view=views.categories_by_uuid, name='categories_by_uuid'), # * ввод в url символов формата xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx
    re_path(r'^lsn1/test-(?P<number>[0-9]{4})/', view=views.categories_by_regex, name='categories_by_regex'), # принимает регулярное выражение
    path('lsn1/<slug:cat_slug>/',view=views.categories_by_slug, name='categories_by_slug'), # принимает буквы лат алфавита, цифры и символ -
    path('lsn1/<str:cat_str>/', view=views.categories_by_str, name = 'categories_by_str'), # принимает строку (то есть все символы которые не прошли выше кроме /)
    path('lsn1/<path:cat_path>/', view=views.categories_by_path, name='categories_by_path'), # ввод пути в url главное наличие символа / 
]

"""
uuid не смотря на все попытки не работает корректно и перехватывается slug, поэтому пока вопрос по нему остаётся открытым
вероятно, для него стоит все таки использовать регулярные выражения, или кастомные конверторы
* важно uuid, должен иметь определенную структуру:
xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx
например:
fads34d2d-b8b5-4d7e-a2d4-4c0e7e2b3f64

то есть 5 груп символов из латинских символов и цифр, разделенные четыремя дефисами
"""