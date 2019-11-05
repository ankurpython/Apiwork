from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from adjustapp.models import Dataset
from adjustapp.serializers import ApiSerializer
from adjustapp.filters import UserFilter
from rest_framework import generics
from rest_framework.permissions import AllowAny

class DataListFilter(generics.ListAPIView):
    serializer_class=ApiSerializer
    queryset=Dataset.objects.all()
    filter_backends=(DjangoFilterBackend,)
    filter_class=UserFilter
    permission_classes=(AllowAny,)


    def get_queryset(self):
        queryset=self.queryset.extra(select={"cpi":"spend/installs"})
        fields=[fields.name for field in Dataset._meta.get_fields()]
        fields.append('cpi')
        return queryset
