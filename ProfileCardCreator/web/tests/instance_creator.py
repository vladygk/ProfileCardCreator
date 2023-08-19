from django.contrib.auth.models import User

from ProfileCardCreator.web.models import FieldOfWork, TodoTask, Category, Item, Subtask


class CreateInstance:
    def __new__(cls):
        raise TypeError("This is a static class and cannot be instantiated.")

    @staticmethod
    def create_task():
        field_of_work = CreateInstance.create_field_of_work()

        creator = User.objects.create_user(username="creator_user", password="password123")
        assignee = User.objects.create_user(username="assignee_user", password="password456")

        todo_task = TodoTask.objects.create(
            Title="Example Task",
            Description="Task description",
            Deadline="2023-12-31",
            IsCompleted=False,
            FieldOfWork=CreateInstance.create_field_of_work(),
            Creator=creator,
            Assignee=assignee,
        )
        return todo_task

    @staticmethod
    def creat_category():
        category = Category.objects.create(Name="test category")
        return category

    @staticmethod
    def create_field_of_work():
        field = FieldOfWork.objects.create(Name="test field of work", Category=CreateInstance.creat_category())
        return field

    @staticmethod
    def create_item():
        item = Item.objects.create(
            Name="Example Item",
            Price=100,  # Specify the item's price
            ImageUrl="https://example.com/item-image.jpg",  # Provide a valid URL
            TodoTask=CreateInstance.create_task(),
        )

    @staticmethod
    def create_subtask():
        subtask = Subtask.objects.create(Title="test subtask", TodoTask=CreateInstance.create_task())

