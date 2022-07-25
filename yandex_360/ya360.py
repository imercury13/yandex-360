"""Модуль функций библиотеки"""

from wsgiref import headers
from jreq.jreq import safe_request

def create_group(token, orgID, body):
    """Функция создания группы

    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
    
    return  safe_request('post', url, headers, body)

def update_group(token, orgID, body, ID):
	"""Функция обновления информации о группе
	
	"""

	url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'+ID+'/'
	headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}

	return safe_request('patch', url, headers, body)

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

    return safe_request('post', url, headers, body)

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

