from rest_framework import serializers
from .models import Attendance
from datetime import date
from django.utils import timezone


class AttendanceSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)

    def validate_date(self, value):
        today = timezone.localdate() 

        if value != today:
            raise serializers.ValidationError(
                "Attendance can only be marked for today."
            )

        return value

    class Meta:
        model = Attendance
        fields = '__all__'

    def validate(self, data):

        if data['date'] != date.today():
            raise serializers.ValidationError("Attendance can only be marked for today.")

        if Attendance.objects.filter(
            employee=data['employee'],
            date=data['date']
        ).exists():
            raise serializers.ValidationError("Attendance already marked for this date.")

        return data