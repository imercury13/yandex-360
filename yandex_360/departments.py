"""Модуль функций для работы с подразделениями. Просмотр, создание, изменение и удаление.

.. note::
    **Права доступа для работы с подразделениями:**

    **directory:read_departments** — просмотр;
    **directory:write_departments** — просмотр и изменение.


"""

from jreq.jreq import safe_request
import json

def add_department(token, orgID, body):
    """Функция создания подразделения

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: тело запроса
    :type body: dict
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/departments'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post', url, headers, json.dumps(body))

def update_department(token, orgID, depID, body):
    """Функция изменяет информацию о подразделении.
    
    .. note::
        Изменяются значения только тех параметров, которые были переданы в запросе.

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param depID: :term:`ID подразделения в Яндекс 360`
    :type depID: str
    :param body: тело запроса
    :type body: dict
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/departments/{depID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('patch', url, headers, json.dumps(body))

def delete_department(token, orgID, depID):
    """Функция удаляет подразделение.
    
    .. note::
        Запрос может быть выполнен только для подразделения без сотрудников и вложенных подразделений

    .. danger::
        **Данная операция необратима, восстановить данные будет невозможно!**

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param depID: :term:`ID подразделения в Яндекс 360`
    :type depID: str
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/departments/{depID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
    
    return safe_request('delete', url, headers)

def add_alias_department(token, orgID, depID, body):
    """Функция добавляет подразделению алиас почтовой рассылки.
    
    .. note::
        Запрос может быть выполнен только для подразделений, у которых уже указано основное имя почтовой рассылки в поле **label**

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param depID: :term:`ID подразделения в Яндекс 360`
    :type depID: str
    :param body: тело запроса
    :type body: dict
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/departments/{depID}/aliases'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post', url, headers, json.dumps(body))

def delete_alias_department(token, orgID, depID, alias):
    """Функция удаляет алиас почтовой рассылки подразделения

    .. danger::
        **Данная операция необратима, восстановить данные будет невозможно!**

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param depID: :term:`ID подразделения в Яндекс 360`
    :type depID: str
    :param alias: альяс
    :type alias: str
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/departments/{depID}/aliases/{alias}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def show_department(token, orgID, depID):
    """Функция возвращает информацию об одном подразделении

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param depID: :term:`ID подразделения в Яндекс 360`
    :type depID: str
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/departments/{depID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get', url, headers)

def show_departments(token, orgID, url=None):
    """Функция возвращает список подразделений с постраничной навигацией

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param url: :term:`Ключи разбивки на страницы`
    :type url: str or None
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/departments/?{url}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get', url, headers)