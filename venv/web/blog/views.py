from typing import Any
from django.shortcuts import render
from django.http import HttpRequest , HttpResponse , JsonResponse
from .models import Loan
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST 

from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now

from django.views.generic import View
from rest_framework.generics import ListAPIView




time = lambda : now()

# this


@csrf_exempt 
@require_POST 
def get_the_loan(requests:HttpRequest)->HttpResponse:
    # send the user 
    user =  User.objects.get(
        username = requests.POST.get('username')
    )
    
    context = {
        'load' : (Loan.objects.filter(
            author = user
        ))
    }
    return HttpResponse((context))





@csrf_exempt 
@require_POST 
def create_the_loan(requests:HttpRequest)->HttpResponse:
    user = User.objects.get(username = requests.POST.get('username'))
    Loan.objects.create(
        author = user , 
        price = requests.POST.get('price') , 
        datetime_get = time() , 
        datetime_push = requests.POST.get('datetime_push')  , 
        is_settle = 0 
    )
    return JsonResponse({'status':'ok'})
##########################class base view in django base views 
from django.http import HttpResponse , HttpRequest
class MixinGetPostDetails():
    query = ... 
    template_name = ...
    url_pk = 'pk'
    def __init__(self) -> None:
        self.context = {}
    def GET(self ,requests , ID_, *args , **kwargs): # get all contex and return last off fus 
        self.context['object'] = self.query.get(ID = ID_)
        
        
    def POST(self ,requests, *args , **kwargs):... # save Post 
    # SOBE KHELY KHASTE BOODAYM     

    def get_context(self):
        return self.context

    def as_views(self):
        def render(requests :HttpRequest):
            if requests.method == "GET":
                self.GET()
            else : 
                self.POST()
            return render()
#post detials 
"""
GET 
post.object.get 
POST 
save POST With Detials 
PUT 
update 


"""
class GetPostDetails(MixinGetPostDetails):
    def GET(self, *args, **kwargs):
    
        return super().GET(*args, **kwargs)
# API VIEWS 

from rest_framework.generics import ListAPIView  , ListCreateAPIView
