from django.shortcuts import render
from django.template.defaultfilters import slugify # импорт тега шаблона

# Create your views here.

def index(request):
    context = { # после значения указ использ фильтр в html
        'title':'Стандартные django фильтры теги в шаблонах', # capfirst
        'number_1':100, # add
        'number_2':500, # divisibleby
        'number_3':400, # divisibleby
        'num_3_div':3, # divisibleby (делитель для фильтра)
        'test_word_1':'test', # upper
        'test_word_2':'TEST', # lower
        'test_word_3':'TEST_@123@_TEST', # cut
        'test_word_4':'', # default
        'test_word_5':'value from view.py', # default
        'test_word_6':'table for kitchen', # slugify
        'test_word_7': slugify('test for value'),
        'test_collect_1':[100,200,400], # first/last/join
        
    }
    return render(request,'lesson4/index.html',context)