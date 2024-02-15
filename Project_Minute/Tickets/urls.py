
from django.urls import path
from .import views


urlpatterns = [
    path('file_parcel/',views.import_from_excel)
    

]
