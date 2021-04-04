import json
import pytest
import os
import sys
print(os.getcwd())
print(sys.path)
sys.path.append(os.path.join(os.getcwd(),'helloworld'))
from helloworld.application import app


@pytest.fixture
def client():
    return app.test_client()


def test_response(client):
    result = client.get()
    response_body = json.loads(result.get_data())
    assert result.status_code == 200
    assert result.headers['Content-Type'] == 'application/json'
    assert response_body['Output'] == 'Hello World'
    
   
