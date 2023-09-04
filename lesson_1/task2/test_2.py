import requests
import yaml
import pytest
from conftest2 import login

with open('config2.yaml') as f:
    data = yaml.safe_load(f)
    url1 = data['url1']


def token_auth(token):
    response = requests.get(url=url1, headers={'X-Auth-Token': token}, params={'owner': 'notMe'})
    content_var = [item['content'] for item in response.json()['data']]
    return content_var
    # return response.json()['data'][0]['id']


def test_step2(login):
    assert 'content' in token_auth(login)
