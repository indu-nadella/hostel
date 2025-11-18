from django import forms
from hostel.models import HostelPersonDetails,HostelFeeDetails,HostelMenu

class person_details(forms.ModelForm):
    class Meta:
        model=HostelPersonDetails
        fields='__all__'

class fee_details(forms.ModelForm):
    class Meta:
        model=HostelFeeDetails
        fields='__all__'

class menu_details(forms.ModelForm):
    class Meta:
        model=HostelMenu
        fields='__all__'

