from .models import Task
from django.shortcuts import render


# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by("-created_at")
    context = {"tasks": tasks}
    response = render(request, "index.html", context)
    return response
