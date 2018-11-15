from django.views.generic.list import ListView, View

class IndexClass(ListView):
    """
    Renders Index.html and Returns recent public activity.
    """
    template_name = 'index.html'


    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(*args, **kwargs)
        return context
