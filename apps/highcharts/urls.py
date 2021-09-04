from django.urls import path
from .views import *

urlpatterns = [
    path('bar-chart/', bar_line_chart, name='bar_chart'),
    path('area-chart/', area_chart, name='area_chart'),
    path('bullet-chart/', bullet_chart, name='bullet_chart'),
]
