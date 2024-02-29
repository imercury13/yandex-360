"""Модуль функций для работы с группами. Просмотр, создание, изменение и удаление.

.. note::
    **Права доступа для работы с группами:**

    **directory:read_groups** — просмотр;
    **directory:write_groups** — просмотр и изменение.


"""

from jreq.jreq import safe_request
import json

def add_group(token, orgID, body):
    """Функция создает новую группу.
    
    .. note::
        Пользователь, от имени которого выполняется запрос, не включается в состав группы

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
	"""Функция изменяет информацию о группе.
    
    .. note::
        Изменяются значения только тех параметров, которые были переданы в запросе.
	
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

def delete_group(token, orgID, groupID):
    """Функция удаляет группу.
    
    .. note::
        Участники, которые входили в группу, не удаляются

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

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/groups/{groupID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def add_member_group(token, orgID, groupID, body):
    """Функция добавляет участника в группу.
    
    .. note::
        Участником группы может быть сотрудник организации, отдельное подразделение или другая группа

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

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/groups/{groupID}/members'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post', url, headers, json.dumps(body))

def delete_member_group(token, orgID, groupID, memberType, memberID):
    """Функция удаляет конкретного участника из группы: сотрудника организации, подразделение или вложенную группу

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

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/groups/{groupID}/members/{memberType}/{memberID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def delete_all_members_group(token, orgID, groupID):
    """Функция удаляет из группы всех участников

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param ID: ID группы
    :type ID: str
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/groups/{groupID}/members'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def show_group(token, orgID, groupID):
    """Функция возвращает информацию об одной группе
	
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param ID: ID группы
    :type ID: str
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/groups/{groupID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
    
    return safe_request('get', url, headers)

def show_members_group(token, orgID, groupID):
    """Функция возвращает список участников группы, таких как сотрудники, подразделения или другие группы
	
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param ID: ID группы
    :type ID: str
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/groups/{groupID}/members/'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
    
    return safe_request('get', url, headers)

def show_groups(token, orgID, url=None):
    """Функция возвращает список групп с постраничной навигацией

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param url: :term:`Ключи разбивки на страницы`
    :type url: str or None
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/groups/?{url}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
	
    return safe_request('get', url, headers)

def update_admin_group(token, orgID, groupID, body):
	"""Функция назначает руководителей группы.
    
    .. warning::
        Руководителем группы может стать любой сотрудник организации. Изменяет сразу весь список руководителей
	
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

	url = f'https://api360.yandex.net/directory/v1/org/{orgID}/groups/{groupID}/admins'
	headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

	return safe_request('put', url, headers, json.dumps(body))

def delete_admins_group(token, orgID, groupID):
	"""Функция удаляет всех руководителей группы
	
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

	url = f'https://api360.yandex.net/directory/v1/org/{orgID}/groups/{groupID}/admins'
	headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

	return safe_request('delete', url, headers)