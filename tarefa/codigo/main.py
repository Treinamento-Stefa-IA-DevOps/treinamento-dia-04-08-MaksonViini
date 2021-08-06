import pickle
from fastapi import FastAPI


app = FastAPI()


@app.post('/model')
# Coloque seu codigo na função abaixo
async def titanic(Sex: int, Age: float, Lifeboat: int, Pclass: int):
    """
    Method: POST
    Sex: Sexo da pessoa. EX: 0/1, Parametro binario
    Age: Idade da pessoa. Ex: 35
    Lifeboat: Numero do barco salva vidas. EX: 1, 2, 3...
    Pclass: Classe no navio. EX: 1 - Primeira classe, 2 - Segunda classe ...
    """
    try:
        with open('model/Titanic.pkl', 'rb') as fid:
            titanic = pickle.load(fid)

        pred = titanic.predict([[Sex, Age, Lifeboat, Pclass]]).tolist()[0]

        return {
            'survived': pred,
            'status': 200,
            'message': 'Valor predito com sucesso!',
        }
    except Exception as exception:
        return {
            'Error': exception,
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
