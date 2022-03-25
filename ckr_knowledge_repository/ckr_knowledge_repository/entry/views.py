from django.views.generic import ListView, DetailView
from api.models import Entry
from django.shortcuts import render


def home(request):
    context = {
        'entries': Entry.objects.all()
    }
    return render(request, 'Entry/home_page.html', context)


class EntryView(ListView):
    model = Entry
    template_name = 'Entry/home_page.html'
    context_object_name = 'entries'
#     order entries from newest to oldest
    ordering = ['-date']


class EntryDetailView(DetailView):
    model = Entry
    template_name = 'Entry/detail_page.html'
    context_object_name = 'entry'

