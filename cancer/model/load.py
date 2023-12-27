import pickle,os
from django.conf import settings

def loads(inp):
    try:
        os.chdir(settings.BASE_DIR)
        model="Model.Lung"
        model=pickle.load(open(model,"rb"))
        modelPrediction=model.predict([inp])
        if(modelPrediction == 1):
            return True
        else:
            return False
    except Exception as e:
        raise Exception(str(e))
    

def loadbreastmodel(inp):
    try:
        os.chdir(settings.BASE_DIR)
        model="Model.Breast"
        model=pickle.load(open(model,"rb"))
        modelPrediction=model.predict([inp])
        if(modelPrediction == 0):
            return "Malignant"
        else:
            return "Benign"
    except Exception as e:
        raise Exception(str(e))
    
    
