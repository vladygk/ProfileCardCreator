from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from ProfileCardCreator.web.forms.item import ItemForm
from ProfileCardCreator.web.models import Category, FieldOfWork, TodoTask, Item
from django.contrib.auth.models import User, Group

from ProfileCardCreator.web.tests.instance_creator import CreateInstance


class ItemViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test_user", password=make_password("testpassword"))
        self.group = Group.objects.create(name='Stuff_group')
        self.category = CreateInstance.creat_category()
        self.field_of_work = CreateInstance.create_field_of_work()
        self.todo_task = CreateInstance.create_task()

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
        self.user.groups.add(self.group)
        self.client.login(username='test_user', password='testpassword')

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
