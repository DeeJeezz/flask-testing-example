from flask import Response


def test_index(client):
    response: Response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'<h3>Hello world</h3>'
