"""Модуль функций для работы с сотрудниками. Просмотр, создание, изменение и удаление.

.. note::
    **Права доступа для работы с данными сотрудников:**

    **directory:read_users** — просмотр;
    **directory:write_users** — просмотр и изменение.

"""

from jreq.jreq import safe_request
import json

def show_users(token, orgID, url=None):
    """Функция Возвращает список сотрудников с постраничной навигацией

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param url: :term:`Ключи разбивки на страницы`
    :type url: str or None
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/users/?{url}'
    print(url)
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
	
    return safe_request('get', url, headers)