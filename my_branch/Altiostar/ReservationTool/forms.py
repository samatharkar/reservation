from django import forms
from .models import *


class DeviceTypeForm(forms.ModelForm):

	class Meta:
		model = DeviceType
		fields = '__all__'


class VendorForm(forms.ModelForm):

	class Meta:
		model = Vendor
		fields = '__all__'


class ConsumableForm(forms.ModelForm):

	class Meta:
		model = Consumable
		fields = '__all__'



class TeamForm(forms.ModelForm):

	class Meta:
		model = Team
		fields = '__all__'


class DeviceForm(forms.ModelForm):

	class Meta:
		model = Device
		exclude = ['setup']
		widgets = {
            'po_date': forms.DateInput(attrs={'type': 'date'}),
            'shipped_date': forms.DateInput(attrs={'type': 'date'}),
            'arrival_date': forms.DateInput(attrs={'type': 'date'}),
            'added_date': forms.DateInput(attrs={'type': 'date'}),
        }


class SetupTypeForm(forms.ModelForm):

	class Meta:
		model = SetupType
		fields = '__all__'


class MakeSetupForm(forms.ModelForm):

	class Meta:
		model = Setup
		fields = '__all__'