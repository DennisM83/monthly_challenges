from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat for the entire month")

# def february(request):
#     return HttpResponse("Walk for at least 20 minutes everyday")

def monthly_challenge(request, month):
    if month == 'january':
        challenge_text = "No meat for the enitre month"
    elif month == 'february':
        challenge_text = "Walk for at least 20 minutes a day"
    elif month == 'march':
        challenge_text = "No meat for the enitre month"
    else:
        return HttpResponseNotFound("Month not supported")
    return HttpResponse(challenge_text)