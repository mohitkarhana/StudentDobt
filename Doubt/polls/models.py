
from django.db import models

# Create your models here.
class Student(models.Model):
	"""This Models is used for student details"""
	name = models.CharField(max_length=20,null=True,blank=True)
	roll_no=models.CharField(max_length=10,unique=True)
	standard = models.CharField(max_length=100,null=True, blank=True)

	class Meta:
		db_table = 'student'

	unique_togter = ('name','roll_no')


	def __str__(self):
		return self.name

class Doubt(models.Model):
	"""This Model is used for Doubt"""
	question = models.CharField(max_length=100, null=True, blank=True)
	question_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
	student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)

