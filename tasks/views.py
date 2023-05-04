from .models import Task
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

def index(request):
    """main page for displaying tasks"""

    # read last page number visited by user from cookies
    tasks = Task.objects.all().order_by("-created_at")
    # paginator = Paginator(tasks, PAGINATION_PER_PAGE)
    # page = paginator.get_page(page_number)
    context = {
        # "task_page": page,
        # "user": request.user,
        # "form": SignupForm(),
        # "user_type": "کارفرما" if hasattr(request.user, "employer") else "پیمانکار",
        # "is_employer": hasattr(request.user, "employer"),
        "tasks": tasks
    }

    response = render(request, "index.html", context)
    # response.set_cookie("page_number", str(page_number))
    return response
