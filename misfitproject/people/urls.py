
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# from account.views import InviteUserView

# from geonode.people.views import CreateUser, activateuser, UserSignup, InviteUser
from views import UserSignup, ProfileEdit

urlpatterns = patterns('misfitproject.people.views',
                       url(r"^signup/$", UserSignup.as_view(), name="user_signup"),
                       url(r"^loginerror/$", 'loginerror', name="loginerror"),
                       url(r"^(?P<user_id>[0-9]+)/edit/$", ProfileEdit.as_view(),
                           name="profile_edit"),

                       # url(r"^edit/$", ProfileEdit.as_view(), name="profile_edit"),


                       )
