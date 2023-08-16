from django.urls import path

from ProfileCardCreator.ProfileCardCreatorApp.views import IndexView

urlpatterns = (path("", IndexView.as_view(), name="index"),)
