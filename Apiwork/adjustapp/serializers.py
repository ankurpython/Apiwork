from rest_framework import serializers
from adjustapp.models import Dataset
from rest_framework.serializers import ModelSerializer

class ApiSerializer(ModelSerializer):
    date=serializers.DateField(required=False)
    channel=serializers.CharField(required=False)
    country=serializers.CharField(required=False)
    imperessions=serializers.IntegerField(required=False)
    os=serializers.CharField(required=False)
    clicks=serializers.IntegerField(required=False)
    installs=serializers.IntegerField(required=False)
    spend=serializers.DecimalField(max_digits=25,decimal_places=2,required=False)
    revenue=serializers.DecimalField(max_digits=25,decimal_places=2,required=False)
    cpi=serializers.FloatField(required=False)

    class Meta:
        model=Dataset
        fields = ['spend','os','installs','revenue','channel','country','impressions','clicks','date',]
