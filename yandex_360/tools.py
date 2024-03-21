"""Модуль вспомогательных функций"""

from . import users, groups, departments, domains, dns, org, logs

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
    """Функция возвращает список групп

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: :numref:`результат запроса %s <Результат запроса get_groups>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса get_groups
        :name: Результат запроса get_groups

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

    lst_grp =[]

    grps = groups.show_groups(token, orgID)
    if check_request(grps):
        while grps['page'] <= grps['pages']:
            lst_grp += grps['groups']
            grps = groups.show_groups(token, orgID, page=grps['page']+1)
        return {"groups":lst_grp,"page":grps['page'],"pages":grps['pages'],"perPage":grps['perPage'],"total":grps['total']}
    else:
        return grps

def get_departments(token, orgID):
    """Функция возвращает список подразделений

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: :numref:`результат запроса %s <Результат запроса get_departments>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса get_departments
        :name: Результат запроса get_departments

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

    lst_dep =[]

    deps = departments.show_departments(token, orgID)
    if check_request(deps):
        while deps['page'] <= deps['pages']:
            lst_dep += deps['departments']
            deps = departments.show_departments(token, orgID, page=deps['page']+1)
        return {"departments":lst_dep,"page":deps['page'],"pages":deps['pages'],"perPage":deps['perPage'],"total":deps['total']}
    else:
        return deps

def get_users(token, orgID):
    """Функция Возвращает список сотрудников

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: :numref:`результат запроса %s <Результат запроса get_users>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса get_users
        :name: Результат запроса get_users

        {
            "page": int,
            "pages": int,
            "perPage": int,
            "total": int,
            "users": [
                {
                    "about": str,
                    "aliases": [
                        str
                    ],
                    "avatarId": str,
                    "birthday": str,
                    "contacts": [
                        {
                            "alias": bool,
                            "label": str,
                            "main": bool,
                            "synthetic": bool,
                            "type": str,
                            "value": str
                        }
                    ],
                    "createdAt": str,
                    "departmentId": int,
                    "displayName": str,
                    "email": str,
                    "externalId": str,
                    "gender": str,
                    "groups": [
                        int
                    ],
                    "id": str,
                    "isAdmin": bool,
                    "isDismissed": bool,
                    "isEnabled": bool,
                    "isRobot": bool,
                    "language": str,
                    "name": {
                        "first": str,
                        "last": str,
                        "middle": str
                    },
                    "nickname": str,
                    "position": str,
                    "timezone": str,
                    "updatedAt": str
                }
            ]
        }

    """

    lst_usr =[]

    usrs = users.show_users(token, orgID)
    if check_request(usrs):
        while usrs['page'] <= usrs['pages']:
            lst_usr += usrs['users']
            usrs = users.show_users(token, orgID, page=usrs['page']+1)
        return {"users":lst_usr,"page":usrs['page'],"pages":usrs['pages'],"perPage":usrs['perPage'],"total":usrs['total']}
    else:
        return usrs

def get_domains(token, orgID):
    """Функция возвращает список доменов организации

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :return: :numref:`результат запроса %s <Результат запроса get_domain>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса get_domain
        :name: Результат запроса get_domain

        {
            "domains": [
                {
                    "country": str,
                    "delegated": bool,
                    "master": bool,
                    "mx": bool,
                    "name": str,
                    "status": {
                        "dkim": {
                            "match": bool,
                            "value": str
                        },
                        "lastAdded": str,
                        "lastCheck": str,
                        "mx": {
                            "match": bool,
                            "value": str
                        },
                        "name": str,
                        "ns": {
                            "match": bool,
                            "value": str
                        },
                        "spf": {
                            "match": bool,
                            "value": str
                        }
                    },
                    "verified": bool
                }
            ],
            "page": int,
            "pages": int,
            "perPage": int,
            "total": int
        }

    """

    lst_dom =[]

    doms = domains.show_domains(token, orgID)
    if check_request(doms):
        while doms['page'] <= doms['pages']:
            lst_dom += doms['domains']
            doms = domains.show_domains(token, orgID, page=doms['page']+1)
        return {"domains":lst_dom,"page":doms['page'],"pages":doms['pages'],"perPage":doms['perPage'],"total":doms['total']}
    else:
        return doms

def get_dns(token, orgID, domain):
    """Функция позволяет получить все DNS-записи, которые были установлены для домена

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param domain: :term:`Полное доменное имя`
    :type domain: str
    :return: :numref:`результат запроса %s <Результат запроса get_dns>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса get_dns
        :name: Результат запроса get_dns

        {
            "page": int,
            "pages": int,
            "perPage": int,
            "records": [
                {
                    "address": str,
                    "exchange": str,
                    "flag": int,
                    "name": str,
                    "port": int,
                    "preference": int,
                    "priority": int,
                    "recordId": int,
                    "tag": str,
                    "target": str,
                    "text": str,
                    "ttl": int,
                    "type": str,
                    "value": str,
                    "weight": int
                }
            ],
            "total": int
        }

    """

    lst_dnss =[]

    dnss = dns.show_dns(token, orgID, domain)
    if check_request(dnss):
        while dnss['page'] <= dnss['pages']:
            lst_dnss += dnss['records']
            dnss = dns.show_dns(token, orgID, domain, page=usrs['page']+1)
        return {"records":lst_dnss,"page":dnss['page'],"pages":dnss['pages'],"perPage":dnss['perPage'],"total":dnss['total']}
    else:
        return dnss

def get_orgs(token, orgID):
    """Функция возвращает список организаций пользователя

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :return: :numref:`результат запроса %s <Результат запроса get_orgs>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса get_orgs
        :name: Результат запроса get_orgs

        {
            "nextPageToken": str,
            "organizations": [
                {
                    "email": str,
                    "fax": str,
                    "id": int,
                    "language": str,
                    "name": str,
                    "phone": str,
                    "subscriptionPlan": str
                }
            ]
        }

    """

    lst_orgs =[]

    orgs = org.show_orgs(token, orgID)
    if check_request(orgs):
        lst_orgs += orgs['organizations']
        orgs = org.show_orgs(token, orgID, pageToken=orgs['nextPageToken'])
        while orgs['nextPageToken'] != '':
            lst_orgs += orgs['organizations']
            orgs = org.show_orgs(token, orgID, pageToken=orgs['nextPageToken'])
        return {"organizations":lst_orgs,"nextPageToken":orgs['nextPageToken']}
    else:
        return orgs

def get_disk_log(token, orgID, beforeDate=None, afterDate=None, includeUids=None, excludeUids=None):
    """Функция возвращает список событий в аудит-логе Диска организации.

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param beforeDate: Верхняя граница периода выборки в формате ISO 8601
    :type beforeDate: str
    :param afterDate: Нижняя граница периода выборки в формате ISO 8601
    :type afterDate: str
    :param includeUids: Список пользователей, действия которых должны быть включены в список событий
    :type includeUids: str
    :param excludeUids: Список пользователей, действия которых должны быть исключены из списка событий
    :type excludeUids: str
    :return: :numref:`результат запроса %s <Результат запроса get_disk_log>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса get_disk_log
        :name: Результат запроса get_disk_log

        {
            "events": [
                {
                    "clientIp": str,
                    "date": str,
                    "eventType": str,
                    "lastModificationDate": str,
                    "orgId": int,
                    "ownerLogin": str,
                    "ownerName": str,
                    "ownerUid": str,
                    "path": str,
                    "requestId": str,
                    "resourceFileId": str,
                    "rights": str,
                    "size": str,
                    "uniqId": str,
                    "userLogin": str,
                    "userName": str,
                    "userUid": str
                }
            ],
            "nextPageToken": str
        }

    """

    lst_disk =[]

    disk = logs.disk_log(token, orgID, beforeDate=beforeDate, afterDate=afterDate, includeUids=includeUids, excludeUids=excludeUids)
    if check_request(disk):
        lst_disk += disk['events']
        disk = logs.disk_log(token, orgID, pageToken=disk['nextPageToken'], beforeDate=beforeDate, afterDate=afterDate, includeUids=includeUids, excludeUids=excludeUids)
        while disk['nextPageToken'] != '':
            lst_disk += disk['events']
            disk = logs.disk_log(token, orgID, pageToken=disk['nextPageToken'], beforeDate=beforeDate, afterDate=afterDate, includeUids=includeUids, excludeUids=excludeUids)
        return {"events":lst_disk,"nextPageToken":disk['nextPageToken']}
    else:
        return disk

def get_mail_log(token, orgID, beforeDate=None, afterDate=None, includeUids=None, excludeUids=None, types=None):
    """Функция возвращает список событий в аудит-логе Почте организации.

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param beforeDate: Верхняя граница периода выборки в формате ISO 8601
    :type beforeDate: str
    :param afterDate: Нижняя граница периода выборки в формате ISO 8601
    :type afterDate: str
    :param includeUids: Список пользователей, действия которых должны быть включены в список событий
    :type includeUids: str
    :param excludeUids: Список пользователей, действия которых должны быть исключены из списка событий
    :type excludeUids: str
    :param types: Типы событий которые должны быть включены в список. По умолчанию включаются все события
    :type types: str
    :return: :numref:`результат запроса %s <Результат запроса get_mail_log>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса get_mail_log
        :name: Результат запроса get_mail_log

        {
            "events": [
                {
                    "bcc": str,
                    "cc": str,
                    "clientIp": str,
                    "date": str,
                    "destMid": str,
                    "eventType": str,
                    "folderName": str,
                    "folderType": str,
                    "from": str,
                    "labels": [
                        str
                    ],
                    "mid": str,
                    "msgId": str,
                    "orgId": int,
                    "requestId": str,
                    "source": str,
                    "subject": str,
                    "to": str,
                    "uniqId": str,
                    "userLogin": str,
                    "userName": str,
                    "userUid": str
                }
            ],
            "nextPageToken": str
        }

    """

    lst_mail =[]

    mail = logs.mail_log(token, orgID, beforeDate=beforeDate, afterDate=afterDate, includeUids=includeUids, excludeUids=excludeUids, types=None)
    if check_request(mail):
        lst_mail += mail['events']
        mail = logs.mail_log(token, orgID, pageToken=mail['nextPageToken'], beforeDate=beforeDate, afterDate=afterDate, includeUids=includeUids, excludeUids=excludeUids, types=None)
        while mail['nextPageToken'] != '':
            lst_mail += mail['events']
            mail = logs.mail_log(token, orgID, pageToken=mail['nextPageToken'], beforeDate=beforeDate, afterDate=afterDate, includeUids=includeUids, excludeUids=excludeUids, types=None)
        return {"events":lst_mail,"nextPageToken":mail['nextPageToken']}
    else:
        return mail