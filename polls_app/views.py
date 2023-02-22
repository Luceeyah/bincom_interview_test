from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from .models import *

# Create your views here.

def get_pu_result(request):
    results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=13)
    return render(request, 'pu_result.html', {'results': results})

def getPolls(request):
    polling_units = PollingUnit.objects.filter(polling_unit_id__gt=0)
    return render(request, 'polls.html', {'polls': polling_units})

def getPollByLGA(request, id):
    lga_polls = PollingUnit.objects.filter(lga_id=id)
    return render(request, 'lga_polls.html', {'polls': lga_polls})

def get_sum_of_polling_units(request, id):
    polls = PollingUnit.objects.filter(polling_unit_id__gt=0)
    polling_units = polls.filter(lga_id=id)
    context = {}
    total = 0
    for poll in polling_units:
        context[poll] = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=poll).aggregate(Sum('party_score'))
    for k, v in context.items():
        for x, y in v.items():
            if y == None:
                continue
            else:
                total += y 
    return render(request, 'sum_polling_units.html', {'context': context, 'total':total, 'polls': polls})
# Create your views here.
