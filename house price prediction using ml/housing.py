import uvicorn
from fastapi import FastAPI
from para import house_data
import pickle
app = FastAPI()
pickleo = open("re.pkl","rb")
model=pickle.load(pickleo)

@app.get('/')
def index():
    return {'Deployment': 'Hello and Welcome to Pranit'}

@app.post('/predict')
def predict(data:house_data):
    data = data.dict()
    MedInc=data['MedInc']
    HouseAge=data['HouseAge']
    AveRooms=data['AveRooms']
    AveBedrms=data['AveBedrms']
    Population=data['Population']
    AveOccup=data['AveOccup']
    Latitude=data['Latitude']
    Longitude=data['Longitude']


    prediction = model.predict([[MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude]])
    
    return {
        'prediction': prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)