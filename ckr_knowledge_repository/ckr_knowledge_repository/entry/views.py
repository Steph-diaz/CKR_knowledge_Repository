from django.views import generic
from api.models import Entry


class EntryView(generic.TemplateView):
    model = Entry
    template_name = 'Entry/home_page.html'
