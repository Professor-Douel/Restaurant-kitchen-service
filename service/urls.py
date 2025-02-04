from django.contrib.auth.views import LoginView
from django.urls import path

from service.views import (
    index,
    DishesListView,
    DishCreateView,
    DishDetailView,
    DishUpdateView,
    DishDeleteView,
    CookDetailView,
    CookListView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView
)

urlpatterns = [
    path(
        "",
        index,
        name="index"
    ),
    path(
        "dishes/",
        DishesListView.as_view(),
        name="dishes"
    ),
    path(
        "dishes/create/",
        DishCreateView.as_view(),
        name="dish-create"
    ),
    path(
        "dish/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "dish/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dish/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete"
    ),
    path(
        "login/",
        LoginView.as_view(),
        name="login"
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        "cook/create/",
        CookCreateView.as_view(),
        name="cook-create"
    ),
    path(
        "cook/<int:pk>/update/",
        CookUpdateView.as_view(),
        name="cook-update"
    ),
    path(
        "cook/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete"
        ),
]

app_name = "service"
