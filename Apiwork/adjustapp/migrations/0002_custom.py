from django.db import migrations
import pandas as pd

class Migrations(migrations.Migration):
    def import_data(apps,schema_editor):
        data_set=apps.getmodelI('adjustapp','Dataset')
        sample_dataset_df=pd.read_csv('dataset.csv',sep=',')
        data_set_record=[]

        for row in sample_dataset_df.index:
            data_set_record.append(data_set(
            date=sample_dataset_df.ix[row]['date'],
            channel = sample_dataset_df.ix[row]['channel'],
            country=sample_dataset_df.ix[row]['country'],
            os=sample_dataset_df.ix[row]['os'],
            impressions=sample_dataset_df.ix[row]['impressions'],
            clicks=sample_dataset_df.ix[row]['clicks'],
            installs=sample_dataset_df.ix[row]['installs'],
            spend=sample_dataset_df.ix[row]['spend'],
            revenue=sample_dataset_df.ix[row]['revenue'],

            ))
        data_set.objects.bulk_create(data_set_record)

    dependencies=[('adjustapp','0001_inital'),]

    operations=[
    migrations.RunPython(import_data)
    ]
