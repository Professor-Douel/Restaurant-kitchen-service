
from django.urls import path

from service.views import index, DishesListView

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishesListView.as_view(), name="dishes-list"),
]

app_name = "service"
