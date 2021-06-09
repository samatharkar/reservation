from django import forms
from .models import *

# Model form for DeviceType model with all fields
class DeviceTypeForm(forms.ModelForm):

	class Meta:
		model = DeviceType
		fields = '__all__'

# Model form for Vendor model with all fields
class VendorForm(forms.ModelForm):

	class Meta:
		model = Vendor
		fields = '__all__'

# Model form for Consumable model with all fields
class ConsumableForm(forms.ModelForm):

	class Meta:
		model = Consumable
		fields = '__all__'

# Model form for Team model with all fields
class TeamForm(forms.ModelForm):

	class Meta:
		model = Team
		fields = '__all__'

# Model form for Device model with all fields
class DeviceForm(forms.ModelForm):

	class Meta:
		model = Device
		fields = '__all__'
		# Convert all date fields into input type=date for the templates
		widgets = {
            'po_date': forms.DateInput(attrs={'type': 'date'}),
            'shipped_date': forms.DateInput(attrs={'type': 'date'}),
            'arrival_date': forms.DateInput(attrs={'type': 'date'}),
            'added_date': forms.DateInput(attrs={'type': 'date'}),
        }

# Model form for SetupType model with all fields
class SetupTypeForm(forms.ModelForm):

	class Meta:
		model = SetupType
		fields = '__all__'

# Model form for Setup model with all fields
class MakeSetupForm(forms.ModelForm):

	class Meta:
		model = Setup
		fields = '__all__'