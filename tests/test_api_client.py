import pytest
import requests
from unittest.mock import Mock
from src.code import APIClient


# Fixture que crea una instancia del cliente API para las pruebas
@pytest.fixture
def api_client():
    return APIClient()


# Fixture que crea una respuesta HTTP simulada con datos de prueba
@pytest.fixture
def mock_response():
    mock = Mock()
    mock.json.return_value = {
        "nombre": "Aaron",
        "apellido": "Flores",
        "email": "a.flores.a@uni.pe",
        "estado": "disponible",
    }
    mock.status_code = 200
    return mock


# Prueba el caso exitoso de obtener datos de usuario
def test_happy_path(mocker, api_client, mock_response):
    mock_get = mocker.patch("requests.get", create_autospec=True)
    mock_get.return_value = mock_response

    result = api_client.get_user_data(1)

    assert result["nombre"] == "Aaron"
    assert result["apellido"] == "Flores"
    assert result["email"] == "a.flores.a@uni.pe"
    assert result["estado"] == "disponible"
    mock_get.assert_called_once_with("https://test.net/data/1")


# Prueba el manejo de errores HTTP
def test_api_error(mocker, api_client):
    mock_get = mocker.patch("requests.get", create_autospec=True)
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "404 No encontrado"
    )
    mock_get.return_value = mock_response

    with pytest.raises(requests.exceptions.HTTPError):
        api_client.get_user_data(-1)

    mock_get.assert_called_once_with("https://test.net/data/-1")


# Prueba el mecanismo de reintentos: 4 fallos seguidos de 1 éxito
def test_api_error_con_intentos(mocker, api_client, mock_response):
    mock_get = mocker.patch("requests.get", create_autospec=True)

    # Registramos al mock que obtengan las primeras 4 llamadas erroneas
    fail_responses = []
    for i in range(4):
        fail_response = Mock()
        fail_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
            "500 Server Error"
        )
        fail_responses.append(fail_response)

    # Usar el mock_response original para la respuesta exitosa
    mock_response.raise_for_status.return_value = None
    mock_response.status_code = 200

    # Configurar el mock para devolver las 4 respuestas fallidas seguidas de la exitosa
    mock_get.side_effect = fail_responses + [mock_response]

    # Bucle que llama 5 veces a get_user_data
    result = None
    for i in range(5):
        if i < 4:
            try:
                api_client.get_user_data(1)
            except requests.exceptions.HTTPError:
                pass
        else:
            result = api_client.get_user_data(1)

    # Validar número de llamadas realizadas
    assert mock_get.call_count == 5

    # Validar los datos obtenidos
    assert result["nombre"] == "Aaron"
    assert result["apellido"] == "Flores"
    assert result["email"] == "a.flores.a@uni.pe"
    assert result["estado"] == "disponible"
