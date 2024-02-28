"""Модуль функций для просмотра организаций пользователя
"""

from jreq.jreq import safe_request
import json

def show_orgs(token, orgID, url=None):
    """Функция возвращает список организаций пользователя

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param url: :term:`Ключи разбивки на страницы`
    :type url: str or None
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org?{url}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get', url, headers)