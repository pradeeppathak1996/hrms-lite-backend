from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def home(request):
    return JsonResponse({"status": "HRMS Lite Backend is running"})


urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/employees/", include("employees.urls")),
    path("api/attendance/", include("attendance.urls")),
]