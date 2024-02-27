"""Модуль функций для управления DNS записями домена

.. note::
    **Разрешения работы с DNS:**

    **directory:manage_dns** — управление DNS (чтение и запись).


"""

from jreq.jreq import safe_request
import json

def show_dns (token, orgID, domain, url=None):
    """Функция позволяет получить все DNS-записи, которые были установлены для домена

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param domain: :term:`Полное доменное имя`
    :type domain: str
    :param url: :term:`Ключи разбивки на страницы`
    :type url: str or None
    :return: результат запроса
    :rtype: dict
    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains/{domain}/dns?{url}'
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
    :param body: :term:`Тело запроса добавления записи DNS`
    :type body: dict
    :return: результат запроса
    :rtype: dict

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
    :param body: :term:`Тело запроса редактирования записи DNS`
    :type body: dict
    :return: результат запроса
    :rtype: dict
 
    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains/{domain}/dns/{recordID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers, json.dumps(body))