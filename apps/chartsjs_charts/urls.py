from django.urls import path
from .views import *

name = 'charts_js'
urlpatterns = [
    path('bar-chart/', bar_chart, name='bar_chart'),
    path('line-chart/', line_chart, name='line_chart'),
    path('bubble-chart/', bubble_chart, name='bubble_chart'),
    path('radar-chart/', radar_chart, name='radar_chart'),
]
