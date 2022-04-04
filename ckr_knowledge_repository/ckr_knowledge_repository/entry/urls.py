from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.EntryView.as_view(), name='home_page'),
    path('entry/<int:pk>/', views.EntryDetailView.as_view(), name='entry_detail'),
    path('entry/new/', views.EntryCreateView.as_view(), name='entry_create'),
    path('entry/<int:pk>/update/', views.EntryUpdateView.as_view(), name='entry_update'),
    path('entry/<int:pk>/delete/', views.EntryDeleteView.as_view(), name='entry_delete'),
    path('entry/archives/', views.EntryHistoryView.as_view(), name='entry_archives'),
    # re_path("^(?P<pk>\d+)$", view=views.DetailView.as_view(), name="detail_view"),
]
