from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date, datetime
import json

# Create your views here.
def home(request):
    return HttpResponse('Hello World!')

@api_view(["POST"])
def computeAge(dd, mm, yyyy): 

    day = json.loads(dd.body)
    month = json.loads(mm.body)
    year = json.loads(yyyy.body)

    try:
        bday = datetime.date(year, month, day)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    today = date.today()

    return JsonResponse("Birthday: "+bday+"\nToday: "+today, safe=False)
    # return JsonResponse("Today: "+today.strftime('%d-%m-%Y'), safe=False)