from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from service.models import Dish, Cook, DishType

User = get_user_model()


class DishViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")

        # Створюємо об'єкт DishType перед тим, як використовувати його в Dish
        self.dish_type = DishType.objects.create(name="Main Course")

        self.dish = Dish.objects.create(
            name="Pizza",
            description="Cheese and tomato",
            price=10.99,
            dish_type=self.dish_type  # ВАЖЛИВО: передаємо dish_type
        )

    def test_dishes_list_view(self):
        response = self.client.get(reverse("service:dishes"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pizza")

    def test_dish_detail_view(self):
        response = self.client.get(
            reverse("service:dish-detail", kwargs={"pk": self.dish.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cheese and tomato")

    def test_dish_create_view(self):
        response = self.client.post(reverse("service:dish-create"), {
            "name": "Pasta",
            "description": "Creamy sauce",
            "price": 12.99,
            "dish_type": self.dish_type.id  # Додаємо dish_type
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Dish.objects.filter(name="Pasta").exists())

    def test_dish_update_view(self):
        response = self.client.post(
            reverse("service:dish-update", kwargs={"pk": self.dish.pk}), {
                "name": "Pizza Margherita",
                "description": "Updated description",
                "price": 11.99,
                "dish_type": self.dish_type.id  # Додаємо dish_type
            })
        self.dish.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.dish.name, "Pizza")

    def test_dish_delete_view(self):
        response = self.client.post(
            reverse("service:dish-delete", kwargs={"pk": self.dish.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Dish.objects.filter(pk=self.dish.pk).exists())


class CookViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        self.cook = Cook.objects.create(username="cook1", email="cook1@example.com",
                                        first_name="John", last_name="Doe",
                                        years_of_experience=5)

    def test_cook_list_view(self):
        response = self.client.get(reverse("service:cook-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cook1")

    def test_cook_detail_view(self):
        response = self.client.get(
            reverse("service:cook-detail", kwargs={"pk": self.cook.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")

    def test_cook_create_view(self):
        response = self.client.post(reverse("service:cook-create"),
                                    {"username": "cook2", "email": "cook2@example.com",
                                     "first_name": "Jane", "last_name": "Doe",
                                     "years_of_experience": 3})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Cook.objects.filter(username="cook2").exists())

    def test_cook_update_view(self):
        response = self.client.post(
            reverse("service:cook-update", kwargs={"pk": self.cook.pk}),
            {"username": "cook1_updated", "email": "cook1@example.com",
             "first_name": "John", "last_name": "Doe", "years_of_experience": 6})
        self.cook.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.cook.username, "cook1_updated")

    def test_cook_delete_view(self):
        response = self.client.post(
            reverse("service:cook-delete", kwargs={"pk": self.cook.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Cook.objects.filter(pk=self.cook.pk).exists())
