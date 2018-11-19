import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, BaseCreateView


from forms import UserRequestCreateUpdateForm
from models import UserRequest

# Create your views here.

class UserRequestList(ListView):
    template_name = 'user_request_list.html'
    model = UserRequest

    def get_queryset(self):
        return UserRequest.objects.filter(owner=self.request.user, status='OPEN')


class UserRequestCreate(CreateView):
    """
    This view is for creating new news
    """
    template_name = 'user_request_create.html'
    model = UserRequest
    form_class = UserRequestCreateUpdateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = 'OPEN'
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


    def get_success_url(self):
        return reverse('user_request_list')


class UserRequestUpdate(UpdateView):
    template_name = 'user_request_create.html'
    model = UserRequest
    form_class = UserRequestCreateUpdateForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner == request.user:
            return super(UserRequestUpdate, self).get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Cannot update other's request")

    def get_object(self):
        return UserRequest.objects.get(pk=self.kwargs['request_id'])

    def get_success_url(self):
        return reverse('user_request_list')


class UserRequestDelete(DeleteView):
    template_name = 'user_request_delete.html'
    model = UserRequest

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner == request.user:
            success_url = self.get_success_url()
            self.object.delete()
            return HttpResponseRedirect(success_url)
        else:
            return HttpResponseForbidden("You dont have permission to delete this request")

    def get_success_url(self):
        return reverse('user_request_list')

    def get_object(self):
        return UserRequest.objects.get(pk=self.kwargs['request_id'])


class UserRequestDetails(DetailView):
    """
    This view gives the details of a user request
    """
    template_name = 'user_request_details.html'

    def get_object(self):
        return UserRequest.objects.get(pk=self.kwargs['request_id'])


class UserRequestReviewList(ListView):
    template_name = 'user_request_list.html'
    model = UserRequest

    def get_queryset(self):
        return UserRequest.objects.filter(status='OPEN')


class UserRequestProcessList(ListView):
    template_name = 'user_request_list.html'
    model = UserRequest

    def get_queryset(self):
        return UserRequest.objects.filter(status='REVIEWED')


class AllProcessedUserRequestList(ListView):
    template_name = 'user_request_list.html'
    model = UserRequest

    def get_queryset(self):
        return UserRequest.objects.filter(status='PROCESSED')

    def get_context_data(self, **kwargs):
        context = super(AllProcessedUserRequestList, self).get_context_data(**kwargs)
        context['allprocessed'] = True
        return context



def user_request_review(request, request_id):

    if request.method == 'POST':
        user_request = UserRequest.objects.get(id=request_id)
        user_request.status = 'REVIEWED'
        user_request.reviewed_by = request.user
        user_request.save()
        return HttpResponseRedirect(reverse("user_request_review_list"))


def user_request_process(request, request_id):
    if request.method == 'POST':
        user_request = UserRequest.objects.get(id=request_id)
        user_request.status = 'PROCESSED'
        user_request.processed_by = request.user
        user_request.save()
        return HttpResponseRedirect(reverse("user_request_process_list"))


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path


def render_pdf_view(request):
    template_path = 'user_printer.html'
    if request.user.groups.filter(name='manager').exists() or request.user.groups.filter(name='hr').exists():
        context = {'object_list': UserRequest.objects.all()}
    else:
        context = {'object_list': UserRequest.objects.none()}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="employee_requests_report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(Context(context))

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response