from django.shortcuts import render


def index(request):
    context={
        'title':'lesson5',
    }
    return render(request, 'lesson5/index.html',context)
