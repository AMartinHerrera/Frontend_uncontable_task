from django.shortcuts import render
import json
from .forms import InputForm, ScatterPlotForm
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError
import matplotlib.pyplot as plt


def home(request):
    """View function for home page of site."""

    with open('static/dataset.json') as f:
        data = json.load(f)
    type(data)
    # Output: dict
    keys = []
    for k in data.keys():
        keys.append(k)

    # for k, v in data.items():
    #     print("La clave   ")
    #     print(k)
    #     print("tiene values   ")
    #     print(v)
    #     for val in v.items():
    #         for mv in val:
    #             print("OJOOOO")
    #             print (mv)
    num_experiments = len(data)

    context = {
        'keys': keys,
        'num_experiments': num_experiments,
    }

    return render(request, 'home.html', context=context)

def exp_details(request):

    if request.method == 'POST':
        form = InputForm(request.POST)

    else:
        form = InputForm()

    context = {
        'form': form,
    }

    return render(request, 'exp_details.html', context)


def scatterplot_tool(request):


    if request.method == 'POST':
        form = ScatterPlotForm(request.POST)

    else:
        form = ScatterPlotForm()

    with open('static/dataset.json') as f:
        data = json.load(f)
    type(data)

    context = {
        'form': form,
        'dataset': data,
    }

    return render(request, 'scatterplot_tool.html', context)
