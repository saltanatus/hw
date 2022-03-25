"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web_program import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('department/employee/<int:id>/', views.EmployeeDeparture.as_view(), name="employee_department"),
    path('department/', views.DepartmentView.as_view(), name="department"),
    # path('department/create/', views.department_create, name="department_create"),
    # path('position/', views.position_view, name="position"),
    path('position/create/', views.PositionCreate.as_view(), name="position_create"),
    path('position/detail/<int:pk>/', views.PositionDetail.as_view(), name="single_positioin"),
    path('position/delete/<int:pk>/', views.PositionDelete.as_view(), name="position_delete"),
    path('position/update/<int:pk>/', views.PopsitionUpdate.as_view(), name="position_update"),
    path('employee/', views.EmployeeView.as_view(), name="employee"),
    path('employee/create/', views.EmloyeeCreate.as_view(), name="employee_create"),
    path('employee/detail/<int:pk>/', views.EmployeeDetail.as_view(), name='single_employee'),
    path('employee/delete/<int:pk>/', views.EmployeeDelete.as_view(), name='employee_delete'),
    path('employee/update/<int:pk>/', views.EmployeeUpdate.as_view(), name="employee_update"),
]
