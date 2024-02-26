"""Модуль функций mail (26.02.2024)
для работы с настройками почтовых ящиков сотрудников. Работает для пользователей, аккаунты которых созданы на домене организации.

Разрешения на использование сервиса, которые доступны при настройке приложения:

ya360_admin:mail_read_user_settings — чтение настроек почты пользователя;
ya360_admin:mail_write_user_settings — управление настройками почты пользователя.
"""

from jreq.jreq import safe_request
import json

def show_sender_info (token, orgID, userID):
    """Функция позволяет просмотреть почтовый адрес, с которого отправляются письма по умолчанию, и настройки подписей сотрудника

    :return: результат запроса
    :rtype: dict
    """

    url = f'https://api360.yandex.net/admin/v1/org/{orgID}/mail/users/{userID}/settings/sender_info'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get',url, headers)

def edit_sender_info (token, orgID, userID, body):
    """Функция позволяет управлять почтовым адресом сотрудника, с которого отправляются письма по умолчанию, и настройками его подписей

    :return: результат запроса
    :rtype: dict
    """

    url = f'https://api360.yandex.net/admin/v1/org/{orgID}/mail/users/{userID}/settings/sender_info'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post',url, headers, json.dumps(body))