"""Модуль функций для управления DNS записями домена

.. note::
    **Разрешения работы с DNS:**

    **directory:manage_dns** — управление DNS (чтение и запись).


"""

from jreq.jreq import safe_request
import json

def show_dns (token, orgID, domain, page=1, perPage=50):
    """Функция позволяет получить все DNS-записи, которые были установлены для домена

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param domain: :term:`Полное доменное имя`
    :type domain: str
    :param page: Номер страницы ответа. Значение по умолчанию — 1
    :type page: int
    :param perPage: Количество записей на одной странице ответа. Значение по умолчанию — 50
    :type perPage: int
    :return: :numref:`результат запроса %s <Результат запроса show_dns>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_dns
        :name: Результат запроса show_dns

        {
            "page": int,
            "pages": int,
            "perPage": int,
            "records": [
                {
                    "address": str,
                    "exchange": str,
                    "flag": int,
                    "name": str,
                    "port": int,
                    "preference": int,
                    "priority": int,
                    "recordId": int,
                    "tag": str,
                    "target": str,
                    "text": str,
                    "ttl": int,
                    "type": str,
                    "value": str,
                    "weight": int
                }
            ],
            "total": int
        }

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains/{domain}/dns?page={page}&perPage={perPage}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get',url, headers)

def delete_dns (token, orgID, domain, recordID):
    """Функция позволяет удалить DNS-запись

    .. danger::
        **Данная операция необратима, восстановить данные будет невозможно!**

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param domain: :term:`Полное доменное имя`
    :type domain: str
    :param recordID: :term:`ID записи`
    :type recordID: int
    :return: результат запроса
    :rtype: dict
    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains/{domain}/dns/{recordID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('delete',url, headers)

def add_dns (token, orgID, domain, body):
    """Функция позволяет добавить DNS-запись

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param domain: :term:`Полное доменное имя`
    :type domain: str
    :param body: :numref:`тело запроса %s <Тело запроса add_dns>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса add_dns>`
    :rtype: dict

    .. code-block:: python
        :caption: Тело запроса add_dns
        :name: Тело запроса add_dns

        {
            "address": str,
            "exchange": str,
            "flag": int,
            "name": str,
            "port": int,
            "preference": int,
            "priority": int,
            "tag": str,
            "target": str,
            "text": str,
            "ttl": int,
            "type": str,
            "value": str,
            "weight": int
        }

    .. code-block:: python
        :caption: Результат запроса add_dns
        :name: Результат запроса add_dns

        {
            "address": str,
            "exchange": str,
            "flag": int,
            "name": str,
            "port": int,
            "preference": int,
            "priority": int,
            "tag": str,
            "target": str,
            "text": str,
            "ttl": int,
            "type": str,
            "value": str,
            "weight": int
        }

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains/{domain}/dns'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers, json.dumps(body))

def edit_dns (token, orgID, domain, recordID, body):
    """Функция позволяет добавить DNS-запись

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param domain: :term:`Полное доменное имя`
    :type domain: str
    :param recordID: :term:`ID записи`
    :type recordID: int
    :param body: :numref:`тело запроса %s <Тело запроса edit_dns>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса edit_dns>`
    :rtype: dict

    .. code-block:: python
        :caption: Тело запроса edit_dns
        :name: Тело запроса edit_dns

        {
            "address": str,
            "exchange": str,
            "name": str,
            "port": int,
            "preference": int,
            "priority": int,
            "target": str,
            "text": str,
            "ttl": int,
            "type": str,
            "weight": int
        }

    .. code-block:: python
        :caption: Результат запроса edit_dns
        :name: Результат запроса edit_dns

        {
            "address": str,
            "exchange": str,
            "flag": int,
            "name": str,
            "port": int,
            "preference": int,
            "priority": int,
            "tag": str,
            "target": str,
            "text": str,
            "ttl": int,
            "type": str,
            "value": str,
            "weight": int
        }
 
    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains/{domain}/dns/{recordID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers, json.dumps(body))