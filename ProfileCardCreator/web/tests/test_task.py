from django.contrib.auth import login
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ProfileCardCreator.web.forms import TodoTaskForm
from ProfileCardCreator.web.models import Category, TodoTask, FieldOfWork


class TodoTaskViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(Name="TestCategory")
        self.field_of_work = FieldOfWork.objects.create(Name="TestField", Category=self.category)
        self.user = User.objects.create(username="testuser", password="testpassword")

        self.todo_task = TodoTask.objects.create(
            Title="TestTask", Description="Test Description", Deadline="2023-08-31", FieldOfWork=self.field_of_work,
            Creator=self.user
        )


    def test_todo_task_form_valid(self):
        form_data = {
            "Title": "TestTodoTask",
            "Description": "Test Description",
            "Deadline": "2023-08-31",
            "FieldOfWork": self.field_of_work.pk,
        }
        form = TodoTaskForm(data=form_data)
        self.assertTrue(form.is_valid())



