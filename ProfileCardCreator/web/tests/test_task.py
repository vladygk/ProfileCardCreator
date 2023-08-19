from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.urls import reverse

from ProfileCardCreator.web.forms import TodoTaskForm
from ProfileCardCreator.web.models import Category, TodoTask, FieldOfWork


class TodoTaskViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(Name="TestCategory")
        self.field_of_work = FieldOfWork.objects.create(Name="TestField", Category=self.category)
        self.user = User.objects.create(username="testuser", password=make_password("testpassword"))
        self.group = Group.objects.create(name='Stuff_group')
        self.todo_task = TodoTask.objects.create(
            Title="TestTask", Description="Test Description", Deadline="2023-08-31", FieldOfWork=self.field_of_work
            , IsCompleted=False,
            Creator=self.user, Assignee=self.user
        )
        self.user.groups.add(self.group)

    def test_todo_task_form_valid(self):
        form_data = {
            "Title": "TestTodoTask",
            "Description": "Test Description",
            "Deadline": "2023-08-31",
            "FieldOfWork": self.field_of_work.pk,
            "IsCompleted": "False",
            "Creator": self.user.pk,
            "Assignee": self.user.pk
        }
        form = TodoTaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_todo_task_create_view(self):
        self.user.groups.add(self.group)
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(
            reverse("create task"), {"Title": "TestTodoTask", "Description": "Test Description",
                                     "Deadline": "2023-08-31",
                                     "FieldOfWork": self.field_of_work.pk, "Creator": self.user.pk,
                                     "Assignee": self.user.pk}
        )
        self.assertEqual(response.status_code, 302)

        self.assertTrue(TodoTask.objects.filter(Title="TestTodoTask").exists())
