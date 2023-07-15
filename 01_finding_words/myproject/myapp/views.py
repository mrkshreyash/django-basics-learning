from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

# def counter(request):
#     words = request.POST['words']
#     amount_of_words = len(words.split())
#     context = {
#         'words':words,
#         'amount':amount_of_words
#     }
#     return render(request, 'counter.html', context=context)


def find_words(request):
    words = request.POST['words']
    to_find = request.POST['to_find']


    for i in words.split():
        if i == to_find:
            token = 'Present'
            break
        else:
            token = 'Not Present'

    context = {
        'words' : words,
        'to_find': to_find,
        'is_found': token
    }

    return render(request, 'find_words.html', context=context)
