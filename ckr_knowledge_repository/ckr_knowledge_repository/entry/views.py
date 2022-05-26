from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from api.models import Entry
from ckr_knowledge_repository.users.models import User
from django.shortcuts import render, get_object_or_404
from django.db.models import Q


class EntryView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'Entry/home_page.html'
    context_object_name = 'entries'
    # paginate_by = 10
#     order entries from newest to oldest
    ordering = ['-updated']

    def get_queryset(self):
        qs = Entry.objects.all()
        entry_number_query = self.request.GET.get('entry_id')
        entry_status_query = self.request.GET.get('entry_status')
        entry_keywords_query = self.request.GET.get('entry_keywords')
        entry_type_query = self.request.GET.get('entry_type')
        # entry_type_author_query = self.request.GET.get('entry_type_author')

        if entry_number_query != '' and entry_number_query is not None:
            qs = qs.filter(id__icontains=entry_number_query)
        elif entry_status_query != '' and entry_status_query is not None:
            qs = qs.filter(Q(status__icontains=entry_status_query) | Q(
                record__icontains=entry_status_query))
        elif entry_keywords_query != '' and entry_keywords_query is not None:
            qs = qs.filter(key_words__icontains=entry_keywords_query)
        elif entry_type_query != '' and entry_type_query is not None:
            qs = qs.filter(type__icontains=entry_type_query).distinct()
        # elif entry_type_author_query != '' and entry_type_author_query is not None:
        #     qs = qs.filter(Q(type__icontains=entry_type_author_query) | Q(
        #         author__name__icontains=entry_type_author_query))
        else:
            qs = qs

        return qs.order_by('-updated')


class UserListView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'Entry/user_entry.html'
    context_object_name = 'entries'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Entry.objects.filter(author=user).order_by('-updated')


class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'Entry/detail_page.html'
    context_object_name = 'entry'


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'Entry/entry_form.html'
    context_object_name = 'entry'
    # fields = ['title', 'content', 'type', 'key_words']
    fields = ['status', 'record', 'title', 'content', 'type', 'key_words', 'links']

    # set author in form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# logging required, but also,
# For only author can update entries add "UserPassesTestMixin" plus uncomment
class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    template_name = 'Entry/entry_form.html'
    context_object_name = 'entry'
    # fields = ['title', 'content', 'type', 'key_words']
    fields = ['entry_number', 'status','record', 'title', 'content', 'type', 'key_words', 'links']

    # set author in form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # # Func to test if author is the one updating
    # def test_func(self):
    #     # get entry
    #     item = self.get_object()
    #     if self.request.user == item.author:
    #         return True
    #     return False


class EntryDeleteView(LoginRequiredMixin,  DeleteView):
    model = Entry
    template_name = 'Entry/entry_confirm_delete.html'
    context_object_name = 'entry'
    success_url = '/' # sent to home after deleting

    # # Func to test if author is the one updating
    # def test_func(self):
    #     # get entry
    #     item = self.get_object()
    #     if self.request.user == item.author:
    #         return True
    #     return False


class EntryHistoryView(LoginRequiredMixin, ListView):
    template_name = "Entry/entry_history_list.html"

    def get_queryset(self):
        history = Entry.history.all()
        return history


class HistoryDetailView(LoginRequiredMixin, DetailView):
    model = Entry.history.model
    template_name = 'Entry/history_detail.html'
    context_object_name = 'history'

