from django.shortcuts import redirect, render, get_object_or_404
from index.forms import infoForm
from index.models import info
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


    return render(request, "index/home.html", {
        "infos": infos,
        'events': events,
    })

# def home(request):
#     raw_items = date.objects.values_list('date', flat=True)
#     from datetime import datetime
#     sorted_items = sorted(raw_items, key=lambda x: datetime.strptime(x, "%Y %B %d"))
#     clean_dates = [d[5:] for d in sorted_items]

#     return render(request, 'home.html', {'dates': clean_dates})

def Info(request, id):
    data = get_object_or_404(info, id=id)
    month_num = data.month
    month_name = calendar.month_name[month_num]
    context = {
        "Info": data,           
        "monthName": month_name, 
    }
    return render(request, 'index/info.html', context)
    


def fillform(request):
    form = infoForm()
    return render(request, "index/forms.html", {
        "form":form
    })

def submitform(request):

    print(request.POST)

    info.objects.create(
        month = request.POST.get("month"),
        date = request.POST.get("date"),
        name = request.POST.get("name"),
        videoPhoto = request.POST.get("videoPhoto"),
        description = request.POST.get("description"),
        credit = request.POST.get("credit")

    )

    return redirect("index.home")

# def dates(request, id):
    
#     # monthDay = str(date.date)
#     # idfy = monthDay.replace(" ", "-")
#     data = get_object_or_404(date, id=id)
#     context={
#         "data":data,
       
#              }
    
#     return render(request, "index/dates.html", context)




def dates(request, monthAndDate):
    
    
    data = date.objects.filter(date__endswith=monthAndDate.replace("-", " ")).order_by("?").first()
    data.date
    context={
        "data":data,
       
             }
    
    return render(request, "index/dates.html", context)

# def dates(request, j):
#     id = 0
#     for i in range(366):
#         idata= get_object_or_404(date, id=i+1)
#         idate = str(idata.date)
#         maxLetter = len(idate)
#         equi = idate[5:maxLetter]
#         equi.replace("-", " ")

#         if j == equi:
#             id = i+1
#             print(id)
        

#     data = get_object_or_404(date, id=id)
#     context={
#         "data":data,
       
#              }
    
#     return render(request, "index/dates.html", context)