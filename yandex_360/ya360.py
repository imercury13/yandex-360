"""Модуль функций библиотеки"""

from jreq.jreq import safe_request
import json

def create_group(token, orgID, body):
    """Функция создания группы

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: тело запроса
    :type body: dict
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
    
    return safe_request('post', url, headers, json.dumps(body))

def update_group(token, orgID, body, ID):
	"""Функция обновления информации о группе
	
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: тело запроса
    :type body: dict
    :param ID: ID группы
    :type ID: str
    :return: результат запроса
    :rtype: dict

	"""

	url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'+ID+'/'
	headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

	return safe_request('patch', url, headers, json.dumps(body))

def delete_group(token, orgID, ID):
    """Функция удаления группы

    .. danger::
        **Данная операция необратима, восстановить данные будет невозможно!**
    
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param ID: ID группы
    :type ID: str
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'+ID+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def add_member_group(token, orgID, body, ID):
    """Функция добавления участника в группу

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: тело запроса
    :type body: dict
    :param ID: ID группы
    :type ID: str
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'+ID+'/members'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('post', url, headers, json.dumps(body))

def delete_member_group(token, orgID, ID, userType, userID):
    """Функция удаления участника из группы

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param ID: ID группы
    :type ID: str
    :param userType: тип участника
    :type userTupe: str
    :param userID: ID участника
    :type userID: str
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'+ID+'/members/'+userType+'/'+userID
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def show_group(token, orgID, ID):
    """Функция отображения информации о группе
	
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param ID: ID группы
    :type ID: str
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'+ID+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
    
    return safe_request('get', url, headers)

def show_members_group(token, orgID, ID):
    """Функция отображения членов группы
	
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param ID: ID группы
    :type ID: str
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'+ID+'/members/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
    
    return safe_request('get', url, headers)

def show_groups(token, orgID, url=None):
    """Функция вывода списка всех групп

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param url: :term:`Ключи разбивки на страницы`
    :type url: str or None
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/?'+url
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
	
    return safe_request('get', url, headers)

def create_department(token, orgID, body):
    """Функция создания подразделения

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: тело запроса
    :type body: dict
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/departments/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('post', url, headers, json.dumps(body))

def update_department(token, orgID, body, ID):
    """Функция обновления информации о подразделении

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: тело запроса
    :type body: dict
    :param ID: ID подразделения
    :type ID: str
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/departments/'+ID+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('patch', url, headers, json.dumps(body))

def delete_department(token, orgID, ID):
    """Функция удаления подразделения

    .. danger::
        **Данная операция необратима, восстановить данные будет невозможно!**

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param ID: ID подразделения
    :type ID: str
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/departments/'+ID+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
    
    return safe_request('delete', url, headers)

def add_alias_department(token, orgID, body, ID):
    """Функция добавления альяса подразделению

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: тело запроса
    :type body: dict
    :param ID: ID подразделения
    :type ID: str
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/departments/'+ID+'/aliases/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('post', url, headers, json.dumps(body))

def delete_alias_department(token, orgID, ID, alias):
    """Функция удаления альяса у подразделения

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param ID: ID подразделения
    :type ID: str
    :param alias: альяс
    :type alias: str
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/departments/'+ID+'/aliases/'+alias+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def show_department(token, orgID, ID):
    """Функция вывода информации о подразделении

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param ID: ID подраделения
    :type ID: str
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/departments/'+ID+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('get', url, headers)

def show_departments(token, orgID, url=None):
    """Функция вывода списка всех подразделений

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param url: :term:`Ключи разбивки на страницы`
    :type url: str or None
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/departments/?'+url
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('get', url, headers)

def show_users(token, orgID, url=None):
    """Функция вывода списка всех пользователей

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param url: :term:`Ключи разбивки на страницы`
    :type url: str or None
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/users/?'+url
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
	
    return safe_request('get', url, headers)

def show_user(token, orgID, ID):
    """Функция вывода информации о пользователе

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param ID: ID пользователя
    :type ID: str
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/users/'+ID+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('get', url, headers)

def update_user(token, orgID, body, ID):
    """Функция обновления информации о пользователе

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: тело запроса
    :type body: dict
    :param ID: ID пользователя
    :type ID: str
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/users/'+ID+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
	
    return safe_request('patch', url, headers, json.dumps(body))

def create_user(token, orgID, body):
    """Функция создания пользователя

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: тело запроса
    :type body: dict
    :return: результат запроса
    :rtype: dict
    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/users/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
	
    return safe_request('post', url, headers, json.dumps(body))

def delete_user(token, orgID, ID):
    """Функция удаления пользователя

    .. danger::
        **Данная операция необратима, восстановить данные будет невозможно!**

        Будут удалены все почтовые сообщения, а также папки и файлы на Яндекс Диске

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param ID: ID пользователя
    :type ID: str
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/users/'+ID
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def add_alias_user(token, orgID, ID, body):
    """Функция добавления альяса пользователю

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param ID: ID пользователя
    :type ID: str
    :param body: тело запроса
    :type body: dict
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/users/'+ID+'/aliases/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('post', url, headers, json.dumps(body))

def delete_alias_user(token, orgID, ID, alias):
    """Функция удаления альяса у пользователя

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param ID: ID пользователя
    :type ID: str
    :param alias: альяс
    :type alias: str
    :return: результат запроса
    :rtype: dict

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/users/'+ID+'/aliases/'+alias+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)
