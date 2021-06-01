from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Submit


class AddDeviceTypeForm(forms.ModelForm):

	class Meta:
		model = DeviceType
		fields = '__all__'


class AddVendorForm(forms.ModelForm):

	class Meta:
		model = Vendor
		fields = '__all__'


class AddConsumableForm(forms.ModelForm):

	class Meta:
		model = Consumable
		fields = '__all__'



class AddTeamForm(forms.ModelForm):

	class Meta:
		model = Team
		fields = '__all__'


class AddDeviceForm(forms.ModelForm):

	class Meta:
		model = Device
		exclude = ['setup']
		widgets = {
            'po_date': forms.DateInput(attrs={'type': 'date'}),
            'shipped_date': forms.DateInput(attrs={'type': 'date'}),
            'arrival_date': forms.DateInput(attrs={'type': 'date'}),
            'added_date': forms.DateInput(attrs={'type': 'date'}),
        }


class AddSetupTypeForm(forms.ModelForm):

	class Meta:
		model = SetupType
		fields = '__all__'


class MakeSetupForm(forms.ModelForm):

	class Meta:
		model = Setup
		fields = '__all__'