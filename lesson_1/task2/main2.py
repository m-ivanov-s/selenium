# Написать тест с использованием pytest и requests, в котором:
#
# Адрес сайта, имя пользователя и пароль хранятся в config.yaml
#
# conftest2.py содержит фикстуру авторизации по адресу https://test-stand.gb.ru/gateway/login
# с передачей параметров “username" и "password" и возвращающей токен авторизации
#
# Тест с использованием DDT проверяет наличие поста
# с определенным заголовком в списке постов другого пользователя,
# для этого выполняется get запрос по адресу https://test-stand.gb.ru/api/posts c хедером,
# содержащим токен авторизации в параметре "X-Auth-Token".
# Для отображения постов другого пользователя передается "owner": "notMe".
#
# http://restapi.adequateshop.com/api/authaccount/registration
#
# http://restapi.adequateshop.com/api/authaccount/login


import requests
import yaml

with open('config2.yaml') as f:
    data = yaml.safe_load(f)

    un = data['username']
    pw = data['password']
    url = data['url']
    url1 = data['url1']

# def login(username, password):
#     obj_data = requests.post(url=url, data={'username': username, 'password': password})
#     token = obj_data.json()['token']
#     return token


# print(obj_data.json())

def token_auth(token):
    response = requests.get(url=url1, headers={'X-Auth-Token': token}, params={'owner': 'notMe'})
    content_var = [item['content'] for item in response.json()['data']]
    return content_var
    # return response.json()['data']
    # return response.json()['data'][0]['id']

def test_step2(login):
    assert 'content' in token_auth(login)

# if __name__ == '__main__':
    # print(token_auth(login(un, pw)))
    # print(login())
