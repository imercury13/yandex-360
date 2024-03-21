"""Модуль вспомогательных функций"""

from . import users
from . import groups
from . import departments

def check_request(req):
    """Функция проверки ответа запроса

    :param req: результат запроса
    :type req: dict
    """

    if 'code' in req and 'message' in req: return False

    return True

def get_id_group_by_label(sstr, token, orgID):
    """Функция преобразования label группы в id

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param sstr: строка поиска
    :type sstr: str
    :return: ID группы: {'id': int}
    :rtype: dict

    """

    grps = groups.show_groups(token, orgID)
    if check_request(grps):
        while grps['page'] <= grps['pages']:
            for group in grps['groups']:
                if group['label'] == sstr:
                    return {'id':group['id']}
            grps = groups.show_groups(token, orgID, page=grps['page']+1)
    else:
        return grps

def get_id_department_by_label(sstr, token, orgID):
    """Функция преобразования label подразделения в id

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param sstr: строка поиска
    :type sstr: str
    :return: ID подразделения: {'id': int}
    :rtype: dict

    """

    dep = departments.show_departments(token, orgID)

    if check_request(dep):
        while dep['page'] <= dep['pages']:
            for department in dep['departments']:
                if department['label'] == sstr:
                    return {'id':department['id']}
            dep = departments.show_departments(token, orgID, page=dep['page']+1)
    else:
        return dep

def get_id_user_by_nickname(sstr, token, orgID):
    """Функция преобразования nickname пользователя в id

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param sstr: строка поиска
    :type sstr: str
    :return: ID пользователя {'id': str}
    :rtype: dict

    """
     
    usrs = users.show_users(token, orgID)

    if check_request(usrs):
        while usrs['page'] <= usrs['pages']:
            for user in usrs['users']:
                if user['nickname'] == sstr:
                    return {'id':user['id']}
            usrs = users.show_users(token, orgID, page=usrs['page']+1)
    else:
        return usrs

def get_groups(token, orgID):
    """Функция вывода всех групп
    
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: словарь групп
    :rtype: dict
    
    """

    lst_grp =[]

    grps = groups.show_groups(token, orgID)
    if check_request(grps):
        while grps['page'] <= grps['pages']:
            lst_grp.append(grps['groups'])
            grps = groups.show_groups(token, orgID, page=grps['page']+1)
        return {"groups":lst_grp,"page":grps['page'],"pages":grps['pages'],"perPage":grps['perPage'],"total":grps['total']}
    else:
        return grps

def get_departments(token, orgID):
    """Функция вывода всех подразделений
    
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: словарь подразделений
    :rtype: dict
    
    """

    lst_dep =[]

    deps = departments.show_departments(token, orgID)
    if check_request(deps):
        while deps['page'] <= deps['pages']:
            lst_dep.append(deps['departments'])
            deps = departments.show_departmets(token, orgID, page=deps['page']+1)
        return {"departments":lst_dep,"page":deps['page'],"pages":deps['pages'],"perPage":deps['perPage'],"total":deps['total']}
    else:
        return deps

def get_users(token, orgID):
    """Функция вывода всех пользователей
    
    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: словарь пользователей
    :rtype: dict
    
    """

    lst_usr =[]

    usrs = users.show_users(token, orgID)
    if check_request(usrs):
        while usrs['page'] <= usrs['pages']:
            lst_usr.append(users['users'])
            usrs = groups.show_users(token, orgID, page=usrs['page']+1)
        return {"users":lst_usr,"page":usrs['page'],"pages":usrs['pages'],"perPage":usrs['perPage'],"total":usrs['total']}
    else:
        return usrs