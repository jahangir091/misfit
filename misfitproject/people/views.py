from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView
from account.views import SignupView
from account import signals
from account.forms import SignupForm, LoginUsernameForm
from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from forms import UserSignupForm, ProfileUpdateForm
from models import Profile
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


class ProfileEdit(UpdateView):
    template_name = 'profile_edit.html'
    model = Profile
    form_class = ProfileUpdateForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object == request.user:
            return super(ProfileEdit, self).get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You cannot update other's profile")

    def get_object(self):
        return Profile.objects.get(pk=self.kwargs['user_id'])

    def get_success_url(self):
        return reverse('home')