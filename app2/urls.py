from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('kohli/',kohli,name='kohli'),
    path('surya/',surya,name='surya'),
]
