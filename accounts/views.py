from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from .models import Account
# Create your views here.

@api_view(["GET",])
def ListOfAccounts(request):
    List=Account.objects.all()
    serializer=RegistrationSerializer(List,many=True)
    return Response(serializer.data)

@api_view(["GET",])
def single_account(request,pk):
    single=Account.objects.get(id=pk)
    serializer=RegistrationSerializer(single,many=False)
    return Response(serializer.data)


@api_view(["POST",])
def registration(request):
    if request.method =="POST":
        serializer=RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data["response"]="successfully registered"
            data["name"]=account.name
            data["username"]=account.username
            data["calls"]=account.calls
        else:
            data=serializer.errors
        return Response(data)

@api_view(["PUT",])
def update_account(request,pk):
    object=Account.objects.get(id=pk)
    print("true")
    if request.method == "PUT":
        serializer=RegistrationSerializer(object,data=request.data)
        if serializer.is_valid():
            serializer.save()            
        return Response(serializer.data)
    else:
            data=serializer.errors
    