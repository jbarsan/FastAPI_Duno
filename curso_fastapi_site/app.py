from fastapi import (
    FastAPI,  # Importando da biblioteca fastapi o objeto FastAPI
)

app = FastAPI()  # Iniciando uma aplicação FastAPI

"""
@app.get('/') -> Definindo um endpoint com o endereço / acessível pelo
método HTTP GET.
read_root() -> Função que será executada quando o endereço / for acessado por
um cliente.
{'message': 'Olá Mundo!!'} -> Os dados que serão retornados pelo endereço
quando for chamado.
"""


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!!'}
