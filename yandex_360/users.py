"""Модуль функций для работы с сотрудниками. Просмотр, создание, изменение и удаление.

.. note::
    **Права доступа для работы с данными сотрудников:**

    **directory:read_users** — просмотр;
    **directory:write_users** — просмотр и изменение.


"""

from jreq.jreq import safe_request
import json