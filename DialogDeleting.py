# -*- coding: utf-8 -*-
import vk_api
import time

# developer: keyzt
# Site: vk.com/id266855437
# Version: 1.1

"""
 Скрипт для удаления (не)прочитанных сообщений. 
 Измените login и password на свои. 
 В offset написать сколько диалогов отступать(Чтобы не затронуть важные). 
 Если вы хотите удалить непрочитанные сообщения, то в unreaded поставьте значение 1, если же хотите удалить все диалоги, то 0
"""

login = "login"
password = "password"
app_id = 6371584
offset = 20
unreaded = 0  # 0 - удаление всех диалогов(не считая отступа offset), 1 - непрочитанные


def auth(login, password, AppID):

    vk_session = vk_api.VkApi(login, password, AppID)
    print("Начинаю авторизацию...")

    try:
        vk_session.auth()
        print(f"Вы были успешно авторизованы под данными {login}:{password}")

    except Exception as error_msg:
        print(f"Ошибка автоизации. Причина: {error_msg}")
        exit()


    vk = vk_session.get_api()
    return vk


def main(api):
    print("Получение данных...")
    unread = api.messages.getDialogs(offset=offset, count=200, unread=unreaded)

    if not unread['items']:
        return print("Ничего нету")

    for x in unread['items']:
        time.sleep(1)
        try:
            if str(x['message']['user_id']).find("-") != -1:
                print(f"Удаление диалога с сообществом: {str(x['message']['user_id'])}")
                api.messages.deleteDialog(peer_id=x['message']['user_id'])
            else:
                print(f"Удаление диалога с пользователем: {str(x['message']['user_id'])}")
                api.messages.deleteDialog(user_id=x['message']['user_id'])

        except Exception as err_msg:
                    print(f"Ошибка: {err_msg}")
                    exit()
           
    print("Готово")
    exit()

    
vk = auth(login, password, app_id)
while True:
    main(vk)
