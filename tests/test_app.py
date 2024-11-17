from http import HTTPStatus

from fastapi.testclient import TestClient

from curso_fastapi_site.app import app

"""
o FastAPI já conta com um cliente de testes no módulo fastapi.testclient com o
objeto TestClient, que precisa receber nosso app como parâmetro.

client = TestClient(app) -> Cria um cliente de testes usando a nossa aplicação
como base.

"""

"""
No nome da função, geralmente escrevemos o que o teste de fato faz.
teste_root_deve_retornar_ok_e_ola_mundo() -> Aqui estamos dizendo que root deve
retornar o status OK e a mensagem "olá mundo". Root é o nome dado a raiz da
URL. O caminho /, que colocamos na definição do @app.get('/'). OK é o status
que diz que a requisição aconteceu com sucesso no protocolo HTTP.

response = client('/') -> Nesse ponto, o client faz uma requisição. Da mesma
forma que o browser, um cliente da API. Nisso, chamamos o endereço de root,
usando o método GET.

assert response.status_code == HTTPStatus.OK --> Aqui fazemos a validação do
código de resposta, para saber se a resposta é referente ao código 200, que
significa OK.

assert response.json() == {'message': 'Olá Mundo!!'} --> No final, validamos se
o dicionário que enviamos na função é o mesmo que recebemos quando fizemos a
requisição.

"""


def teste_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)    # Fase 1 - Organizar (Arrange)

    response = client.get('/')  # Fase 2 - Agir (Act)

    assert response.status_code == HTTPStatus.OK    # Fase 3 - Afirmar (Assert)
    assert response.json() == {'message': 'Olá Mundo!!'}
