from django.db import models

# Create your models here.

STATUS_CHOICES = (
		(1, 'New'),
		(2, 'In preparation'),
		(3, 'Wait for products'),
		(4, 'Wrong customer data'),
		(5, 'Canceled due by address'),
		(6, 'DELIVERED'),
		(7, 'RETURN'),
	)

class Orders(models.Model):
	order_id = models.CharField(max_length=5, unique=True)
	customer_id = models.IntegerField()
	delivery_id = models.IntegerField(unique=True)
	name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	company_name = models.TextField(blank=True)
	delivery_street = models.CharField(max_length=255)
	post_code = models.CharField(max_length=255)
	delivery_city = models.CharField(max_length=255)
	delivery_country = models.CharField(max_length=255)
	phone_number = models.IntegerField(blank=True)
	email = models.EmailField(blank=True)
	delivery_product = models.CharField(max_length=255)
	weight = models.DecimalField(max_digits=8, decimal_places=3)
	order_price = models.DecimalField(max_digits=8, decimal_places=2)
	cod = models.DecimalField(max_digits=8, decimal_places=2)
	currency = models.CharField(max_length=5)
	paid = models.CharField(max_length=3)
	delivery_note = models.TextField()
	date_of_addition_order = models.DateField(auto_now_add=True)
	order_status = models.CharField(max_length=4, choices=STATUS_CHOICES, default=1)
	order_status_date = models.DateField(auto_now=True)