from django.db import models

# Create your models here.

class Employee(models.Model):
	EmpName = models.CharField(max_length=30)
	EmpID = models.IntegerField()
	Designation = models.CharField(max_length=40)
	SalaryPackage = models.IntegerField()
	Department = models.CharField(max_length=40)
	Experience = models.IntegerField()

class News(models.Model):
	occation = models.CharField(max_length=1000)

class Calendar(models.Model):
	Date = models.CharField(max_length=15)
	Occation = models.CharField(max_length=500)