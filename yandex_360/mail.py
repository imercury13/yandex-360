"""Модуль функций для работы с настройками
почтовых ящиков сотрудников. Работает для пользователей,
аккаунты которых созданы на домене организации.

.. note::
    **Разрешения на использование сервиса, которые доступны при настройке приложения:**

    **ya360_admin:mail_read_user_settings** — чтение настроек почты пользователя;
    **ya360_admin:mail_write_user_settings** — управление настройками почты пользователя;
    **ya360_admin:mail_write_shared_mailbox_inventory** — управление правами доступа к почтовым ящикам;
    **ya360_admin:mail_read_shared_mailbox_inventory** — чтение информации о правах доступа к почтовым ящикам.


"""

import json
from jreq.jreq import safe_request


def show_sender_info (token, orgID, userID):
    """Функция позволяет просмотреть почтовый адрес, с которого отправляются письма по умолчанию, и настройки подписей сотрудника

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :return: :numref:`результат запроса %s <Результат запроса show_sender_info>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_sender_info
        :name: Результат запроса show_sender_info

        {
            "defaultFrom": str,
            "fromName": str,
            "signPosition": str,
            "signs": [
                {
                    "emails": [
                        str
                    ],
                    "isDefault": bool,
                    "lang": str,
                    "text": str
                }
            ]
        }

    """

    url = f'https://api360.yandex.net/admin/v1/org/{orgID}/mail/users/{userID}/settings/sender_info'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get',url, headers)

def edit_sender_info (token, orgID, userID, body):
    """Функция позволяет управлять почтовым адресом сотрудника, с которого отправляются письма по умолчанию, и настройками его подписей

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :param body: :numref:`Тело запроса %s <Тело запроса edit_sender_info>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса edit_sender_info>`
    :rtype: dict

    .. code-block:: python
        :caption: Тело запроса edit_sender_info
        :name: Тело запроса edit_sender_info

        {
            "defaultFrom": str,
            "fromName": str,
            "signPosition": str,
            "signs": [
                {
                    "emails": [
                        str
                    ],
                    "isDefault": bool,
                    "lang": str,
                    "text": str
                }
            ]
        }

    .. code-block:: python
        :caption: Результат запроса edit_sender_info
        :name: Результат запроса edit_sender_info

        {
            "defaultFrom": str,
            "fromName": str,
            "signPosition": str,
            "signs": [
                {
                    "emails": [
                        str
                    ],
                    "isDefault": bool,
                    "lang": str,
                    "text": str
                }
            ]
        }

    """

    url = f'https://api360.yandex.net/admin/v1/org/{orgID}/mail/users/{userID}/settings/sender_info'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers, json.dumps(body))

def show_user_rules (token, orgID, userID):
    """Функция позволяет просмотреть правила автоответа и пересылки писем

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :return: :numref:`результат запроса %s <Результат запроса show_user_rules>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_user_rules
        :name: Результат запроса show_user_rules

        {
            "autoreplies": [
                {
                    "ruleId": integer,
                    "ruleName": string,
                    "text": string
                }
            ],
            "forwards": [
                {
                    "address": string,
                    "ruleId": integer,
                    "ruleName": string,
                    "withStore": boolean
                }
            ]
        }

    """

    url = f'https://api360.yandex.net/admin/v1/org/{orgID}/mail/users/{userID}/settings/user_rules'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get',url, headers)

def edit_user_rules (token, orgID, userID, body):
    """Функция позволяет создать правило автоответа или пересылки писем для сотрудника.

    .. note::
        Возможность пересылки есть только на домены, которые принадлежат выбранной организации.
        Подтверждение получения пересылки при создании такого правила не требуется

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :param body: :numref:`Тело запроса %s <Тело запроса edit_user_rules>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса edit_user_rules>`
    :rtype: dict

    .. code-block:: python
        :caption: Тело запроса edit_user_rules
        :name: Тело запроса edit_user_rules

        {
            "autoreplies": [
                {
                    "ruleName": string,
                    "text": string
                }
            ],
            "forwards": [
                {
                    "address": string,
                    "ruleName": string,
                    "withStore": boolean
                }
            ]
        }

    .. code-block:: python
        :caption: Результат запроса edit_user_rules
        :name: Результат запроса edit_user_rules

        {
            "ruleId": int 
        }

    """

    url = f'https://api360.yandex.net/admin/v1/org/{orgID}/mail/users/{userID}/settings/user_rules'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers, json.dumps(body))

def delete_user_rules (token, orgID, userID, ruleID):
    """Функция удаляет конкретное правило автоответа или пересылки писем, настроенное для сотрудника

    .. danger::
        **Данная операция необратима, восстановить данные будет невозможно!**

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :param ruleID: :term:`ID правила`
    :type ruleID: int
    :return: результат запроса: {}
    :rtype: dict

    """

    url = f'https://api360.yandex.net/admin/v1/org/{orgID}/mail/users/{userID}/settings/user_rules/{ruleID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('delete',url, headers)

def show_address_book (token, orgID, userID):
    """Функция позволяет просмотреть, включено ли автоматическое формирование адресной книги сотрудника из адресов исходящей почты

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :return: :numref:`результат запроса %s <Результат запроса show_address_book>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_address_book
        :name: Результат запроса show_address_book

        {
            "collectAddresses": bool 
        }

    """

    url = f'https://api360.yandex.net/admin/v1/org/{orgID}/mail/users/{userID}/settings/address_book'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get',url, headers)

def edit_address_book (token, orgID, userID, body):
    """Функция позволяет управлять опцией автоматического формирования адресной книги сотрудника из адресов исходящей почты

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :param body: :numref:`Тело запроса %s <Тело запроса edit_address_book>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса edit_address_book>`
    :rtype: dict

    .. code-block:: python
        :caption: Тело запроса edit_address_book
        :name: Тело запроса edit_address_book

        {
            "collectAddresses": bool 
        }

    .. code-block:: python
        :caption: Результат запроса edit_address_book
        :name: Результат запроса edit_address_book

        {
            "collectAddresses": bool 
        }

    """

    url = f'https://api360.yandex.net/admin/v1/org/{orgID}/mail/users/{userID}/settings/address_book'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers, json.dumps(body))


def edit_access_mailbox (token, orgID, userID, touserID, body):
    """Функция предоставляет или изменяет права доступа сотрудника к чужому почтовому ящику.

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360` Идентификатор владельца почтового ящика, права доступа к которому необходимо предоставить или изменить
    :type userID: str
    :param touserID: :term:`ID пользователя в Яндекс 360` Идентификатор сотрудника, для которого настраивается доступ
    :type touserID: str
    :param body: :numref:`Тело запроса %s <Тело запроса edit_access_mailbox>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса edit_access_mailbox>`
    :rtype: dict

    .. code-block:: python
        :caption: Тело запроса edit_access_mailbox
        :name: Тело запроса edit_access_mailbox

        {
            "rights": [
                "str"
            ]
        }

    .. code-block:: python
        :caption: Результат запроса edit_access_mailbox
        :name: Результат запроса edit_access_mailbox

        {
            "taskId": str 
        }

    """

    url = f'https://api360.yandex.net/admin/v1/org/{orgID}/mail/delegated?resourceId={userID}&actorId={touserID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers, json.dumps(body))


def show_users_access_mailbox (token, orgID, userID):
    """Функция возвращает список сотрудников, у которых есть права доступа к почтовому ящику

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360` Идентификатор владельца почтового ящика, права доступа к которому необходимо проверить
    :type userID: str
    :return: :numref:`результат запроса %s <Результат запроса show_users_access_mailbox>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_users_access_mailbox
        :name: Результат запроса show_users_access_mailbox

        {
            "actors": [
                {
                    "actorId": str,
                    "rights": [
                        str
                    ]
                }
            ]
        }

    """

    url = f'https://api360.yandex.net/admin/v1/org/{orgID}/mail/delegated/{userID}/actors'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get',url, headers)


def show_access_mailbox_user (token, orgID, userID):
    """Функция возвращает список почтовых ящиков, к которым у сотрудника есть права доступа

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360` Идентификатор сотрудника, для которого запрашивается список доступных ящиков
    :type userID: str
    :return: :numref:`результат запроса %s <Результат запроса show_access_mailbox_user>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_access_mailbox_user
        :name: Результат запроса show_access_mailbox_user

        {
            "resources": [
                {
                    "resourceId": str,
                    "rights": [
                        str
                    ]
                }
            ]
        }

    """

    url = f'https://api360.yandex.net/admin/v1/org/{orgID}/mail/delegated/{userID}/resources'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get',url, headers)


def show_status_access_mailbox (token, orgID, taskID):
    """Функция возвращает статус задачи на управление правами доступа

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param taskID: Идентификатор задачи на управление правами доступа. Возвращается в ответе на запрос на изменение или на удаление прав доступа к почтовому ящику
    :type taskID: str
    :return: :numref:`результат запроса %s <Результат запроса show_access_mailbox_user>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_status_access_mailbox
        :name: Результат запроса show_status_access_mailbox

        {
            "status": str
        }

    """

    url = f'https://api360.yandex.net/admin/v1/org/{orgID}/mail/delegated/tasks/{taskID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get',url, headers)


def delete_access_mailbox (token, orgID, userID, touserID):
    """Функция удаляет все права доступа сотрудника к почтовому ящику

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360` Идентификатор владельца почтового ящика, права доступа к которому необходимо предоставить или изменить
    :type userID: str
    :param touserID: :term:`ID пользователя в Яндекс 360` Идентификатор сотрудника, для которого настраивается доступ
    :type touserID: str
    :return: :numref:`результат запроса %s <Результат запроса delete_access_mailbox>`
    :rtype: dict


    .. code-block:: python
        :caption: Результат запроса delete_access_mailbox
        :name: Результат запроса delete_access_mailbox

        {
            "taskId": str 
        }

    """

    url = f'https://api360.yandex.net/admin/v1/org/{orgID}/mail/delegated?resourceId={userID}&actorId={touserID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('delete',url, headers)
