from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from ProfileCardCreator.web.forms.item import ItemForm
from ProfileCardCreator.web.models import Category, FieldOfWork, TodoTask, Item


class ItemViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(Name="TestCategory")
        self.field_of_work = FieldOfWork.objects.create(Name="TestField", Category=self.category)
        self.user = User.objects.create(username="testuser", password="testpassword")
        self.todo_task = TodoTask.objects.create(
            Title="TestTask", Description="Test Description", Deadline="2023-08-31", FieldOfWork=self.field_of_work
            ,Creator=self.user
        )

    def test_item_form_valid(self):
        form_data = {
            "Name": "TestItem",
            "Price": 10,
            "ImageUrl": "https://example.com",
            "TodoTask": self.todo_task.pk,
        }
        form = ItemForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_item_create_view(self):
        response = self.client.post(
            reverse("create item"),
            {"Name": "NewItem", "Price": 10, "ImageUrl": "https://example.com", "TodoTask": self.todo_task.pk},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Item.objects.filter(Name="NewItem").exists())

    def test_item_form_invalid_missing_data(self):
        form_data = {}
        form = ItemForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("Name", form.errors)
        self.assertIn("Price", form.errors)
        self.assertIn("ImageUrl", form.errors)
        self.assertIn("TodoTask", form.errors)