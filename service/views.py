from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from service.models import Dish


# Create your views here.
@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_dishes = Dish.objects.all().count()

    context = {
        "num_dishes": num_dishes,
    }
    return render(request, "service/index.html", context=context)


class DishesListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    queryset = Dish.objects.all()
