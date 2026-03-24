from django.shortcuts import redirect, render
from index.forms import infoForm
from index.models import info


def home(request):
    infos = info.objects.all()

    return render(request, "index/home.html", {
        "infos": infos,
    })

def Info(request, id):
    Info = info.objects.filter(id=id).first()

    if not Info:
        raise
    return render(request, 'index/info.html', {
        "Info": Info,
    })


def fillform(request):
    form = infoForm()
    return render(request, "index/forms.html")

def submitform(request):
    info.objects.create(
        month = request.POST.get("month"),
        date = request.POST.get("date"),
        name = request.POST.get("name"),
        videoPhoto = request.POST.get("videoPhoto"),
        description = request.POST.get("description"),
        credit = request.POST.get("credit")

    )

    return redirect("index.home")
