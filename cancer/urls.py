from django.urls import path,include
from cancer.controller.lungpredictController import LungCancerPredict
from cancer.controller.breastpredictController import BreastCancerPredict





urlpatterns = [
    path('lung-predict',LungCancerPredict.as_view()),
    path('breast-predict',BreastCancerPredict.as_view())

    
]