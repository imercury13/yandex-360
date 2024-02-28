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
    :type body: dict
    :return: результат запроса
    :rtype: dict

    """

    body = {'domain':domain}
    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers, json.dumps(body))