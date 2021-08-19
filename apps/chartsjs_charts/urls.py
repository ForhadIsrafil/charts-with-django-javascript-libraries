from django.urls import path
from .views import *

name = 'charts_js'
urlpatterns = [
    path('bar-charts/', bar_chart, name='bar_chart'),
]
