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
    :return: :numref:`результат запроса %s <Результат запроса add_domain>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса add_domain
        :name: Результат запроса add_domain

        {
            "country": str,
            "delegated": bool,
            "master": bool,
            "mx": bool,
            "name": str,
            "status": {
                "dkim": {
                    "match": bool,
                    "value": str
                },
                "lastAdded": str,
                "lastCheck": str,
                "mx": {
                    "match": bool,
                    "value": str
                },
                "name": str,
                "ns": {
                    "match": bool,
                    "value": str
                },
                "spf": {
                    "match": bool,
                    "value": str
                }
            },
            "verified": bool
        }

    """

    body = {'domain':domain}
    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers, json.dumps(body))

def show_domains(token, orgID, page=1, perPage=10):
    """Функция возвращает список доменов организации с постраничной навигацией

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param page: Номер страницы ответа. Значение по умолчанию — 1
    :type page: int
    :param perPage: Количество доменов на одной странице ответа. Значение по умолчанию — 10
    :type perPage: int
    :return: :numref:`результат запроса %s <Результат запроса show_domain>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_domain
        :name: Результат запроса show_domain

        {
            "domains": [
                {
                    "country": str,
                    "delegated": bool,
                    "master": bool,
                    "mx": bool,
                    "name": str,
                    "status": {
                        "dkim": {
                            "match": bool,
                            "value": str
                        },
                        "lastAdded": str,
                        "lastCheck": str,
                        "mx": {
                            "match": bool,
                            "value": str
                        },
                        "name": str,
                        "ns": {
                            "match": bool,
                            "value": str
                        },
                        "spf": {
                            "match": bool,
                            "value": str
                        }
                    },
                    "verified": bool
                }
            ],
            "page": int,
            "pages": int,
            "perPage": int,
            "total": int
        }

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains/?page={page}&perPage={perPage}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
	
    return safe_request('get', url, headers)

def delete_domain (token, orgID, domain):
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
    :return: http код
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains{domain}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('delete',url, headers)

def status_domain (token, orgID, domain):
    """Проверяет статус подключения домена.

    .. note::
        Запрос позволяет получить результат последней проверки, дату и время ее выполнения, а также дату и время следующей проверки.

        **Для кириллических доменов (например домен.рф) используйте кодировку Punycode.**

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param domain: Полное имя домена
    :type domain: str
    :return: :numref:`результат запроса %s <Результат запроса status_domain>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса status_domain
        :name: Результат запроса status_domain

        {
            "methods": [
                {
                    "code": str,
                    "method": str
                }
            ],
            "status": str
        }

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains/{domain}/status'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get',url, headers)

def enable_domain_dkim (token, orgID, domain):
    """Включить DKIM подпись для домена

    .. note::
        **Для кириллических доменов (например домен.рф) используйте кодировку Punycode.**

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param domain: Полное имя домена
    :type domain: str
    :return: http код
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains/{domain}/dkim/enable'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers)

def disable_domain_dkim (token, orgID, domain):
    """Выключить DKIM подпись для домена

    .. note::
        **Для кириллических доменов (например домен.рф) используйте кодировку Punycode.**

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param domain: Полное имя домена
    :type domain: str
    :return: http код
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains/{domain}/dkim/disable'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers)

def status_domain_dkim (token, orgID, domain):
    """Получить статус DKIM подпись для домена

    .. note::
        **Для кириллических доменов (например домен.рф) используйте кодировку Punycode.**

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param domain: Полное имя домена
    :type domain: str
    :return: :numref:`результат запроса %s <Результат запроса status_domain_dkim>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса status_domain_dkim
        :name: Результат запроса status_domain_dkim

        {
            "enabled": bool,
            "publicKey": str
        }

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/domains/{domain}/dkim/disable'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers)