import pytest
import os
from flask import Flask

from app import create_app


@pytest.fixture
def app():
    app: Flask = create_app()
    app.config['TESTING'] = True

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def file_path():
    return 'test.txt'


@pytest.fixture
def create_file(file_path):
    with open(file_path, 'w') as f:
        f.write('HELLO WORLD')

    yield
    os.remove(file_path)
