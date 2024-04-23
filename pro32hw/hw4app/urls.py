from django.urls import path
from hw4app.views import *

urlpatterns=[
    path('Samsung/',samsung),
    path('OnePlus/',oneplus),
    path('iphone/',iphone),
    path('Oppo/',oppo),
    path('IQOO/',iqoo),
    
]