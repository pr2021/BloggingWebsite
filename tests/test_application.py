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
    return "The Website Works Completely Fine"
    
   
