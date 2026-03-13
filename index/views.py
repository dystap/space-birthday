from django.shortcuts import redirect, render


def home(request):
  
    return render(request, "index/home.html", {})

# Create your views here.


