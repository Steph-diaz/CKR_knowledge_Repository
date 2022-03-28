from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from api.models import Entry
from django.shortcuts import render

#
# def home(request):
#     context = {
#         'entries': Entry.objects.all()
#     }
#     return render(request, 'Entry/home_page.html', context)


class EntryView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'Entry/home_page.html'
    context_object_name = 'entries'
#     order entries from newest to oldest
    ordering = ['-date']


class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'Entry/detail_page.html'
    context_object_name = 'entry'


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'Entry/entry_form.html'
    context_object_name = 'entry'
    fields = ['title', 'content', 'type', 'key_words']

    # set author in form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
