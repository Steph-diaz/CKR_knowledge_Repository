from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.EntryView.as_view(), name='home_page'),
    # re_path("^(?P<pk>\d+)$", view=views.DetailView.as_view(), name="detail_view"),
]
