"""Модуль функций для работы с подразделениями. Просмотр, создание, изменение и удаление.

.. note::
    **Права доступа для работы с подразделениями:**

    **directory:read_departments** — просмотр;
    **directory:write_departments** — просмотр и изменение.


"""

from jreq.jreq import safe_request
import json

