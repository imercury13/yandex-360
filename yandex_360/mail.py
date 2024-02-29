"""Модуль функций для работы с настройками
почтовых ящиков сотрудников. Работает для пользователей,
аккаунты которых созданы на домене организации.

.. note::
    **Разрешения на использование сервиса, которые доступны при настройке приложения:**

    **ya360_admin:mail_read_user_settings** — чтение настроек почты пользователя;
    **ya360_admin:mail_write_user_settings** — управление настройками почты пользователя.


"""

from jreq.jreq import safe_request
import json

def show_sender_info (token, orgID, userID):
    """Функция позволяет просмотреть почтовый адрес, с которого отправляются письма по умолчанию, и настройки подписей сотрудника

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :return: результат запроса
    :rtype: dict
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
    :param body: :term:`Тело запроса редактирования основного адреса и подписи`
    :type body: dict
    :return: результат запроса
    :rtype: dict
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
    :return: результат запроса
    :rtype: dict
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
    :param body: :term:`Тело запроса добавления правила автоответа или пересылки`
    :type body: dict
    :return: результат запроса
    :rtype: dict
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
    :return: результат запроса
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
    :return: результат запроса
    :rtype: dict
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
    :param body: :term:`Тело запроса автоматического сбора контактов`
    :type body: dict
    :return: результат запроса
    :rtype: dict
    """

    url = f'https://api360.yandex.net/admin/v1/org/{orgID}/mail/users/{userID}/settings/address_book'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers, json.dumps(body))