import json
import pytest
from helloworld.application import app as application


@pytest.fixture
def client():
    return application.test_client()


def test_response(client):
    return "The Website Works"
    
   
