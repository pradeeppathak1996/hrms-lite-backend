from rest_framework import serializers
from .models import Employee
import re

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def validate(self, data):
        request = self.context.get("request")
        if request and request.method in ["POST", "PUT", "PATCH"]:
            required_fields = ['employee_id', 'full_name', 'email', 'department']
            for field in required_fields:
                if not data.get(field):
                    raise serializers.ValidationError(
                        {field: f"{field.replace('_', ' ').title()} is required."}
                    )
        return data

    def validate_employee_id(self, value):
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]+$', value):
            raise serializers.ValidationError(
                "Employee ID must contain both letters and numbers (Example: EMP001)."
            )
        return value

    def validate_full_name(self, value):
        if not re.match(r'^[A-Za-z ]+$', value):
            raise serializers.ValidationError(
                "Name should contain only letters."
            )
        return value

    def validate_email(self, value):
        if not re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', value):
            raise serializers.ValidationError(
                "Enter a valid email address."
            )
        return value

    def validate_department(self, value):
        if not re.match(r'^[A-Za-z ]+$', value):
            raise serializers.ValidationError(
                "Department should contain only letters."
            )
        return value