Глоссарий
=========

.. glossary::
   :sorted:

   ID организации в Яндекс 360
      Числовой идентификатор организации в сервисе Яндекс 360. Его можно увидеть на странице `профиля организации <https://admin.yandex.ru/company-profile>`_.

   ID пользователя в Яндекс 360
      Числовой идентификатор пользователя в сервисе Яндекс 360.

   ID подразделения в Яндекс 360
      Числовой идентификатор подразделения в сервисе Яндекс 360.

   ID записи
      Числовой идентификатор записи
   
   Яндекс токен приложения
      Токен авторизации экземпляра приложения

      .. tip::
         Для более простой работы с токенами Яндекс OAuth, вы можете воспользоваться библиотекой
         `yandex_oauth <https://yandex-oauth.readthedocs.io/>`_

         .. code-block:: console

            $ pip install yandex_oauth

   Полное доменное имя
      Например example.com. Для кириллических доменов (например домен.рф) используйте кодировку Punycode.

      Используется в функциях:
         * :func:`yandex_360.dns.show_dns`
         * :func:`yandex_360.dns.edit_dns`
         * :func:`yandex_360.dns.delete_dns`
         * :func:`yandex_360.dns.add_dns`

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


   Тело запроса добавления записи DNS
      * :func:`yandex_360.dns.add_dns`
      .. code-block:: python
         
         {
            "address": str,
            "exchange": str,
            "flag": int,
            "name": str,
            "port": int,
            "preference": int,
            "priority": int,
            "tag": str,
            "target": str,
            "text": str,
            "ttl": int,
            "type": str,
            "value": str,
            "weight": int
         }

   Тело запроса редактирования записи DNS
      * :func:`yandex_360.dns.edit_dns`
      .. code-block:: python

         {
            "address": str,
            "exchange": str,
            "name": str,
            "port": int,
            "preference": int,
            "priority": int,
            "target": str,
            "text": str,
            "ttl": int,
            "type": str,
            "weight": int
         }

   Тело запроса редактирования основного адреса и подписи
      * :func:`yandex_360.mail.edit_sender_info`
      .. code-block:: python

         {
            "defaultFrom": str,
            "fromName": str,
            "signPosition": str,
            "signs": [
               {
                  "emails": [
                     str
                  ],
                  "isDefault": bool,
                  "lang": str,
                  "text": str
               }
            ]
         }

   Тело запроса добавления правила автоответа или пересылки
      * :func:`yandex_360.mail.edit_user_rules`
      .. code-block:: python

         {
            "autoreply": {
               "ruleName": str,
               "text": str
            },
            "forward": {
               "address": str,
               "ruleName": str,
               "withStore": bool
            }
         }

   Тело запроса автоматического сбора контактов
      * :func:`yandex_360.mail.edit_address_book`
      .. code-block:: python

         {
            "collectAddresses": bool
         }

