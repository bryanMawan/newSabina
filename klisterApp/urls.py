from django.urls import path
from .views import formPageView, create_form, change_filepath, change_password

urlpatterns = [

    path('', create_form, name='home'),
    path('change-filepath/', change_filepath, name='change_filepath'),
    path('change_password/', change_password, name='change_password'),


    ]