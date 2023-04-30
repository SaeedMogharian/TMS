from .models import Task, Contractor, Employer
# from .forms import SignupForm

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
import logging


# Create your views here.

def index(request):
    """main page for displaying tasks"""

    # read last page number visited by user from cookies
    tasks = Task.objects.all().order_by("-created_at")
    # paginator = Paginator(tasks, PAGINATION_PER_PAGE)
    # page = paginator.get_page(page_number)
    # context = {
    #     "task_page": page,
    #     "user": request.user,
    #     "form": SignupForm(),
    #     "user_type": "کارفرما" if hasattr(request.user, "employer") else "پیمانکار",
    #     "is_employer": hasattr(request.user, "employer"),
    # }

    response = render(request, "index.html")
    # response.set_cookie("page_number", str(page_number))
    return response
