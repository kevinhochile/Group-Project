from django import forms
from django.db.models import fields
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'phone', 'order_description', 'credentials',
                  'image')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Gender',
            'state': 'State',
            'phone': 'Credentials',
            'order_description': 'Specialty',
            'credentials': 'Is Opioid Prescriber?',
            'image': 'Total Prescriptions'
        }
