# coding=utf-8
from django import forms
from .models import Orders

STATUS_CHOICES = (
        (1, 'New'),
        (2, 'In preparation'),
        (3, 'Wait for products'),
        (4, 'Wrong customer data'),
        (5, 'Canceled due by address'),
        (6, 'DELIVERED'),
        (7, 'RETURN'),
    )

class OrdersForm(forms.Form):
    # orders = Orders.objects.all()
    # order_id = Orders.objects.get('order_id')
    order_id = forms.CharField(max_length=200)
    status_field = forms.ChoiceField(choices=STATUS_CHOICES)

