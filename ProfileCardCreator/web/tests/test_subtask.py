from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.urls import reverse

from ProfileCardCreator.web.forms import SubtaskForm
from ProfileCardCreator.web.models import Category, FieldOfWork, TodoTask, Subtask
from ProfileCardCreator.web.tests.instance_creator import CreateInstance


class SubtaskViewsTestCase(TestCase):
    def setUp(self):
        self.category = CreateInstance.creat_category()
        self.field_of_work = CreateInstance.create_field_of_work()

        self.group = Group.objects.create(name='Stuff_group')
        self.user, _ = User.objects.update_or_create(username="testuser", password=make_password("testpassword"))

        self.user.groups.add(self.group)
        self.todo_task = CreateInstance.create_task()

    def test_subtask_form_valid(self):
        form_data = {"Title": "TestSubtask", "TodoTask": self.todo_task.pk}
        form = SubtaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_subtask_create_view(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(
            reverse("create subtask"), {"Title": "NewSubtask", "TodoTask":self.todo_task.pk}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Subtask.objects.filter(Title="NewSubtask").exists())