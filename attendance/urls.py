from django.urls import path
from .views import (
    AttendanceListCreateView,
    DashboardSummaryView,
    EmployeePresentSummaryView,
    EmployeeAttendanceDetailView,
)

urlpatterns = [
    path("", AttendanceListCreateView.as_view()),
    path("dashboard/", DashboardSummaryView.as_view()),
    path("present-summary/", EmployeePresentSummaryView.as_view()),
    path("<int:employee_id>/", EmployeeAttendanceDetailView.as_view()),
]