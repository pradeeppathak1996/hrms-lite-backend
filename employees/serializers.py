from rest_framework import serializers
from .models import Employee
import re

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        extra_kwargs = {
            'employee_id': {
                'error_messages': {
                    'required': 'Employee ID is required.'
                }
            },
            'email': {
                'error_messages': {
                    'required': 'Email is required.',
                    'invalid': 'Enter a valid email address.'
                }
            },
            'full_name': {
                'error_messages': {
                    'required': 'Full name is required.'
                }
            },
            'department': {
                'error_messages': {
                    'required': 'Department is required.'
                }
            }
        }

    def validate(self, data):
        required_fields = ['employee_id', 'full_name', 'email', 'department']
        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError(
                    {field: f"{field.replace('_', ' ').title()} is required."}
                )
        return data

    def validate_employee_id(self, value):
        id_regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]+$'
        if not re.match(id_regex, value):
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
        email_regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        if not re.match(email_regex, value):
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