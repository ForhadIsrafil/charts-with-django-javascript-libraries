from django.urls import path
from .views import *

urlpatterns = [
    path('highcharts-bar-chart/', bar_chart, name='bar_chart'),
]
