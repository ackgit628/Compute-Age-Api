from django.urls import path
from myWebApp.views import home_view, checkAge_view

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('check-age/', checkAge_view)
]
