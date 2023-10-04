from django.urls import path, include

urlpatterns = [
    path('api/company', include("company.urls"))
]
