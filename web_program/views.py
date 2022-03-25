from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Department, Position, Employee
from .forms import DepartmentForm, PositionForm, EmployeeForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class DepartmentView(ListView):
    model = Department
    template_name = 'department_view.html'

class EmployeeView(ListView):
    model = Employee
    template_name = 'employee_view.html'

class EmployeeDeparture(ListView):
    pass



class PositionDetail(DetailView):
    model = Position
    template_name = 'single_position.html'

class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'single_employee.html'
    
    
class PositionCreate(CreateView):
    model = Position
    fields = '__all__'
    template_name = 'add.html'

class EmloyeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'add.html'


class PositionDelete(DeleteView):
    model = Position
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('department_view')

class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'delete_confirm.html'

    success_url = reverse_lazy('employee_view')


class PopsitionUpdate(UpdateView):
    model = Position
    template_name = "add.html"
    fields = '__all__'
    success_url = reverse_lazy('employee')

class EmployeeUpdate(UpdateView):
    model = Employee
    template_name = "add.html"
    fields = '__all__'
    success_url = reverse_lazy('employee')


# def position_update(request, id):
#     position = Position.objects.get(id=id)
#     if request.method == "GET":
#         form = PositionForm()
#         return render(request, 'add.html', {'form':form})
#     if request.method == "POST":
#         form= PositionForm(request.POST, instance=position)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("departmentgit"))
#         else:
#             return render(request, 'add.html', {'form':form})

# def employee_update(request, id):
#     employee = Employee.objects.get(id=id)
#     if request.method == "GET":
#         form = EmployeeForm()
#         return render(request, "add.html", {"form":form})
#     if request.method == "POST":
#         form = EmployeeForm(request.POST, instance=employee)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("employee"))
#         else:
#             return render(request, "add.html", {"form":form})


# def department_view(request):
#     department = Department.objects.all()
#     return render(request, 'department_view.html', {'pandas':department})


# def position_view(request):
#     position = Position.objects.all()
#     return render(request, 'position_view.html', {'pandas': position})


# def employee_view(request):
#     employee = Employee.objects.all()
#     return render(request, "employee_view.html", {"pandas": employee})


# def employee_in_departure_view(request, id):
#     department = Department.objects.get(id=id)
#     employee = Position.objects.filter(department=department)
#     return render(request, "position_view.html", {"pandas": employee})



# def department_create(request):
#     if request.method == "GET":
#         form = DepartmentForm()
#         return render(request, 'add.html', {'form':form})
#     if request.method == "POST":
#         form = DepartmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('department'))
#         else:
#             return render(request, 'add.html', {'form':form})


# def position_create(request):
#     if request.method == "GET":
#         form = PositionForm()
#         return render(request, 'add.html', {'form':form})
#     if request.method == "POST":
#         form= PositionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("position"))
#         else:
#             return render(request, 'add.html', {'form':form})


# def employee_create(request):
#     if request.method == "GET":
#         form = EmployeeForm()
#         return render(request, "add.html", {"form":form})
#     if request.method == "POST":
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("employee"))
#         else:
#             return render(request, "add.html", {"form":form})



