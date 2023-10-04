from django.urls import path

from company.views.auth import LoginAPIView


urlpatterns = [
    path("/", LoginAPIView.as_view(), name="")
]
