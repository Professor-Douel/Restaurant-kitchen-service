from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from service.models import Dish


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    num_dishes = Dish.objects.all().count()

    context = {
        'num_dishes': num_dishes,
    }
    return render(request, "service/index.html", context=context)
