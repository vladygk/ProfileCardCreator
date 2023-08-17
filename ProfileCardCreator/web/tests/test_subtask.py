from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ProfileCardCreator.web.forms import SubtaskForm
from ProfileCardCreator.web.models import Category, FieldOfWork, TodoTask, Subtask


class SubtaskViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(Name="TestCategory")
        self.field_of_work = FieldOfWork.objects.create(Name="TestField", Category=self.category)
        self.user = User.objects.create(username="testuser", password="testpassword")
        self.todo_task = TodoTask.objects.create(
            Title="TestTask", Description="Test Description", Deadline="2023-08-31", FieldOfWork=self.field_of_work
            , Creator=self.user
        )

    def test_subtask_form_valid(self):
        form_data = {"Title": "TestSubtask", "TodoTask": self.todo_task.pk}
        form = SubtaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_subtask_create_view(self):
        response = self.client.post(
            reverse("create subtask"), {"Title": "NewSubtask", "TodoTask": self.todo_task.pk}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Subtask.objects.filter(Title="NewSubtask").exists())