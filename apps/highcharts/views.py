from django.shortcuts import render, redirect
import json, os
from django.contrib.staticfiles import finders  # Given a relative file path, find an absolute file path.
import pandas as pd
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, F, Sum, Avg
from django.db.models.functions import ExtractYear, ExtractMonth
from django.http import JsonResponse
from .models import *

csv_path = os.path.join(os.path.dirname(__file__), 'data.csv')


def bar_line_chart(request):
    '''x='Year', y='Completion', text='Completion'''
    get_csv_data = pd.read_csv(csv_path, )
    bar_group = get_csv_data.groupby('Year', as_index=False).sum()
    bar_group = bar_group.drop('Unnamed: 16', axis=1)
    # print(json.loads(bar_group.head().to_json(orient='records')))
    data = bar_group.head().to_json(orient='records')
    context = {
        'years': bar_group.Year.astype(int).to_list(),
        'completion': bar_group.Completion.astype(int).to_list(),
        'gas_production': bar_group.GasProd.astype(int).to_list(),
        'data': data,
    }
    return render(request, 'highcharts_templates/bar_line_chart.html', context)


def area_chart(request):
    '''x='Year', y='Completion', text='Completion'''
    get_csv_data = pd.read_csv(csv_path, )
    bar_group = get_csv_data.groupby('Year', as_index=False).sum()
    bar_group = bar_group.drop('Unnamed: 16', axis=1)
    # print(json.loads(bar_group.head().to_json(orient='records')))
    data = bar_group.head().to_json(orient='records')
    context = {
        'years': bar_group.Year.astype(int).to_list(),
        'completion': bar_group.Completion.astype(int).to_list(),
        'gas_production': bar_group.GasProd.astype(int).to_list(),
        'data': data,
    }
    return render(request, 'highcharts_templates/area_chart.html', context)


def bullet_chart(request):
    '''x='Year', y='Completion', text='Completion'''
    get_csv_data = pd.read_csv(csv_path, )
    bar_group = get_csv_data.groupby('Year', as_index=False).sum()
    bar_group = bar_group.drop('Unnamed: 16', axis=1)
    # print(json.loads(bar_group.head().to_json(orient='records')))
    data = bar_group.head().to_json(orient='records')
    context = {
        'years': bar_group.Year.astype(int).to_list(),
        'completion': bar_group.Completion.astype(int).to_list(),
        'gas_production': bar_group.GasProd.astype(int).to_list(),
        'data': data,
    }
    return render(request, 'highcharts_templates/bullet_chart.html', context)


def column_chart(request):
    '''x='Year', y='Completion', text='Completion'''
    get_csv_data = pd.read_csv(csv_path, )
    bar_group = get_csv_data.groupby('Year', as_index=False).sum()
    bar_group = bar_group.drop('Unnamed: 16', axis=1)
    # print(json.loads(bar_group.head().to_json(orient='records')))
    data = bar_group.head().to_json(orient='records')
    context = {
        'years': bar_group.Year.astype(int).to_list(),
        'completion': bar_group.Completion.astype(int).to_list(),
        'gas_production': bar_group.GasProd.astype(int).to_list(),
        'data': data,
    }
    return render(request, 'highcharts_templates/column_chart.html', context)


def dependency_wheel_chart(request):
    '''x='Year', y='Completion', text='Completion'''
    get_csv_data = pd.read_csv(csv_path, )
    bar_group = get_csv_data.groupby('Year', as_index=False).sum()
    bar_group = bar_group.drop('Unnamed: 16', axis=1)
    # print(json.loads(bar_group.head().to_json(orient='records')))
    data = bar_group.head().to_json(orient='records')
    context = {
        'years': bar_group.Year.astype(int).to_list(),
        'completion': bar_group.Completion.astype(int).to_list(),
        'gas_production': bar_group.GasProd.astype(int).to_list(),
        'data': data,
    }
    return render(request, 'highcharts_templates/dependency_wheel_chart.html', context)


def heatmap_chart(request):
    '''x='Year', y='Completion', text='Completion'''
    get_csv_data = pd.read_csv(csv_path, )
    bar_group = get_csv_data.groupby('Year', as_index=False).sum()
    bar_group = bar_group.drop('Unnamed: 16', axis=1)
    # print(json.loads(bar_group.head().to_json(orient='records')))
    data = bar_group.head().to_json(orient='records')
    context = {
        'years': bar_group.Year.astype(int).to_list(),
        'completion': bar_group.Completion.astype(int).to_list(),
        'gas_production': bar_group.GasProd.astype(int).to_list(),
        'data': data,
    }
    return render(request, 'highcharts_templates/heatmap_chart.html', context)

def pie_chart(request):
    '''x='Year', y='Completion', text='Completion'''
    get_csv_data = pd.read_csv(csv_path, )
    bar_group = get_csv_data.groupby('Year', as_index=False).sum()
    bar_group = bar_group.drop('Unnamed: 16', axis=1)
    # print(json.loads(bar_group.head().to_json(orient='records')))
    data = bar_group.head().to_json(orient='records')
    context = {
        'years': bar_group.Year.astype(int).to_list(),
        'completion': bar_group.Completion.astype(int).to_list(),
        'gas_production': bar_group.GasProd.astype(int).to_list(),
        'data': data,
    }
    return render(request, 'highcharts_templates/pie_chart.html', context)

