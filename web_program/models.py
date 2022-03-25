from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)
    max_amount = models.IntegerField()

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    birth = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    STATUS_CHOICE = [
        ('work', 'Работает'),
        ('fired', 'Уволен'),
        ('maternity leave', 'Декретный отпуск')
    ]
    status = models.CharField(max_length=50, default='work', choices=STATUS_CHOICE)

