from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
    # paginate_by = 3
#     order entries from newest to oldest
    ordering = ['-updated']


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


# logging required, but also, only author can update entries
class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Entry
    template_name = 'Entry/entry_form.html'
    context_object_name = 'entry'
    fields = ['title', 'content', 'type', 'key_words']

    # set author in form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Func to test if author is the one updating
    def test_func(self):
        # get entry
        item = self.get_object()
        if self.request.user == item.author:
            return True
        return False


class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Entry
    template_name = 'Entry/entry_confirm_delete.html'
    context_object_name = 'entry'
    success_url = '/' # sent to home after deleting

    # Func to test if author is the one updating
    def test_func(self):
        # get entry
        item = self.get_object()
        if self.request.user == item.author:
            return True
        return False
