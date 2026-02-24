# from rest_framework import generics
# from .models import Employee
# from .serializers import EmployeeSerializer

# class EmployeeListCreateView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeDeleteView(generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'id'


# from rest_framework import generics, status
# from rest_framework.response import Response
# from .models import Employee
# from .serializers import EmployeeSerializer

# class EmployeeListCreateView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {"message": "Employee added successfully"},
#                 status=status.HTTP_201_CREATED
#             )

#         # 👇 THIS IS IMPORTANT
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )



# employees/views.py

from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer