from django.urls import path
from .views import *
urlpatterns = [
    path('tui-bubble-chart/', bubble_chart, name='bubble_chart'),
]
