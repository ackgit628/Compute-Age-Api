from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('check-age/', views.checkAge_view),
    path('computeAge/', views.computeAge)
]
