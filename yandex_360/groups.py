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
    :param body: :numref:`Тело запроса %s <Тело запроса add_group>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса add_group>`
    :rtype: dict

    .. code-block:: python
        :caption: Тело запроса add_group
        :name: Тело запроса add_group

        {
            "adminIds": [
                str
            ],
            "description": str,
            "externalId": str,
            "label": str,
            "members": [
                {
                    "id": str,
                    "type": str
                }
            ],
            "name": str
        }

    .. code-block:: python
        :caption: Результат запроса add_group
        :name: Результат запроса add_group

        {
            "adminIds": [
                str
            ],
            "aliases": [
                str
            ],
            "authorId": str,
            "createdAt": str,
            "description": str,
            "email": str,
            "externalId": str,
            "id": int,
            "label": str,
            "memberOf": [
                int
            ],
            "members": [
                {
                    "id": str,
                    "type": str
                }
            ],
            "membersCount": int,
            "name": str,
            "removed": bool,
            "type": str
        }

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
    :param ID: ID группы
    :type ID: str
    :param body: :numref:`Тело запроса %s <Тело запроса update_group>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса update_group>`
    :rtype: dict

    .. code-block:: python
        :caption: Тело запроса update_group
        :name: Тело запроса update_group

        {
            "adminIds": [
                str
            ],
            "description": str,
            "externalId": str,
            "label": str,
            "members": [
                {
                    "id": str,
                    "type": str
                }
            ],
            "name": str
        }

    .. code-block:: python
        :caption: Результат запроса update_group
        :name: Результат запроса update_group

        {
            "adminIds": [
                str
            ],
            "aliases": [
                str
            ],
            "authorId": str,
            "createdAt": str,
            "description": str,
            "email": str,
            "externalId": str,
            "id": int,
            "label": str,
            "memberOf": [
                int
            ],
            "members": [
                {
                    "id": str,
                    "type": str
                }
            ],
            "membersCount": int,
            "name": str,
            "removed": bool,
            "type": str
        }

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
    :return: :numref:`результат запроса %s <Результат запроса delete_group>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса delete_group
        :name: Результат запроса delete_group

        {
            "id": int,
            "removed": bool
        }

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
    :param ID: ID группы
    :type ID: str
    :param body: :numref:`Тело запроса %s <Тело запроса add_member_group>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса add_member_group>`
    :rtype: dict

    .. code-block:: python
        :caption: Тело запроса add_member_group
        :name: Тело запроса add_member_group

        {
            "id": str,
            "type": str
        }

    .. code-block:: python
        :caption: Результат запроса add_member_group
        :name: Результат запроса add_member_group

        {
            "added": bool,
            "id": str,
            "type": str
        }

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
    :return: :numref:`результат запроса %s <Результат запроса delete_member_group>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса delete_member_group
        :name: Результат запроса delete_member_group

        {
            "deleted": bool,
            "id": str,
            "type": str
        }

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
    :return: :numref:`результат запроса %s <Результат запроса delete_all_members_group>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса delete_all_members_group
        :name: Результат запроса delete_all_members_group

        {
            "departments": [
                {
                    "id": int,
                    "membersCount": int,
                    "name": str
                }
            ],
            "groups": [
                {
                    "id": int,
                    "membersCount": int,
                    "name": str
                }
            ],
            "users": [
                {
                    "avatarId": str,
                    "departmentId": int,
                    "email": str,
                    "gender": str,
                    "id": str,
                    "name": {
                        "first": str,
                        "last": str,
                        "middle": str
                    },
                    "nickname": str,
                    "position": str
                }
            ]
        }

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
    :return: :numref:`результат запроса %s <Результат запроса show_group>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_group
        :name: Результат запроса show_group

        {
            "adminIds": [
                str
            ],
            "aliases": [
                str
            ],
            "authorId": str,
            "createdAt": str,
            "description": str,
            "email": str,
            "externalId": str,
            "id": int,
            "label": str,
            "memberOf": [
                int
            ],
            "members": [
                {
                    "id": str,
                    "type": str
                }
            ],
            "membersCount": int,
            "name": str,
            "removed": bool,
            "type": str
        }

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
    :return: :numref:`результат запроса %s <Результат запроса show_members_group>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_members_group
        :name: Результат запроса show_members_group

        {
            "departments": [
                {
                    "id": int,
                    "membersCount": int,
                    "name": str
                }
            ],
            "groups": [
                {
                    "id": int,
                    "membersCount": int,
                    "name": str
                }
            ],
            "users": [
                {
                    "avatarId": str,
                    "departmentId": int,
                    "email": str,
                    "gender": str,
                    "id": str,
                    "name": {
                        "first": str,
                        "last": str,
                        "middle": str
                    },
                    "nickname": str,
                    "position": str
                }
            ]
        }

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/groups/{groupID}/members/'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
    
    return safe_request('get', url, headers)

def show_groups(token, orgID, page=1,perPage=10):
    """Функция возвращает список групп с постраничной навигацией

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param page: Номер страницы ответа. Значение по умолчанию — 1
    :type page: int
    :param perPage: Количество групп на одной странице ответа. Значение по умолчанию — 10
    :type perPage: int
    :return: :numref:`результат запроса %s <Результат запроса show_groups>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_groups
        :name: Результат запроса show_groups

        {
            "groups": [
                {
                    "adminIds": [
                        str
                    ],
                    "aliases": [
                        str
                    ],
                    "authorId": str,
                    "createdAt": str,
                    "description": str,
                    "email": str,
                    "externalId": str,
                    "id": int,
                    "label": str,
                    "memberOf": [
                        int
                    ],
                    "members": [
                        {
                            "id": str,
                            "type": str
                        }
                    ],
                    "membersCount": int,
                    "name": str,
                    "removed": bool,
                    "type": str
                }
            ],
            "page": int,
            "pages": int,
            "perPage": int,
            "total": int
        }

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/groups/?page={page}&perPage={perPage}'
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
    :param ID: ID группы
    :type ID: str
    :param body: :numref:`Тело запроса %s <Тело запроса update_admin_group>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса update_admin_group>`
    :rtype: dict

    .. code-block:: python
        :caption: Тело запроса update_admin_group
        :name: Тело запроса update_admin_group

        {
            "adminIds": [
                "str"
            ]
        }

    .. code-block:: python
        :caption: Результат запроса update_admin_group
        :name: Результат запроса update_admin_group

        {
            "adminIds": [
                str
            ],
            "aliases": [
                str
            ],
            "authorId": str,
            "createdAt": str,
            "description": str,
            "email": str,
            "externalId": str,
            "id": int,
            "label": str,
            "memberOf": [
                int
            ],
            "members": [
                {
                    "id": str,
                    "type": str
                }
            ],
            "membersCount": int,
            "name": str,
            "removed": bool,
            "type": str
        }

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
    :return: :numref:`результат запроса %s <Результат запроса delete_admins_group>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса delete_admins_group
        :name: Результат запроса delete_admins_group

        {
            "adminIds": [
                str
            ],
            "aliases": [
                str
            ],
            "authorId": str,
            "createdAt": str,
            "description": str,
            "email": str,
            "externalId": str,
            "id": int,
            "label": str,
            "memberOf": [
                int
            ],
            "members": [
                {
                    "id": str,
                    "type": str
                }
            ],
            "membersCount": int,
            "name": str,
            "removed": bool,
            "type": str
        }

	"""

	url = f'https://api360.yandex.net/directory/v1/org/{orgID}/groups/{groupID}/admins'
	headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

	return safe_request('delete', url, headers)