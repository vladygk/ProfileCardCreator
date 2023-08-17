from django.urls import path

from ProfileCardCreator.web.views import IndexView, RegisterView, LoginView \
    , LogoutView, TasksListView, CreateTaskView \
    , CategoryListView, CategoryCreateView \
    , FieldOfWorkCreateView, FieldOfWorkListView \
    , SubtaskCreateView, SubtaskListView \
    , ItemCreateView, ItemListView, ItemDetailView, CategoryDeleteView \
    , FieldOfWorkDeleteView, ItemDeleteView, SubtaskDeleteView \
    , TaskDeleteView, TaskMarkAsDoneView, TodoTaskUpdateView, Custom403View\
    , Custom404View, AddUserToGroupView, RemoveUserToGroupView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("tasks/", TasksListView.as_view(), name="all tasks"),
    path("create-task/", CreateTaskView.as_view(), name="create task"),
    path("tasks/<int:pk>", TaskMarkAsDoneView.as_view(),name="complete task"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="delete task"),
    path("tasks/<int:pk>/edit/", TodoTaskUpdateView.as_view(), name="edit task"),

    path("categories/", CategoryListView.as_view(), name="all categories"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="delete category"),
    path("create-category/", CategoryCreateView.as_view(), name="create category"),

    path("fields/", FieldOfWorkListView.as_view(), name="all fields"),
    path("fields/<int:pk>/delete/", FieldOfWorkDeleteView.as_view(), name="delete field"),
    path("create-field/", FieldOfWorkCreateView.as_view(), name="create field"),

    path("subtasks/", SubtaskListView.as_view(), name="all subtasks"),
    path("subtasks/<int:pk>/delete/", SubtaskDeleteView.as_view(), name="delete subtask"),
    path("create-subtask/", SubtaskCreateView.as_view(), name="create subtask"),

    path("items/<int:pk>", ItemDetailView.as_view(), name="details item"),
    path("items/", ItemListView.as_view(), name="all items"),
    path("create-item/", ItemCreateView.as_view(), name="create item"),
    path("items/<int:pk>/delete/", ItemDeleteView.as_view(), name="delete item"),

    path('error/', Custom403View.as_view(), name='custom 403 error'),

    path('add-group/', AddUserToGroupView.as_view(), name='add group'),
    path('remove-group/', RemoveUserToGroupView.as_view(), name='remove group'),
]


handler404 = Custom404View.as_view()

