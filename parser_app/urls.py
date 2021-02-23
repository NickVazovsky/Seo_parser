from django.urls import path
from .views import send_form, result_view

urlpatterns =[
    path('', send_form, name='start_page'),
    path('result/', result_view, name='result')
]