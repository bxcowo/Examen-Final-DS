import pytest
import src.code

@pytest.fixture(autouse=True)
def patch_src(monkeypatch):
    def mockpath():
        return "./tests/stubs/fake-analyzer.sh"
    monkeypatch.setattr(src.code, "get_binary", mockpath)

def test_happy_path(patch_src):
    results = src.code.exec_binary_full(path=src.code.get_binary(), nombre="Aaron", apellido="Flores", edad="19", codigo="20221346A")
    assert results.returncode == 0

def test_error_edad(patch_src):
    results = src.code.exec_binary_min(path=src.code.get_binary(), edad="", codigo="20221346A")
    assert results.returncode == 1

def test_menor_edad():
    results = src.code.exec_binary_min(path=src.code.get_binary(), edad="10", codigo="20221346A")
    assert results.returncode == 1

def test_error_codigo():
    results = src.code.exec_binary_min(path=src.code.get_binary(), edad="19", codigo="")
    assert results.returncode == 1

def test_default_nombre():
    results = src.code.exec_binary_not_nombre(path=src.code.get_binary(), apellido="Flores", edad="19", codigo="20221346A")
    assert results.returncode == 0

def test_default_apellido():
    results = src.code.exec_binary_not_apellido(path=src.code.get_binary(), nombre="Aaron", edad="19", codigo="20221346A")
    assert results.returncode == 0
