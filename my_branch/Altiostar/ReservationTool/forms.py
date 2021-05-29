from django import forms
from .models import *


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
		fields = '__all__'


class AddSetupTypeForm(forms.ModelForm):

	class Meta:
		model = SetupType
		fields = '__all__'


class CreateSetupForm(forms.ModelForm):

	class Meta:
		model = CreateSetup
		fields = '__all__'


class MakeSetupForm(forms.ModelForm):

	class Meta:
		model = MakeSetup
		fields = '__all__'