from utils.lolz_api import LolzApi
import utils.config as config
from pyrogram import Client
from utils.utils import extract_telegram_data

from pyrogram.errors.exceptions.forbidden_403 import PeerIdInvalid
from pyrogram.errors.exceptions.bad_request_400 import BalanceTooLow

import asyncio


client = LolzApi(thread_id=config.thread_id,
                 token=config.lolz_token)

app = Client("auto_stars")

async def main():
    post_ids = []
    added_counter = 0
    
    while True:
        new_posts = [p['post_id'] for p in (await client.get_posts())['posts'][1:]]
        new_ids = [post_id for post_id in new_posts if post_id not in post_ids]
        
        if new_ids:
            post_ids.extend(new_ids)
            added_counter += len(new_ids)
            print(f"Добавлено: {len(new_ids)} (Всего: {added_counter}) | ID: {new_ids}")
            
            for post_id in new_ids:
                post_data = await client.get_post(post_id)
                post_body = post_data['post']['post_body']
                
                if not (await client.get_comments(post_id)).get('comments'):
                    tg_data = extract_telegram_data(post_body)
                    
                    if tg_data:
                        try:
                            async with Client("auto_stars") as app:
                                await app.add_paid_message_reaction(
                                    chat_id=tg_data['username'],
                                    message_id=tg_data['post_id'],
                                    star_count=config.star
                                )
                            
                            await client.create_comment(post_id, comment_body=config.text)
                            print(f"Комментарий и {config.star} звезда(звезд) отправлены к посту {post_id}")
                        
                        except BalanceTooLow:
                            print("Ошибка: Недостаточно звёзд на балансе.")
                            continue
                            
                        except PeerIdInvalid:
                            print(f"Ошибка PeerIdInvalid")
                            await client.create_comment(
                                post_id,
                                "В вашем канале отключены платные реакции."
                            )
                            print(f"У пользователя отключены платные реакции. ID: {post_id}")
                    
                    else:
                        await client.create_comment(post_id, comment_body='TG ссылка не найдена!')
                        print(f"Ошибка: Telegram ссылка не найдена. ID: {post_id}")
        else:
            print("Новых постов нет")
            
        await asyncio.sleep(config.delay)

asyncio.run(main())
