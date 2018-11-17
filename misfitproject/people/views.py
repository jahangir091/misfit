from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from account.views import SignupView
from account import signals
from account.forms import SignupForm, LoginUsernameForm
# Create your views here.


class UserSignup(SignupView):

    def after_signup(self, form):
        signals.user_signed_up.send(sender=SignupForm, user=self.created_user, form=form)

        #added the created user to the desired group
        user = self.created_user
        user_type = self.request.POST['usertype']
        if user_type == 'MANAGER':
            user_group = Group.objects.get(name='manager')
            user_group.user_set.add(user)
        elif user_type == 'HR':
            user_group = Group.objects.get(name='hr')
            user_group.user_set.add(user)
        else:
            user_group = Group.objects.get(name='member')
            user_group.user_set.add(user)
