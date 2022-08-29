Глоссарий
=========

.. glossary::
   :sorted:

   ID организации в Яндекс 360
      Числовой идентификатор организации в сервисе Яндекс 360. Его можно увидеть на странице `профиля организации <https://admin.yandex.ru/company-profile>`_.

   Яндекс токен приложения
      Токен авторизации экземпляра приложения

      .. tip::
         Для более простой работы с токенами Яндекс OAuth, вы можете воспользоваться библиотекой
         `yandex_oauth <https://yandex-oauth.readthedocs.io/>`_

         .. code-block:: console

            $ pip install yandex_oauth


   Ключи разбивки на страницы
      Это символьная строка, содержащая два параметра в url запросе для указания номера выводимой страницы и количества записей на ней.
      
      Используется в функциях:
         * :func:`yandex_360.ya360.show_users`
         * :func:`yandex_360.ya360.show_groups`
         * :func:`yandex_360.ya360.show_departments`

         Обусловленно это тем, что данные функции возвращают большое количество данных, которые необходимо разбивать постранично.

      Ключи:
         * ``page``: номер страницы
         * ``perPage``: количество записей на странице

      Пример формирования строки `url`:
         .. code-block:: python

            url = ''
            if args.page:
               url += 'page='+str(args.page)+'&'
            else:
               url += 'page=1&'
            if args.perPage:
               url += 'perPage='+str(args.perPage)+'&'
            else:
               url += 'perPage=1000'
