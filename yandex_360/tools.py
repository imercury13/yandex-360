"""Модуль вспомогательных функций"""

from . import ya360

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
    :return: ID группы
    :rtype: dict

    """

    url = 'perPage=10000'
    groups = ya360.show_groups(token, orgID, url)
    if check_request(groups):
        for group in groups['groups']:
            if group['label'] == sstr:
                return {'id':group['id']}
    else:
        return groups

def get_id_department_by_label(sstr, token, orgID):
    """Функция преобразования label подразделения в id

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param sstr: строка поиска
    :type sstr: str
    :return: ID подразделения
    :rtype: dict

    """

    url = 'perPage=1000'
    departments = ya360.show_departments(token, orgID, url)
    if check_request(departments):
        for department in departments['departments']:
            if department['label'] == sstr:
                return {'id':department['id']}
    else:
        return departments

def get_id_user_by_nickname(sstr, token, orgID):
    """Функция преобразования nickname пользователя в id

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param sstr: строка поиска
    :type sstr: str
    :return: ID пользователя
    :rtype: dict

    """

    url = 'perPage=10000'
    users = ya360.show_users(token, orgID, url)
    if check_request(users):
        for user in users['users']:
            if user['nickname'] == sstr:
                return {'id':user['id']}
    else:
        return users
