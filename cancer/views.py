from django.shortcuts import render
from rest_framework import viewsets
from .models import breast,lung
from .serializers import breastSerializers,lungSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view
import pickle

class breastViewSet(viewsets.ModelViewSet):
    queryset = breast.objects.all()
    serializer_class = breastSerializers

@api_view(["GET","POST"])
def test(request):
    print("Hi")
    if request['method']=='GET':
        return {"data":"Hello world"}
    mdl = pickle.load('Model.Breast')
    mydata = request.data.values()
    unit = ([[mydata]])
    mdl_pre = mdl.predict(unit)
    print(mdl_pre)

class lungViewSet(viewsets.ModelViewSet):
    queryset = lung.objects.all()
    serializer_class = lungSerializers


