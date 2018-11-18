from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from account.views import SignupView
from account import signals
from account.forms import SignupForm, LoginUsernameForm
from forms import UserSignupForm
# Create your views here.


class UserSignup(SignupView):
    form_class = UserSignupForm

    def after_signup(self, form):
        signals.user_signed_up.send(sender=UserSignupForm, user=self.created_user, form=form)

        #added the created user to the desired group
        user = self.created_user
        user_type = self.request.POST['usertype']
        if user_type == 'MANAGER':
            user_group, created = Group.objects.get_or_create(name='manager')
            user_group.user_set.add(user)
        elif user_type == 'HR':
            user_group, created = Group.objects.get_or_create(name='hr')
            user_group.user_set.add(user)
        else:
            user_group, created = Group.objects.get_or_create(name='member')
            user_group.user_set.add(user)
