import pickle
from fastapi import FastAPI, HTTPException


app = FastAPI()


@app.post('/model')
# Coloque seu codigo na função abaixo
async def titanic(Sex: int, Age: float, Lifeboat: int, Pclass: int):
    with open('model/Titanic.pkl', 'rb') as fid:
        titanic = pickle.load(fid)

    pred = titanic.predict([[Sex, Age, Lifeboat, Pclass]]).tolist()[0]

    try:
        return {
            'survived': pred,
            'status': 200,
            'message': 'Valor predito com sucesso!',
        }
    except Exception:
        return {
            'message': 'Internal server error'
        }


@app.get('/model')
async def get():
    return {
        'hello': 'test'
    }


@app.get('/')
async def init():
    return {
        'message': 'sucess'
    }
