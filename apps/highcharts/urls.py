from django.urls import path
from .views import *

urlpatterns = [
    path('bar-chart/', bar_line_chart, name='bar_chart'),
    path('area-chart/', area_chart, name='area_chart'),
    path('bullet-chart/', bullet_chart, name='bullet_chart'),
    path('column-chart/', column_chart, name='column_chart'),
    path('dependency-wheel-chart/', dependency_wheel_chart, name='dependency_wheel_chart'),
    path('heatmap-chart/', heatmap_chart, name='heatmap_chart'),
    path('pie-chart/', pie_chart, name='pie_chart'),
]
