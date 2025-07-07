import subprocess

def get_binary():
    return "original path"

def exec_binary_full(path, nombre, apellido, edad, codigo):
    return subprocess.run([path, "--nombre", nombre, "--apellido", apellido, "--edad", edad, "--codigo", codigo], capture_output=True, text=True)

def exec_binary_not_nombre(path, apellido, edad, codigo):
    return subprocess.run([path, "--apellido", apellido, "--edad", edad, "--codigo", codigo], capture_output=True, text=True)

def exec_binary_not_apellido(path, nombre, edad, codigo):
    return subprocess.run([path, "--nombre", nombre, "--edad", edad, "--codigo", codigo], capture_output=True, text=True)

def exec_binary_min(path, edad, codigo):
    return subprocess.run([path, "--edad", edad, "--codigo", codigo], capture_output=True, text=True)
