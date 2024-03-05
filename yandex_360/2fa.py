"""Модуль для управления обязательной двухфакторной аутентификацией (2FA) пользователей домена.

.. note::
    **Разрешения на использование сервиса, которые доступны при настройке приложения:**

    **ya360_security:domain_2fa_write** — управление обязательной 2FA для пользователей.


"""

from jreq.jreq import safe_request
import json

def show_domain_2fa(token, orgID):
    """Функция Возвращает статус обязательной двухфакторной аутентификации (2FA) для пользователей домена.

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: :numref:`результат запроса %s <Результат запроса show_domain_2fa>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_domain_2fa
        :name: Результат запроса show_domain_2fa

        {
            "duration": int,
            "enabled": bool,
            "enabledAt": str
        }

    """

    url = f'https://api360.yandex.net/security/v1/org/{orgID}/domain_2fa'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
	
    return safe_request('get', url, headers)

def enable_domain_2fa (token, orgID, body):
    """Функция включает обязательную двухфакторную аутентификацию (2FA) для пользователей домена.

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: :numref:`тело запроса %s <Тело запроса enable_domain_2fa>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса enable_domain_2fa>`
    :rtype: dict


    .. code-block:: python
        :caption: Тело запроса enable_domain_2fa
        :name: Тело запроса enable_domain_2fa

        {
            "duration": int,
            "logoutUsers": bool,
            "validationMethod": str
        }

    .. code-block:: python
        :caption: Результат запроса enable_domain_2fa
        :name: Результат запроса enable_domain_2fa

        {
            "duration": int,
            "enabled": bool,
            "enabledAt": str
        }

    """

    url = f'https://api360.yandex.net/security/v1/org/{orgID}/domain_2fa'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers, json.dumps(body))

def disable_domain_2fa (token, orgID, body):
    """Функция включает обязательную двухфакторную аутентификацию (2FA) для пользователей домена.

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: :numref:`результат запроса %s <Результат запроса disable_domain_2fa>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса disable_domain_2fa
        :name: Результат запроса disable_domain_2fa

        {
            "duration": int,
            "enabled": bool,
            "enabledAt": str
        }

    """

    url = f'https://api360.yandex.net/security/v1/org/{orgID}/domain_2fa'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('delete',url, headers)