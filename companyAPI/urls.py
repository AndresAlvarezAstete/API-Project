from django.conf.urls import url
from django.urls import path
from django.urls import path
from .views import CompanyDetailView, CompanyListView

urlpatterns = [
    path('company/', CompanyListView.as_view(), name='company_list'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company'),
]
