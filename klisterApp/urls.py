from django.urls import path
from .views import create_form, change_filepath, change_password, SuccessView

urlpatterns = [

    path('', create_form, name='home'),
    path('change-filepath/', change_filepath, name='change_filepath'),
    path('change_password/', change_password, name='change_password'),
    path('success/', SuccessView.as_view(), name='success'),
    ]

