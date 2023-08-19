from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.urls import reverse

from ProfileCardCreator.web.forms import CategoryForm
from ProfileCardCreator.web.models import Category


class CategoryViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )

        self.group = Group.objects.create(name='Stuff_group')
        self.user.groups.add(self.group)

    def test_category_form_valid(self):
        form_data = {"Name": "TestCategory"}
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_category_create_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse("create category"), {"Name": "NewCategory"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(Name="NewCategory").exists())
        