from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'user_name': "I would return the name of the logged-in user."}
    return render(request, 'freetime/index.html', context_dict)


def about(request):
    return HttpResponse('This will be the about page for UnFree Time')