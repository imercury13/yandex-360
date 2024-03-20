"""Модуль функций для просмотра организаций пользователя
"""

from jreq.jreq import safe_request
import json

def show_orgs(token, orgID, pageSize=10, pageToken=None):
    """Функция возвращает список организаций пользователя

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param pageSize: Количество организаций на странице. Максимальное значение — 100. По умолчанию — 10
    :type pageSize: int
    :param pageToken: Токен постраничной навигации
    :type pageToken: str
    :return: :numref:`результат запроса %s <Результат запроса show_orgs>`
    :rtype: dict

    .. code-block:: python
        :caption: Результат запроса show_orgs
        :name: Результат запроса show_orgs

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

    url = f'https://api360.yandex.net/directory/v1/org?pageSize={pageSize}'
    if pageToken: url += f'&pageToken={pageToken}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get', url, headers)