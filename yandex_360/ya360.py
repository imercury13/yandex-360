"""Модуль функций библиотеки"""

from jreq.jreq import safe_request

def _check_request(req):
	"""Функция проверки ответа запроса
	
	:param req: результат запроса
	:type req: dict
	"""
	if 'code' in req and 'message' in req:
		print('Код ошибки: '+str(req['code'])+' Сообщение: '+req['message'])
		exit(1)

def create_group(args, token, orgID):
    """Функция создания группы

    :param args: словарь аргументов командной строки
    :type args: dict
    """

    url = 'https://api360.yandex.net/directory/v1/org/'+orgID+'/groups/'
    headers={'Authorization': 'OAuth '+token, 'Content-type': 'application/json'}
    body = {}
    body.update({'name':args.name})
    if args.label: body.update({'label':args.label})
    if args.adminIds: body.update({'adminIds':args.adminIds})
    if args.description: body.update({'description':args.description})
    cg = safe_request('post', url, headers, body)
    _check_request(cg)
    print('Группа создана с ID: '+str(cg['id']))

