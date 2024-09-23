from django.urls import path
from . import views
urlpatterns = [
    path('employee-all', views.employee_all, name="employee_all"),
    path('employee_details/<int:id>', views.employee_details, name="employee_details")
]
