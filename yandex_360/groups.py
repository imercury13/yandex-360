"""Модуль функций для работы с группами. Просмотр, создание, изменение и удаление.

.. note::
    **Права доступа для работы с группами:**

    **directory:read_groups** — просмотр;
    **directory:write_groups** — просмотр и изменение.


"""

from jreq.jreq import safe_request
import json

def add_group(token, orgID, body):
    """Функция создает новую группу. Пользователь, от имени которого выполняется запрос, не включается в состав группы

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: тело запроса
    :type body: dict
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/groups'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
    
    return safe_request('post', url, headers, json.dumps(body))

def update_group(token, orgID, groupID, body):
	"""Функция изменяет информацию о группе. Изменяются значения только тех параметров, которые были переданы в запросе.
	
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

	url = f'https://api360.yandex.net/directory/v1/org/{orgID}/groups/{groupID}'
	headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

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