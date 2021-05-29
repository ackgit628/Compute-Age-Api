from django.shortcuts import render

def check_age(request):
    return render(request, "index.html")