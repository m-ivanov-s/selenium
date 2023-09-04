import pytest
import requests
import yaml

with open('config2.yaml') as f:
    data = yaml.safe_load(f)
    url = data['url']
    un = data['username']
    pw = data['password']


@pytest.fixture()
def login():
    obj_data = requests.post(url=url, data={'username': un, 'password': pw})
    token = {}
    if 'token' in obj_data.json():
        token = obj_data.json()['token']
    else:
        print(f'my_token = {obj_data.json()["error"]}')
    return token
