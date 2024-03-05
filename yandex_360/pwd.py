"""Модуль позволяет управлять параметрами паролей пользователей организации.

.. note::
    **Разрешения на использование сервиса, которые доступны при настройке приложения:**

    **ya360_security:domain_passwords_read** — чтение информации о параметрах паролей пользователей;
    **ya360_security:domain_passwords_write** — управление параметрами паролей пользователей.


"""

from jreq.jreq import safe_request
import json

def show_domain_passwords(token, orgID):
    """Функция позволяет просмотреть параметры парольной политики в организации:

    Наличие у пользователей возможности самостоятельно менять пароль;
    Наличие и длительность (в днях) срока действия пароля.


    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: :numref:`результат запроса %s <Результат запроса show_domain_passwords>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_domain_passwords
        :name: Результат запроса show_domain_passwords

        {
            "changeFrequency": int,
            "enabled": bool
        }

    """

    url = f'https://api360.yandex.net/security/v1/org/{orgID}/domain_passwords'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
	
    return safe_request('get', url, headers)

def edit_domain_passwords (token, orgID, body):
    """Функция позволяет управлять парольной политикой пользователей организации:

    разрешать или запрещать самостоятельную смену пароля;
    устанавливать периодичность смены пароля.


    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: :numref:`тело запроса %s <Тело запроса edit_domain_passwords>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса edit_domain_passwords>`
    :rtype: dict


    .. code-block:: python
        :caption: Тело запроса edit_domain_passwords
        :name: Тело запроса edit_domain_passwords

        {
            "changeFrequency": int,
            "enabled": bool
        }

    .. code-block:: python
        :caption: Результат запроса edit_domain_passwords
        :name: Результат запроса edit_domain_passwords

        {
            "changeFrequency": int,
            "enabled": bool
        }

    """

    url = f'https://api360.yandex.net/security/v1/org/{orgID}/domain_passwords'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('put',url, headers, json.dumps(body))