from django.db import models 
from django.utils import timezone  

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	photo = models.URLField(blank=True)
	location = models.CharField(max_length=100)
	create_at = models.DateTimeField(editable=False, null=True, blank=True, auto_now_add=True)
	date_filed = models.DateField(default=timezone.now)
	category = models.ForeignKey('Category',blank = True,null = True)

	def __str__(self): #更改Post的表示方式
		return self.title

class Category(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

