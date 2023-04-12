from telethon import TelegramClient, events

from config import config

client = TelegramClient(':memory', config.API_ID, config.API_HASH)


@client.on(events.NewMessage(chats=config.TARGET_CHANNEL))
async def my_event_handler(event):
    if "#крипто" in event.text:
        await client.forward_messages(config.DESTINATION_CHANNEL, messages=event.message)


client.start()
client.run_until_disconnected()
