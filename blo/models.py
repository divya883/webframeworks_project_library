from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import date
import uuid

# Create your models here.

class Book(models.Model):
	b_id=models.IntegerField()
	b_name=models.CharField(max_length=100)
	b_author=models.CharField(max_length=100,null=True)
	b_publisher=models.CharField(max_length=100)
	b_year=models.IntegerField()
	b_img_src=models.CharField(max_length=100)
	b_describe=models.CharField(max_length=2000)

	def __str__(self):
		return self.b_name


class BookInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	#imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)
	borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	
	BOOK_STATUS = (
		('a', 'Available'),
		('b', 'Borrowed'),
	)

	status = models.CharField(
	max_length=1,
	choices=BOOK_STATUS,
	blank=True,
	default='a')

	

	def __str__(self):
		return '{0} ({1})'.format(self.id, self.book.b_name)
