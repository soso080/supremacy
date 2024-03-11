import os
#os.system("pip install --upgrade pymino")
from pymino import Bot, Client
from pymino.ext import *


client = Client()


bot = Bot(
    command_prefix="!",
    device_key="E7309ECC0953C6FA60005B2765F99DBBC965C8E9",
    signature_key="DFA5ED192DDA6E88A12FE12130DC6206B1251E44",
    community_id=244133939
)


shawn_commu = "244133939"

@bot.on_ready()
def on_ready():
    print(f"connecté {bot.profile.username}")


@bot.command("t")
def test(ctx: Context):
    ctx.reply("Bot en fonctionnement")


@bot.command("t")
def test(ctx: Context):
    ctx.reply("Bot en fonctionnement")

@bot.command("msg")
def msg(ctx: Context):
    try:
        msgg = ctx.message.content[len("!msg "):]
        msgid = ctx.message.messageId
        bot.community.delete_message(chatId=ctx.chatId, asStaff=True, reason="msg", messageId=msgid)
        bot.community.send_message(chatId=ctx.chatId, content=f"{msgg}",comId=shawn_commu)
    except Exception:
        msgg = ctx.message.content[len("!msg "):]
        bot.community.send_message(chatId=ctx.chatId, content=f"{msgg}",comId=shawn_commu)

@bot.command("titre")
def title(ctx: Context):
    le_titre = ctx.message.content[len("!titre"):]
    bot.community.edit_titles(comId=ctx.comId, userId=ctx.author.userId, titles=le_titre, colors=["#000000"])
    bot.community.send_message(chatId=ctx.chatId, content="c'est bon !", comId=ctx.comId)


@bot.command("join")
def join(ctx: Context):
    bot.community.join_chat(comId=shawn_commu,chatId=ctx.chatId)
    bot.community.send_message(chatId=ctx.chatId, content="Me voici", comId=shawn_commu)

@bot.command("joinall")
def joinall(ctx: Context):
    chat = bot.community.fetch_chats(comId=shawn_commu).chatId
    for chats in chat:
        bot.community.join_chat(comId=shawn_commu,chatId=chats)
    bot.community.send_message(chatId=ctx.chatId, content="C'est bon j'ai fini de rejoindre tout les chats", comId=shawn_commu)

@bot.command("online")
def online(ctx: Context):
    on = bot.community.fetch_online_users(size=100, comId=shawn_commu).nickname
    bot.community.send_message(chatId=ctx.chatId, content="Les membres connecté sont : "
                                                          f"{on}",
                               comId=shawn_commu)

@bot.command("ac")
def ac(ctx: Context):
    amc = bot.account.fetch_wallet().totalCoins
    bot.community.send_message(chatId=ctx.chatId, content=f"J'ai {amc} ac",comId=shawn_commu)

@bot.command("id")
def id_finder(ctx: Context):
    msg = ctx.message.content[len("!id"):]
    id = bot.community.fetch_object_id(msg)
    bot.community.send_message(chatId=ctx.chatId, content=f"l'id : {id}", comId=shawn_commu)


@bot.command("bio")
def bio(ctx: Context):
    labio = ctx.message.content[len("!bio "):]
    bot.community.edit_profile(content=f"{labio}", comId=shawn_commu)
    bot.community.send_message(chatId=ctx.chatId, content="la bio vient d'etre modifiée", comId=shawn_commu)

@bot.command("sup")
def sup(ctx: Context):
    moi = "a92d7072-c06d-45d3-bf5f-b8bf3846e552"
    leader = bot.community.fetch_users(userType=UserTypes.LEADERS).userId
    curateur = bot.community.fetch_users(userType=UserTypes.CURATORS).userId
    staff = moi or leader or curateur

    nbr = ctx.message.content[len("!sup "):]
    if ctx.author.userId in staff:
        for msgId in bot.community.fetch_messages(chatId=ctx.chatId, size=nbr, comId=shawn_commu).messageId:
            bot.community.delete_message(chatId=ctx.chatId, reason="sup", messageId=msgId, asStaff=True, comId=shawn_commu)

        else:
            ctx.reply("Commande Staff", delete_after=3)


@bot.command("voc")
def voc(ctx: Context):
    bot.community.start_vc(chatId=ctx.chatId, comId=shawn_commu)
    bot.community.send_message(chatId=ctx.chatId, content="Me voilaaa ! ", comId=shawn_commu)

@bot.command("fin")
def fin(ctx: Context):
    bot.community.stop_vc(chatId=ctx.chatId, comId=shawn_commu)
    bot.community.send_message(chatId=ctx.chatId, content="Je m'éclipse ! ", comId=shawn_commu)



bot.run(email="Minneemerick@gmail.com", password="Nougat9900")


