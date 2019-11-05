from django.urls import path
from adjustapp.views import DataListFilter

urlpatterns = [
    path('data', DataListFilter.as_view(),name='data'),
]
