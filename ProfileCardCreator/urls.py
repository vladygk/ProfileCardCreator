from django.contrib import admin
from django.urls import path, include

from ProfileCardCreator.web.views import Custom404View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProfileCardCreator.web.urls')),
]

handler404 = Custom404View.as_view()
