"""Модуль функций  для работы с доменами. Просмотр, создание, изменение и удаление. Получение статуса подключения и настроек доменов.

.. note::
    **Права доступа для работы с доменами:**

    **directory:read_domains**  — просмотр;
    **directory:write_domains** — просмотр и изменение.


"""

from jreq.jreq import safe_request
import json

def add_domain (token, orgID, domain):
    """Функция используется, чтобы подключить новый домен.

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param domain: Полное имя домена
    :type domain: str
    :return: результат запроса
    :rtype: dict

    """

    body = {'domain':domain}
    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers, json.dumps(body))

def show_domains(token, orgID, url=None):
    """Функция возвращает список доменов организации с постраничной навигацией

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param url: :term:`Ключи разбивки на страницы`
    :type url: str or None
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains/?{url}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
	
    return safe_request('get', url, headers)

def add_domain (token, orgID, domain):
    """Функция позволяет удалить домен.
    
    .. note::
        Вы можете удалить любой домен, кроме технического.

    .. danger::
        **Данная операция необратима, восстановить данные будет невозможно!**

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param domain: Полное имя домена
    :type domain: str
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains{domain}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers)