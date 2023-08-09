from django.urls import path,include
from cancer.controller.predictController import LungCancerPredict





urlpatterns = [
    path('lung-predict',LungCancerPredict.as_view())
    
]