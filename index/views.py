from django.shortcuts import redirect, render, get_object_or_404
from index.forms import infoForm
from index.models import info
from index.models import date
import calendar


def home(request):
    infos = date.objects.all()
    dates_queryset = date.objects.all().order_by('date')


    return render(request, "index/home.html", {
        "infos": infos,
        'events': dates_queryset,
    })

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




def dates(request, id):
    numbers = list(range(1,367))
    numbers.reverse()
    realID = numbers[id-1]
    
    data = get_object_or_404(date, id=realID)
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