from os import system as sys
import os
import time
import urllib.request
from threading import Thread
from pathlib import Path
from contextlib import suppress
from BotAmino import BotAmino, Parameters
#from keep_alive import keep_alive

#keep_alive()
os.system("clear")
client = BotAmino()

comid= 144781697

#7996400 on est là
#71560051
@client.command()
def test(data):
  help = ("En marche...")
  data.subClient.send_message(data.chatId, message=help)

@client.event("on_group_member_join")
def on_chat(data):
    try:
        commuId= 144781697
        subClient = client.get_community(commuId)
    except Exception:
        return
    args=Parameters(data,subClient)
    nick=subClient.get_user_info(args.authorId).nickname
    if not "azazaz" in nick:
      subClient.kick(chatId=args.chatId,userId=args.authorId,allowRejoin=True)

@client.event("on_text_message")
def on_chat(data):
    try:
        commuId= 144781697
        subClient = client.get_community(commuId)
    except Exception:
        return
    args=Parameters(data,subClient)
    nick=subClient.get_user_info(args.authorId).nickname
    if not "azazazaz" in nick:
    	subClient.kick(chatId=args.chatId,userId=args.authorId,allowRejoin=True)

client.launch()
print("Bot connecté")