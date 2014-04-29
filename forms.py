from django import forms
#from django.contrib.localflavor.fr.forms import FRPhoneNumberField
from localflavor.fr.forms import FRRegionField, FRDepartmentField, FRPhoneNumberField

class MyFlavorForm(forms.Form):
    region = FRRegionField()
    department = FRDepartmentField()
    phone_number = FRPhoneNumberField()
