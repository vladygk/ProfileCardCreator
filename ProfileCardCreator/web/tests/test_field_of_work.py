from django.test import TestCase
from django.urls import reverse

from ProfileCardCreator.web.forms import FieldOfWorkForm
from ProfileCardCreator.web.models import Category, FieldOfWork


class FieldOfWorkViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(Name="TestCategory")

    def test_field_of_work_form_valid(self):
        form_data = {"Name": "TestField", "Category": self.category.pk}
        form = FieldOfWorkForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_field_of_work_create_view(self):
        response = self.client.post(reverse("create field"), {"Name": "NewField", "Category": self.category.pk})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(FieldOfWork.objects.filter(Name="NewField").exists())