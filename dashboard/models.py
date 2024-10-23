from django.db import models
from django.contrib.auth.models import User #to get users from admin avccount
# Create your models here.

CATEGORY = (
	('Stationary','Stationary'),
	('Electronics','Electronics'),
	('Food','Food')


	)
class Product(models.Model):
	name = models.CharField(max_length=100,null=True)
	category = models.CharField(max_length=20, choices=CATEGORY ,null=True)
	quantity = models.PositiveIntegerField(null=True)

	class Meta:  #incase want to change the name of db in admin 
		verbose_name_plural = "Products"

def __str__(self):
	return f"{self.name} {self.quantity}"

class Order(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
	staff = models.ForeignKey(User,models.CASCADE, null=True) #getting form the database od=f admin called user
	order_quantity =  models.PositiveIntegerField(null=True)
	date  = models.DateTimeField(auto_now_add=True)

	class Meta:
		    verbose_name_plural = "Orders"

def __str__(self):
	return f"{self.product} ordered by {self.staff.username}"



    
