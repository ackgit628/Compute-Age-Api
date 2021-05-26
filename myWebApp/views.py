from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date
import datetime
import json

# Create your views here.
def home(request):
    return HttpResponse('Hello World!')

@api_view(["POST"])
def computeAge(request): 

    date1 = json.loads(request.body)

    try:
        day = date1.get("day", 0)
        month = date1.get("month", 0)
        year = date1.get("year", 0)
        bday = datetime.date(year, month, day)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    
    today = date.today()

    # return JsonResponse("{  message: Birthday: "+str(bday)+" and Today: "+str(today)+"  }", safe=False)

    if bday.year > today.year:
        return JsonResponse("greetings time traveller", safe=False)
    if (bday.month < today.month) or (bday.month == today.month and bday.day < today.day):
        age = today.year - bday.year
        return JsonResponse("Your age is "+str(age)+"yrs", safe=False)
    if (bday.month > today.month) or (bday.month == today.month and bday.day > today.day):
        age = today.year - bday.year - 1
        return JsonResponse("Your age is "+str(age)+"yrs", safe=False)