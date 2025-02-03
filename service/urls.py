
from django.urls import path

from service.views import index, DishesListView, DishCreateView, DishDetailView, \
    DishUpdateView, DishDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishesListView.as_view(), name="dishes"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
]

app_name = "service"
