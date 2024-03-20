"""Инструмент для управления потоком входящих писем на уровне домена. Управление подразумевает создание специальных правил обработки писем для сотрудников организации, выполняется Администратором и определяет настройки имеющие приоритет над пользовательскими.

.. note::
    **Разрешения на использование сервиса, которые доступны при настройке приложения:**

    **ya360_admin:mail_write_routing_rules** — просмотр и изменения;
    **ya360_admin:mail_read_routing_rules** — просмотр.

"""

from jreq.jreq import safe_request
import json

def show_routing(token, orgID):
    '''Функция вывода содержимого таблицы правил обработки почты
    
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: :numref:`результат запроса %s <Результат запроса show_routing>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_routing
        :name: Результат запроса show_routing

        {
            "rules": [
                {
                    "actions": [
                        {}
                    ],
                    "terminal": bool
                }
            ]
        }

    '''

    url = 'https://api360.yandex.net/admin/v1/org/'+orgID+'/mail/routing/rules'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('get', url, headers)

def edit_routing(token, orgID, body):
    '''Функция изменения содержимого таблицы правил обработки почты
    
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: :numref:`тело запроса %s <Тело запроса edit_routing>`
    :type body: dict
    :return: пустой словарь: {}
    :rtype: dict

    .. code-block:: python
        :caption: Тело запроса edit_routing
        :name: Тело запроса edit_routing

        {
            "rules": [
                {
                    "actions": [
                        {
                            "action": str,
                            "data": {
                                "email": str
                            }
                        }
                    ],
                    "terminal": bool
                }
            ]
        }

    '''

    url = 'https://api360.yandex.net/admin/v1/org/'+orgID+'/mail/routing/rules'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('put', url, headers, json.dumps(body))
    
