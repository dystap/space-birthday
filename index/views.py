from django.shortcuts import redirect, render, get_object_or_404
from index.models import date
import calendar
import datetime

def home(request):
    infos = date.objects.all()

    dates_queryset = list(date.objects.all().order_by('date'))
    dates_queryset.sort(key=lambda x: datetime.datetime.strptime(x.date, "%Y %B %d").replace(year=2020))
    events = []
    for date_object in dates_queryset:
        monthAndDate = date_object.date[5:].replace(" ","-")
        if monthAndDate in events:
            continue
        else:
            events.append(monthAndDate)


    return render(request, "index/index.html", {
        "infos": infos,
        'events': events,
    })


def dates(request, monthAndDate):
    
    
    data = date.objects.filter(date__endswith=monthAndDate.replace("-", " ")).order_by("?").first()
    
    context={
        "data":data,
       
             }
    
    return render(request, "index/dates.html", context)
