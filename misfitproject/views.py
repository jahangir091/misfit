from django.views.generic.list import ListView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.conf import settings

class IndexClass(ListView):
    """
    This is index page.
    """

    def get(self, request, *args, **kwargs):
        context_dict = {}
        return render_to_response(
            'index.html',
            RequestContext(request, context_dict))


def manager_required(view):

    def f(request, *args, **kwargs):
        if request.user.groups.filter(name='manager').exists():
            return view(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return f


def hr_required(view):

    def f(request, *args, **kwargs):

        if request.user.groups.filter(name='hr').exists():
            return view(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return f
