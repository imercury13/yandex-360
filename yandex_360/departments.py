"""Модуль функций для работы с подразделениями. Просмотр, создание, изменение и удаление.

.. note::
    **Права доступа для работы с подразделениями:**

    **directory:read_departments** — просмотр;
    **directory:write_departments** — просмотр и изменение.


"""

from jreq.jreq import safe_request
import json

def add_department(token, orgID, body):
    """Функция создания подразделения

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: :numref:`Тело запроса %s <Тело запроса add_department>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса add_department>`
    :rtype: dict

    .. code-block:: python
        :caption: Тело запроса add_department
        :name: Тело запроса add_department

        {
            "description": str,
            "externalId": str,
            "headId": str,
            "label": str,
            "name": str,
            "parentId": int
        }

    .. code-block:: python
        :caption: Результат запроса add_department
        :name: Результат запроса add_department

        {
            "aliases": [
                str
            ],
            "createdAt": str,
            "description": str,
            "email": str,
            "externalId": str,
            "headId": str,
            "id": integer,
            "label": str,
            "membersCount": int,
            "name": str,
            "parentId": int
        }

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/departments'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post', url, headers, json.dumps(body))

def update_department(token, orgID, depID, body):
    """Функция изменяет информацию о подразделении.
    
    .. note::
        Изменяются значения только тех параметров, которые были переданы в запросе.

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param depID: :term:`ID подразделения в Яндекс 360`
    :type depID: str
    :param body: :numref:`Тело запроса %s <Тело запроса update_department>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса update_department>`
    :rtype: dict

    .. code-block:: python
        :caption: Тело запроса update_department
        :name: Тело запроса update_department

        {
            "description": str,
            "externalId": str,
            "headId": str,
            "label": str,
            "name": str,
            "parentId": int
        }

    .. code-block:: python
        :caption: Результат запроса update_department
        :name: Результат запроса update_department

        {
            "aliases": [
                str
            ],
            "createdAt": str,
            "description": str,
            "email": str,
            "externalId": str,
            "headId": str,
            "id": integer,
            "label": str,
            "membersCount": int,
            "name": str,
            "parentId": int
        }

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/departments/{depID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('patch', url, headers, json.dumps(body))

def delete_department(token, orgID, depID):
    """Функция удаляет подразделение.
    
    .. note::
        Запрос может быть выполнен только для подразделения без сотрудников и вложенных подразделений

    .. danger::
        **Данная операция необратима, восстановить данные будет невозможно!**

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param depID: :term:`ID подразделения в Яндекс 360`
    :type depID: str
    :return: :numref:`результат запроса %s <Результат запроса delete_department>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса delete_department
        :name: Результат запроса delete_department

        {
            "id": int,
            "removed": bool
        }

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/departments/{depID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
    
    return safe_request('delete', url, headers)

def add_alias_department(token, orgID, depID, body):
    """Функция добавляет подразделению алиас почтовой рассылки.
    
    .. note::
        Запрос может быть выполнен только для подразделений, у которых уже указано основное имя почтовой рассылки в поле **label**

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param depID: :term:`ID подразделения в Яндекс 360`
    :type depID: str
    :param body: :numref:`Тело запроса %s <Тело запроса add_alias_department>`
    :type body: dict
    :return: :numref:`результат запроса %s <Результат запроса add_alias_department>`
    :rtype: dict

    .. code-block:: python
        :caption: Тело запроса add_alias_department
        :name: Тело запроса add_alias_department

        {
            "alias": str
        }

    .. code-block:: python
        :caption: Результат запроса add_alias_department
        :name: Результат запроса add_alias_department

        {
            "aliases": [
                str
            ],
            "createdAt": str,
            "description": str,
            "email": str,
            "externalId": str,
            "headId": str,
            "id": integer,
            "label": str,
            "membersCount": int,
            "name": str,
            "parentId": int
        }

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/departments/{depID}/aliases'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post', url, headers, json.dumps(body))

def delete_alias_department(token, orgID, depID, alias):
    """Функция удаляет алиас почтовой рассылки подразделения

    .. danger::
        **Данная операция необратима, восстановить данные будет невозможно!**

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param depID: :term:`ID подразделения в Яндекс 360`
    :type depID: str
    :param alias: альяс
    :type alias: str
    :return: :numref:`результат запроса %s <Результат запроса delete_alias_department>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса delete_alias_department
        :name: Результат запроса delete_alias_department

        {
            "alias": str,
            "removed": bool
        }

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/departments/{depID}/aliases/{alias}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def show_department(token, orgID, depID):
    """Функция возвращает информацию об одном подразделении

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param depID: :term:`ID подразделения в Яндекс 360`
    :type depID: str
    :return: :numref:`результат запроса %s <Результат запроса show_department>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_department
        :name: Результат запроса show_department

        {
            "aliases": [
                str
            ],
            "createdAt": str,
            "description": str,
            "email": str,
            "externalId": str,
            "headId": str,
            "id": integer,
            "label": str,
            "membersCount": int,
            "name": str,
            "parentId": int
        }

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/departments/{depID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get', url, headers)

def show_departments(token, orgID, page=1, perPage=100, parentId=None, orderBy='id'):
    """Функция возвращает список подразделений с постраничной навигацией

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param page: Номер страницы ответа. Значение по умолчанию — 1
    :type page: int
    :param perPage: Количество подраздлений на одной странице ответа. Значение по умолчанию — 100
    :type perPage: int
    :param parentId: Идентификатор родительского подразделения. Если не указан, то выводятся все подразделения организации
    :type parentId: str
    :param orderBy: Вид сортировки. Возможные значения: 'id' или 'name'
    :type orderBy: str
    :return: :numref:`результат запроса %s <Результат запроса show_departments>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_departments
        :name: Результат запроса show_departments

        {
            "departments": [
                {
                    "aliases": [
                        str
                    ],
                    "createdAt": str,
                    "description": str,
                    "email": str,
                    "externalId": str,
                    "headId": str,
                    "id": int,
                    "label": str,
                    "membersCount": int,
                    "name": str,
                    "parentId": int
                }
            ],
            "page": int,
            "pages": int,
            "perPage": int,
            "total": int
        }

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/departments/?page={page}&perPage={perPage}&orderBy={orderBy}'
    if parentId: url += f'&parentId={parentId}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get', url, headers)