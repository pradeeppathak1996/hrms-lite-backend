from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count, Q
from .models import Attendance
from .serializers import AttendanceSerializer
from employees.models import Employee

class AttendanceListCreateView(generics.ListCreateAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        queryset = Attendance.objects.all().order_by("-date")

        date = self.request.query_params.get("date")
        employee_id = self.request.query_params.get("employee")

        if date:
            queryset = queryset.filter(date=date)

        if employee_id:
            queryset = queryset.filter(employee_id=employee_id)

        return queryset

class EmployeeAttendanceDetailView(APIView):
    def get(self, request, employee_id):
        try:
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)

        attendance_records = Attendance.objects.filter(
            employee_id=employee_id
        ).order_by("-date")

        total_days = attendance_records.count()
        total_present = attendance_records.filter(status="Present").count()
        total_absent = attendance_records.filter(status="Absent").count()

        attendance_percentage = (
            (total_present / total_days) * 100 if total_days > 0 else 0
        )

        data = {
            "employee_name": employee.full_name,
            "total_days": total_days,
            "present": total_present,
            "absent": total_absent,
            "attendance_percentage": round(attendance_percentage, 2),
            "records": attendance_records.values("id", "date", "status"),
        }

        return Response(data)

class EmployeePresentSummaryView(APIView):
    def get(self, request):
        summary = (
            Employee.objects
            .annotate(
                total_present=Count(
                    "attendance",
                    filter=Q(attendance__status="Present")
                )
            )
            .values("id", "full_name", "total_present")
        )

        return Response(summary)

class DashboardSummaryView(APIView):
    def get(self, request):
        total_employees = Employee.objects.count()
        total_attendance = Attendance.objects.count()
        total_present = Attendance.objects.filter(status="Present").count()
        total_absent = Attendance.objects.filter(status="Absent").count()

        return Response({
            "total_employees": total_employees,
            "total_attendance": total_attendance,
            "total_present": total_present,
            "total_absent": total_absent,
        })