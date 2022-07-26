"""Модуль функций библиотеки"""

from jreq.jreq import safe_request
import json

def create_group(token, orgID, body):
    """Функция создания группы

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
    
    return  safe_request('post', url, headers, json.dumps(body))

def update_group(token, orgID, body, ID):
	"""Функция обновления информации о группе
	
	"""

	url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'+ID+'/'
	headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

	return safe_request('patch', url, headers, json.dumps(body))

def delete_group(token, orgID, ID):
    """Функция удаления группы
    (необратимая операция)

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'+ID+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def add_member_group(token, orgID, body, ID):
    """Функция добавления участника в группу

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'+ID+'/members'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('post', url, headers, json.dumps(body))

def delete_member_group(token, orgID, ID, userType, userID):
    """Функция удаления участника из группы

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'+ID+'/members/'+userType+'/'+userID
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def show_group(token, orgID, ID):
    """Функция отображения информации о группе
	
    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'+ID+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
    
    return safe_request('get', url, headers)

def show_members_group(token, orgID, ID):
    """Функция отображения членов группы
	
    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'+ID+'/members/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
    
    return safe_request('get', url, headers)

def show_groups(token, orgID, url=None):
    """Функция вывода списка всех групп

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/?'+url
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
	
    return safe_request('get', url, headers)

def create_department(token, orgID, body):
    """Функция создания подразделения

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/departments/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('post', url, headers, json.dumps(body))

def update_department(token, orgID, body, ID):
    """Функция обновления информации о подразделении

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/departments/'+ID+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('patch', url, headers, json.dumps(body))

def delete_department(token, orgID, ID):
    """Функция удаления подразделения (необратимая операция)

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/departments/'+ID+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
    
    return safe_request('delete', url, headers)

def add_alias_department(token, orgID, body, ID):
    """Функция добавления альяса подразделению

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/departments/'+ID+'/aliases/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('post', url, headers, json.dumps(body))

def delete_alias_department(token, orgID, ID, alias):
    """Функция удаления альяса у подразделения

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/departments/'+ID+'/aliases/'+alias+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def show_department(token, orgID, ID):
    """Функция вывода информации о подразделении

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/departments/'+ID+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('get', url, headers)

def show_departments(token, orgID, url=None):
    """Функция вывода списка всех подразделений

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/departments/?'+url
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('get', url, headers)

def show_users(token, orgID, url=None):
    """Функция вывода списка всех пользователей

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/users/?'+url
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
	
    return safe_request('get', url, headers)

def show_user(token, orgID, ID):
    """Функция вывода информации о пользователе

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/users/'+ID+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('get', url, headers)

def update_user(token, orgID, body, ID):
    """Функция обновления информации о пользователе

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/users/'+ID+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
	
    return safe_request('patch', url, headers, json.dumps(body))

def create_user(token, orgID, body):
    """Функция создания пользователя

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/users/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
	
    return safe_request('post', url, headers, json.dumps(body))

def delete_user(token, orgID, ID):
    """Функция удаления пользователе (необратимая операция: будет удалено всё: почта, содержимое диска)

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/users/'+ID
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def add_alias_user(token, orgID, ID, alias):
    """Функция добавления альяса пользователю

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/users/'+ID+'/aliases/'+alias+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('post', url, headers)

def delete_alias_user(token, orgID, ID, alias):
    """Функция удаления альяса у пользователя

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/users/'+ID+'/aliases/'+alias+'/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)
