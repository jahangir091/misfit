
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from account.views import InviteUserView

# from geonode.people.views import CreateUser, activateuser, UserSignup, InviteUser

urlpatterns = patterns('misfitproject.people.views',
                       # url(r'^$', TemplateView.as_view(template_name='people/profile_list.html'),
                       #     name='profile_browse'),
                       # url(r"^edit/$", "profile_edit", name="profile_edit"),
                       # url(r"^edit/(?P<username>[^/]*)$", "profile_edit", name="profile_edit"),
                       # url(r"^profile/(?P<username>[^/]*)/$", "profile_detail", name="profile_detail"),
                       # url(r'^forgotname', 'forgot_username', name='forgot_username'),
                       # url(r'^create/$', CreateUser.as_view(), name='create-user'),
                       # url(r'^active-inactive-user/(?P<username>[^/]*)$', activateuser, name='active-inactive-user'),
                       url(r"^signup/$", UserSignup.as_view(), name="user_signup"),

                       #invite user
                       # url(r"^invite_user/$", InviteUser.as_view(), name="invite_user"),
                       #
                       # #user message inbox
                       # url(r'^inbox', 'inbox', name='message-inbox-extend'),
                       )
