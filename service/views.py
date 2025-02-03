from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
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
    template_name = "service/dishes_list.html"
    context_object_name = "dishes"


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "service/dish_detail.html"
    context_object_name = "dish"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    template_name = "dish_form.html"
    success_url = reverse_lazy("service:dishes")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    template_name = "dish_form.html"
    success_url = reverse_lazy("service:dishes")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "service/dish_confirm_delete.html"
    success_url = reverse_lazy("service:dishes")
