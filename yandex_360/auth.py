"""Модуль для управления временем жизни cookie сессий пользователей. Позволяет выйти из аккаунта пользователя на всех устройствах.

.. note::
    **Разрешения на использование сервиса, которые доступны при настройке приложения:**

    **ya360_security:domain_sessions_read** — чтение информации о времени жизни cookie сессий пользователей;
    **ya360_security:domain_sessions_write** — управление временем жизни cookie сессий пользователей и авторизацией.


"""

from jreq.jreq import safe_request
import json

def show_domain_sessions(token, orgID):
    """Функция возвращает время жизни cookie сессий пользователей организации.
    Значение по умолчанию — 0. Это значит, что время жизни cookie сессий не ограничено.

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: :numref:`результат запроса %s <Результат запроса show_domain_sessions>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_domain_sessions
        :name: Результат запроса show_domain_sessions

        {
            "authTTL": int
        }

    """

    url = f'https://api360.yandex.net/security/v1/org/{orgID}/domain_sessions'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
	
    return safe_request('get', url, headers)

def edit_domain_sessions (token, orgID, body):
    """Функция позволяет возможность поменять время жизни cookie сессий пользователей организации.

    .. warning::
        Ограничение. Чтобы выполнить запрос, приложению требуется разрешение на управление временем жизни cookie сессий пользователей и авторизацией.


    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: :numref:`тело запроса %s <Тело запроса edit_domain_sessions>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса edit_domain_sessions>`
    :rtype: dict


    .. code-block:: python
        :caption: Тело запроса edit_domain_sessions
        :name: Тело запроса edit_domain_sessions

        {
            "authTTL": int
        }

    .. code-block:: python
        :caption: Результат запроса edit_domain_sessions
        :name: Результат запроса edit_domain_sessions

        {
            "authTTL": int
        }

    """

    url = f'https://api360.yandex.net/security/v1/org/{orgID}/domain_sessions'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers, json.dumps(body))

def close_domain_sessions(token, orgID, userID):
    """Функция позволяет выйти из аккаунта определенного пользователя на всех устройствах, где произведен вход.

    .. danger::
        **Данная функция удаляет все пароли приложений!**

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :return: результат запроса: {}
    :rtype: dict



    """

    url = f'https://api360.yandex.net/security/v1/org/{orgID}/domain_sessions/users/{userID}/logout'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
	
    return safe_request('put', url, headers)