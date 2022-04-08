import email
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User,UserManager
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.
@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
    user=User(username=data["username"],password=data['password'],email=data['email'])
    try : 
        user.save()
        testdata={"status":"200","username":str(data['username']),"password":str(data['password']),"email":str(data['email'])}
    except :
        testdata={"status":"201","create_user":"False"}
    return JsonResponse(testdata)
