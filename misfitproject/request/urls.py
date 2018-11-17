
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from misfitproject.views import manager_required, hr_required

# from account.views import InviteUserView

# from geonode.people.views import CreateUser, activateuser, UserSignup, InviteUser
from views import UserRequestList, UserRequestCreate, UserRequestUpdate, UserRequestDelete, UserRequestDetails
from views import UserRequestReviewList, UserRequestProcessList, AllProcessedUserRequestList, user_request_review

urlpatterns = patterns('misfitproject.people.views',
                       url(r"^list/$", UserRequestList.as_view(), name="user_request_list"),
                       url(r"^create/$", UserRequestCreate.as_view(), name="user_request_create"),
                       url(r"^(?P<request_id>[0-9]+)/update/$", UserRequestUpdate.as_view(), name="user_request_update"),
                       url(r"^(?P<request_id>[0-9]+)/delete/$", UserRequestDelete.as_view(), name="user_request_delete"),
                       url(r"^(?P<request_id>[0-9]+)/details/$", UserRequestDetails.as_view(), name="user_request_details"),
                       url(r"^(?P<request_id>[0-9]+)/requestreview/$", hr_required(user_request_review), name="user_request_review"),
                       url(r"^reviewlist/$", hr_required(UserRequestReviewList.as_view()), name="user_request_review_list"),
                       url(r"^processlist/$", manager_required(UserRequestProcessList.as_view()), name="user_request_process_list"),
                       url(r"^allprocessed/$", manager_required(AllProcessedUserRequestList.as_view()), name="user_request_allprocessed_list"),

                       )
