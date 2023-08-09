from cancer.model.load import loads

class LungCancerPredictService:
    
    def __init__(self,request:dict) -> None:
        self.request=request
        self.dataList=[]
        self.convert()

    def convert(self):
        for i in self.request.data:
            self.dataList.append(self.request.data.get(i))

    def predict(self):
        try:
            return loads(self.dataList)
        except Exception as e:
            print(e)
            raise Exception(str(e))
