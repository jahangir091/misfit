from django import forms
from misfitproject.request.models import UserRequest


class UserRequestCreateUpdateForm(forms.ModelForm):

    class Meta:
        model = UserRequest
        fields = ['title', 'description']
