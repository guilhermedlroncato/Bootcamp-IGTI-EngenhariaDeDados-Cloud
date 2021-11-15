from fastapi import FastAPI

app = FastAPI()

@app.get('/api')
async def root():
    return {'message': 'Você está indo muito bem'}

@app.get('/api/{name}')
async def get_user(name):
    return {
        'name': name,
        'message': f'Olá {name} from FastAPI'
    }