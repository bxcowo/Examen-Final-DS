import subprocess
import requests


# Función que retorna una supuesta dirección original del binario en el ordenador
def get_binary():
    return "original path"


# Función para ejecutar el comando binario con todos los argumentos disponiblrs
def exec_binary_full(path, nombre, apellido, edad, codigo):
    return subprocess.run(
        [
            path,
            "--nombre",
            nombre,
            "--apellido",
            apellido,
            "--edad",
            edad,
            "--codigo",
            codigo,
        ],
        capture_output=True,
        text=True,
    )


# Función para ejecutar el comando binario sin el argumento de nombre
def exec_binary_not_nombre(path, apellido, edad, codigo):
    return subprocess.run(
        [path, "--apellido", apellido, "--edad", edad, "--codigo", codigo],
        capture_output=True,
        text=True,
    )


# Función para ejecutar el comando binario sin el argumento de apellido
def exec_binary_not_apellido(path, nombre, edad, codigo):
    return subprocess.run(
        [path, "--nombre", nombre, "--edad", edad, "--codigo", codigo],
        capture_output=True,
        text=True,
    )


# Función para ejecutar el comando binario sin los argumentos de nombre y apellido
def exec_binary_min(path, edad, codigo):
    return subprocess.run(
        [path, "--edad", edad, "--codigo", codigo], capture_output=True, text=True
    )


# Definimos funcion incompleta de autenticacion de dos pasos
def fa2_authenticate(user_info):
    return {}


# Definición de clase que realiza llamadas a un API externo
class APIClient:
    def __init__(self, base_url="https://test.net"):
        self.base_url = base_url

    def get_user_data(self, user_id):
        url = f"{self.base_url}/data/{user_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
