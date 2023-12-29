import pickle,os
from django.conf import settings

def loads(inp):
    try:
        os.chdir(settings.BASE_DIR)
        model="Model.Lung"
        model=pickle.load(open(model,"rb"))
        modelPrediction=model.predict([inp])
        if(modelPrediction == 1):
            return "Yes You are effected by lung Cancer"
        else:
            return "No You are not effected by lung cancer"
    except Exception as e:
        raise Exception(str(e))
    

def loadbreastmodel(inp):
    try:
        os.chdir(settings.BASE_DIR)
        model="Model.Breast"
        model=pickle.load(open(model,"rb"))
        modelPrediction=model.predict([inp])
        if(modelPrediction == 0):
            return "Malignant! Your Breast Cancer is"
        else:
            return "Benign! Your Breast Cancer is"
    except Exception as e:
        raise Exception(str(e))
    
    
