# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # The root URL for 'myapp' goes to the index view
    path('run_creation_contract/', views.run_creation_contract, name='run_creation_contract'),  # URL for running the script
]
