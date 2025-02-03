
from django.urls import path

from service.views import index, DishesListView, DishCreateView, DishDetailView

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishesListView.as_view(), name="dishes"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/", DishDetailView.as_view(), name="dish-detail"),
]

app_name = "service"
