"""Модуль для работы с настройками антиспама.

.. note::
    **Разрешения на использование сервиса, которые доступны при настройке приложения:**

    **ya360_admin:mail_read_antispam_settings** — чтение настроек антиспама;
    **ya360_admin:mail_write_antispam_settings** — управление настройками антиспама (чтение и запись).


"""

from jreq.jreq import safe_request
import json

def show_whitelist(token, orgID):
    '''Функция вывода содержимого белого списка
    
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: :numref:`результат запроса %s <Результат запроса show_whitelist>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_whitelist
        :name: Результат запроса show_whitelist

        {
            "allowList": [
                str
            ]
        }

    '''

    url = 'https://api360.yandex.net/admin/v1/org/'+orgID+'/mail/antispam/allowlist/ips'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('get', url, headers)


def create_whitelist(token, orgID, body):
    '''Функция создания или замены содержимого белого списка
    
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: :numref:`тело запроса %s <Тело запроса create_whitelist>`
    :type body: dict
    :return: результат запроса: {}
    :rtype: dict

    .. code-block:: python
        :caption: Тело запроса create_whitelist
        :name: Тело запроса create_whitelist

        {
            "allowList": [
                str
            ]
        }

    '''

    url = 'https://api360.yandex.net/admin/v1/org/'+orgID+'/mail/antispam/allowlist/ips'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('post', url, headers, json.dumps(body))


def delete_whitelist(token, orgID):
    '''Функция удаления содержимого белого списка
    
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: результат запроса: {}
    :rtype: dict

    '''

    url = 'https://api360.yandex.net/admin/v1/org/'+orgID+'/mail/antispam/allowlist/ips'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

