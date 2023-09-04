# С использованием фреймворка pytest написать тест операции
# checkText SOAP API https://speller.yandex.net/services/spellservice?WSDL
#
# Тест должен использовать DDT и проверять наличие определенного
# верного слова в списке предложенных исправлений к определенному неверному слову.
#
# Слова должны быть заданы через фикстуры в conftest2.py,
# адрес wsdl должен быть вынесен в config.yaml.
#
# Методы работы с SOAP должны быть вынесены в отдельную библиотеку.


from zeep import Client, Settings
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)
    wsdl = data['wsdl']

settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings=settings)


def check_words(word):
    box = client.service.checkText(word)
    if box:
        # print(box)
        return box[0]['s']


    # output
    # [{
    #     'word': 'НИВЕРНО',
    #     's': [
    #         'НЕВЕРНО'
    #     ],
    #     'code': 1,
    #     'pos': 0,
    #     'row': 0,
    #     'col': 0,
    #     'len': 7
    # }]

    # print(box[0]['s'])
    # output
    # ['НЕВЕРНО']


if __name__ == '__main__':
    check_words("НИВЕРНО")
