from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from adjustapp.views import DataListFilter

router=DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('s',include('adjustapp.urls')),
]

urlpatterns.extend(router.urls)
