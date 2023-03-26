from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges = {
    "january": "No meat for the enitre month",
    "february": "Walk for at least 20 minutes a day",
    "march" : "Learn Django for at least 20 minutes every day!",
    "april": "No meat for the enitre month",
    "may": "Walk for at least 20 minutes a day",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "No meat for the enitre month",
    "august": "Walk for at least 20 minutes a day",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "No meat for the enitre month",
    "november": "Walk for at least 20 minutes a day",
    "december": "Learn Django for at least 20 minutes every day!"
}

# def january(request):
#     return HttpResponse("Eat no meat for the entire month")

# def february(request):
#     return HttpResponse("Walk for at least 20 minutes everyday")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
         return HttpResponseNotFound("Month not supported")