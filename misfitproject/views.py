from django.views.generic.list import ListView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader

class IndexClass(ListView):
    """
    This is index page.
    """

    def get(self, request, *args, **kwargs):
        context_dict = {}
        return render_to_response(
            'index.html',
            RequestContext(request, context_dict))

