"""Модуль функций routing"""

from jreq.jreq import safe_request
import json

def show_routing(token, orgID):
    '''Функция вывода содержимого таблицы правил обработки почты
    
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: результат запроса
    :rtype: dict

    '''

    url = 'https://api360.yandex.net/admin/v1/mail/routing/org/'+orgID+'/rules'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('get', url, headers)

def edit_routing(token, orgID, body):
    '''Функция изменения содержимого таблицы правил обработки почты
    
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: тело запроса
    :type body: dict
    :return: результат запроса
    :rtype: dict

    '''

    url = 'https://api360.yandex.net/admin/v1/mail/routing/org/'+orgID+'/rules'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('put', url, headers, json.dumps(body))
    
