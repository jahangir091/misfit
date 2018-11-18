from django import forms
from django.conf import settings
from account.models import EmailAddress
from account.forms import SignupForm
from django.utils.translation import ugettext_lazy as _



class UserSignupForm(SignupForm):
    usertype = forms.ChoiceField(
        required=True,
        choices=[
            ("MEMBER", _("Member")),
            ("HR", _("HR Member")),
            ("MANAGER", _("Manager"))],
        )

    def clean_email(self):
        value = self.cleaned_data["email"]
        if not value.endswith('@misfit.tech'):
            raise forms.ValidationError(_("Email address must be ends with '@misfit.tech'."))
        qs = EmailAddress.objects.filter(email__iexact=value)
        if not qs.exists() or not settings.ACCOUNT_EMAIL_UNIQUE:
            return value
        raise forms.ValidationError(_("A user is registered with this email address."))
