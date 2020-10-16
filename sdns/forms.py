from django import forms

from utilities.forms import BootstrapMixin

from sdns.models import Register

BLANK_CHOICE = (("", "---------"),)


class RegisterForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = Register
        fields = [
            'ip',
            'host',
            'domain',
        ]

class RegisterFilterForm(BootstrapMixin, forms.ModelForm):
    q = forms.CharField(
        required=False,
        label="Search",
    )
   
    class Meta:
        model = Register
        fields = [
            'ip',
            'host',
            'domain',
        ]

