from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from datetime import date
import datetime
import json
from .forms import AgeForm
from .utils.computeAge import computeAge

# Create your views here.
def home_view(request):
    return render(request, "home.html", {})

def checkAge_view(request):
    form = AgeForm(request.POST or None)
    if form.is_valid():
        # form.save()
        pass

    context = { "form" : form }
    return render(request, "age_form.html", context)

@api_view(["POST"])
def checkAge(request): 

    date1 = json.loads(request.body)

    try:
        day = date1.get("day", 0)
        month = date1.get("month", 0)
        year = date1.get("year", 0)
        bday = datetime.date(year, month, day)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    
    today = datetime.date.today()

    # return JsonResponse("{  message: Birthday: "+str(bday)+" and Today: "+str(today)+"  }", safe=False)
    computeAge(bday, today)