"""Модуль для управления аудит-логов.
"""

from jreq.jreq import safe_request
import json

def disk_log(token, orgID, pageSize=100):
    """Функция возвращает список событий в аудит-логе Диска организации.

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param pageSize: Количество событий на странице
    :type pageSize: int
    :param pageToken: Токен постраничной навигации
    :type pageToken: str
    :param beforeDate: Верхняя граница периода выборки в формате ISO 8601
    :type beforeDate: str
    :param afterDate: Нижняя граница периода выборки в формате ISO 8601
    :type afterDate: str
    :param includeUids: Список пользователей, действия которых должны быть включены в список событий
    :type includeUids: list
    :param excludeUids: Список пользователей, действия которых должны быть исключены из списка событий
    :type excludeUids: list
    :return: :numref:`результат запроса %s <Результат запроса disk_log>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса disk_log
        :name: Результат запроса disk_log

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

    url = f'https://api360.yandex.net/security/v1/org/{orgID}/audit_log/disk?pageSize={pageSize}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
	
    return safe_request('get', url, headers)

def mail_log(token, orgID, pageSize=100):
    """Функция возвращает список событий в аудит-логе Почте организации.

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param pageSize: Количество событий на странице
    :type pageSize: int
    :param pageToken: Токен постраничной навигации
    :type pageToken: str
    :param beforeDate: Верхняя граница периода выборки в формате ISO 8601
    :type beforeDate: str
    :param afterDate: Нижняя граница периода выборки в формате ISO 8601
    :type afterDate: str
    :param includeUids: Список пользователей, действия которых должны быть включены в список событий
    :type includeUids: list
    :param excludeUids: Список пользователей, действия которых должны быть исключены из списка событий
    :type excludeUids: list
    :param types: Типы событий которые должны быть включены в список. По умолчанию включаются все события
    :type types: list
    :return: :numref:`результат запроса %s <Результат запроса mail_log>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса mail_log
        :name: Результат запроса mail_log

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

    url = f'https://api360.yandex.net/security/v1/org/{orgID}/audit_log/mail?pageSize={pageSize}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
	
    return safe_request('get', url, headers)