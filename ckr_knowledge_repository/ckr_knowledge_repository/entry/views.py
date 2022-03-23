from django.views import generic
from api.models import Entry
from django.shortcuts import render


def home(request):
    context = {
        'posts': Entry.objects.all()
    }
    return render(request, 'Entry/home_page.html', context)


# class EntryView(generic.TemplateView):
#     model = Entry
#     template_name = 'Entry/home_page.html'
