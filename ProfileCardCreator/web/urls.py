from django.urls import path

from ProfileCardCreator.web.views import IndexView, RegisterView, LoginView\
    , LogoutView, TasksListView, CreateTaskView\
    , CategoryListView, CategoryCreateView\
    , FieldOfWorkCreateView, FieldOfWorkListView\
    , SubtaskCreateView, SubtaskListView\
    , ItemCreateView, ItemListView, ItemDetailView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("tasks/", TasksListView.as_view(), name="all tasks"),
    path("create-task/", CreateTaskView.as_view(), name="create task"),
    path("categories/", CategoryListView.as_view(), name="all categories"),
    path("create-category/", CategoryCreateView.as_view(), name="create category"),
    path("fields/", FieldOfWorkListView.as_view(), name="all fields"),
    path("create-field/", FieldOfWorkCreateView.as_view(), name="create field"),
    path("subtasks/", SubtaskListView.as_view(), name="all subtasks"),
    path("create-subtask/", SubtaskCreateView.as_view(), name="create subtask"),
    path("items/<int:pk>", ItemDetailView.as_view(), name="details item"),
    path("items/", ItemListView.as_view(), name="all items"),
    path("create-item/", ItemCreateView.as_view(), name="create item"),

]
