from django.urls import path
from .views import create_the_loan , get_the_loan



# this is the simple uri 
urlpatterns = [
    path('create/loan/' , create_the_loan , name="create_load"),
    path('get/loan/' , get_the_loan , name = "get_loan"),

]
