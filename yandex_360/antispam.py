"""Модуль функций antispam"""

from jreq.jreq import safe_request
import json

def show_whitelist(token, orgID):
    '''Функция вывода содержимого белого списка
    
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: результат запроса
    :rtype: dict

    '''

    url = 'https://api360.yandex.net/admin/v1/org/'+orgID+'/mail/antispam/allowlist/ips'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('get', url, headers)

