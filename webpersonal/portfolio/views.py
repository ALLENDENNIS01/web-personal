from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = P roject.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects':projects})