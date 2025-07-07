import pytest
import src.code


# Definimos dos fixtures que manejen datos de prueba reutilizables en otras pruebas
@pytest.fixture
def user_info():
    data = {"nombre": "Aaron", "apellido": "Flores", "edad": 19, "codigo": "20221346A"}
    return data


@pytest.fixture
def authenticated_client_fixture(user_info):
    def authenticate(user_data):
        user_data["codigo_validacion"] = "unova4ever123"
        user_data["hash_verificacion"] = "asdfghjklñ"
        return user_data

    return authenticate


# Prueba de validación de consisntencia de datos entre ambos fixtures
def test_data_consistency(user_info, authenticated_client_fixture):
    authenticated_data = authenticated_client_fixture(user_info)
    assert isinstance(authenticated_data, dict)
    assert authenticated_data["nombre"] == "Aaron"
    assert authenticated_data["apellido"] == "Flores"
    assert authenticated_data["edad"] == 19
    assert authenticated_data["codigo"] == "20221346A"
    assert authenticated_data["codigo_validacion"] == "unova4ever123"
    assert authenticated_data["hash_verificacion"] == "asdfghjklñ"


# Prueba de comparación entre datos obtenidos mediante ambos fixtures
def test_authentication_new_data(user_info, authenticated_client_fixture):
    original_keys = set(user_info.keys())
    authenticated_data = authenticated_client_fixture(user_info)
    authenticated_keys = set(authenticated_data.keys())
    assert "codigo_validacion" in authenticated_keys
    assert "hash_verificacion" in authenticated_keys
    assert original_keys.issubset(authenticated_keys)
    assert len(authenticated_keys) == len(original_keys) + 2


# Prueba marcada como fallida que verifica que no existen datos de autenticacion presentes en un usuario sin autenticar
@pytest.mark.xfail
def test_user_no_authenticated(user_info):
    assert "codigo_validacion" in user_info
    assert "hash_verificacion" in user_info


# Prueba marcada para saltar debido a la nula implementación de la función de FA2
@pytest.mark.skip
def test_user_fa2(user_info, authenticated_client_fixture):
    authenticated_user = authenticated_client_fixture(user_info)
    fa2_authenticated_user = src.code.fa2_authenticate(authenticated_user)
    assert isinstance(fa2_authenticated_user, dict)
    assert fa2_authenticated_user["validacion"] == True
