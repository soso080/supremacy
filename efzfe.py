import subprocess
#subprocess.call(['pip', 'install', 'pymongo'])
import os
import time

#os.system("sudo pip install googletrans")
#os.system("pip install --upgrade amino.fix")
#os.system("pip install --upgrade BotAmino")
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
#from keep_alive import keep_alive
#keep_alive()
import tempfile
from os import path
import json
from termcolor import colored
import sys
from concurrent.futures import ThreadPoolExecutor
from random import uniform, choice, randint
import youtube_dl ,os, urllib.request, subprocess, webbrowser
from gtts import gTTS, lang
from google_trans_new import google_translator
from constant import LANGUAGES, DEFAULT_SERVICE_URLS
from random import choice, randint
import urllib
from BotAmino import *
import random
from PIL import Image, ImageFont, ImageDraw
import requests
import urllib.parse
from multiprocessing.pool import ThreadPool
from googletrans import Translator
from datetime import datetime
import soso
#mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
moi = "a92d7072-c06d-45d3-bf5f-b8bf3846e552"
iku = "b3c859d0-983d-4a10-a6d1-eb11eebbf2e3"
# 79964099 anime mangas scan
# 93307693 univers perdu
# 180011716 Laboratoire
#114703339 village pommer


email="nilal34244@labebx.com"
mdp="Soridu94"
#email="1mjto2sdgp@xojxe.com"
#mdp="Sosolebg123"
client = BotAmino(email=email, password=mdp)
s = client.sid
sidd=f"{s}"
client = BotAmino(sid=sidd)

path_utilities = 'utilities'
path_amino = f'{path_utilities}/amino_list'
path_download = "news"
client.bio = f"Createur du bot : soso" \
             f"!help pour plus de details "
client.prefix = "!"
client.activity = True
client.wait = 3
client.spam_message = "calme down tu spam"
client.favorite_users = "user_bloque"


#uri = "mongodb+srv://Soso_Supremacy:<Supremacy123>@supremacydb.ukceghk.mongodb.net/?retryWrites=true&w=majority"
#climongo = MongoClient(uri, server_api=ServerApi('1'))
#try:
#   climongo.admin.command('ping')
#  print("Connection a la base de donné reussi !")
#except Exception as e:
#    print(e)






def sosoo(data):
    return data.authorId in ('a92d7072-c06d-45d3-bf5f-b8bf3846e552')


def staff(data):
    return data.authorId in ("a92d7072-c06d-45d3-bf5f-b8bf3846e552") or data.subClient.is_in_staff(data.authorId)


def supremacy(data):
    return data.authorId in ("a92d7072-c06d-45d3-bf5f-b8bf3846e552") or ('b3c859d0-983d-4a10-a6d1-eb11eebbf2e3')

def not_staff(data):
    membre = data.subClient.get_user_info(data.authorId).role == 0
    if data.authorId:
        return membre


def not_leader(data):
    membre = data.subClient.get_user_info(data.authorId).role == 0
    curateur = data.subClient.get_user_info(data.authorId).role == 101
    leader = data.subClient.get_user_info(data.authorId).role == 102
    if data.authorId:
        return membre or curateur
    else:
        data.subClient.send_message(message="interdit au leader", chatId=data.chatId)


def participant(data):
    with open("pvpauth.txt", "r") as f:
        # Lire le contenu du fichier pvpauth.txt et stocker chaque ligne dans une liste temporaire
        temp_list = f.readlines()
    # Retirer le caractère de retour à la ligne (\n) de chaque ID dans la liste temporaire
    temp_list = [id.strip() for id in temp_list]
    # Vérifier si l'ID de l'auteur du message est présent dans la liste temporaire
    return data.authorId in temp_list

@client.command()
def res(data):
    lui = data.subClient.search_users(data.message, size=25).userId
    data.subClient.send_message(data.chatId, f"{lui}")


@client.command()
def staff(data):
    leader = data.subClient.get_all_users(type="leaders", size=25).profile.userId
    cura = data.subClient.get_all_users(type="curators", size=25).profile.userId
    for staff in leader:
        print(staff)
    for staf in cura:
        print(staf)


@client.command()
def bu(data):
    lien = client.get_from_code(data.message).objectId
    b = data.subClient.get_user_info(lien).defaultBubbleId
    data.subClient.send_message(message=f"{b}", chatId=data.chatId)


@client.command()
def debilos(data):
    data.subClient.kick(userId="49f82a71-7a67-4999-a71b-b73ad040781d", chatId=data.chatId, allowRejoin=True)


@client.command()
def kikall(data):
    hote = data.subClient.get_chat_thread(data.chatId).author.userId
    b = data.subClient.get_chat_users(chatId=data.chatId, size=1000).userId
    try:
        for user in b:
            if user in hote:
                print("l'hote")
            else:
                data.subClient.kick(userId=user, chatId=data.chatId)
    except Exception:
        print("erreur")

@client.command()
def banall(data):
    a = data.subClient.get_all_users(size=1000).profile.userId
    leader = data.subClient.get_all_users(type="leaders",size=25).profile.userId
    try:
        for b in a:
            if b in leader:
                print("c'est un leader")
            else:
                data.subClient.ban(userId=b, reason="banall")
    except Exception:
        print("leader")
    data.subClient.send_message(message=f"bannissement terminer !", chatId=data.chatId)


@client.command()
def debanall(data):
    a = data.subClient.get_all_users(type="banned", size=1000).profile.userId
    for b in a:
        data.subClient.unban(userId=b, reason="banall")
    data.subClient.send_message(message=f"debannissement terminer !", chatId=data.chatId)



@client.command()
def inv(data):
    tout = data.subClient.get_all_users(size=1000).profile.userId
    for user in tout:
        try:
            data.subClient.invite_to_chat(userId=user, chatId=data.chatId)
        except Exception:
            print("Deja fait")
    data.subClient.send_message(message=f"fait", chatId=data.chatId)



@client.command()
def copvp(data):
    with open("pvpauth.txt", "a") as f:
        # Ajouter l'ID de l'auteur du message en tant que ligne dans le fichier
        f.write(f"{data.authorId}\n")
        data.subClient.send_message(message=f"Connexion de {data.author} au pvp...", chatId=data.chatId)
        time.sleep(3)
        data.subClient.send_message(message=f"{data.author} s'est connecter avec succes au pvp !", chatId=data.chatId)


@client.command()
def decopvp(data):
    data.subClient.send_message(message=f" deconnexion de {data.author} du pvp !", chatId=data.chatId)
    time.sleep(3)
    with open("pvpauth.txt", "r") as f:
        temp_list = f.readlines()
    temp_list = [id.strip() for id in temp_list]
    if data.authorId in temp_list:
        temp_list.remove(data.authorId)
    with open("pvpauth.txt", "w") as f:
        for id in temp_list:
            f.write(f"{id}\n")
    data.subClient.send_message(message=f"{data.author} s'est déconnecté avec succès du pvp !", chatId=data.chatId)



@client.command()
def argent(data):
    nbr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    nbr = random.choice(nbr)
    with open("coins.txt", "r+") as f:
        lines = f.readlines()
        now = datetime.now()
        if now.hour >= 12:
            f.seek(0)
            f.truncate()
            data.subClient.send_message(message="La commande !coins est reset pour tout le monde ! ", chatId=data.chatId)
        elif data.authorId + "\n" not in lines:
            data.subClient.add_influencer(data.authorId, nbr)
            data.subClient.subscribe(data.authorId, False)
            data.subClient.remove_influencer(data.authorId)
            data.subClient.send_message(message=f"gg tu as gagné {nbr} AC ! Retente ta chance demain.", chatId=data.chatId)
            f.write(data.authorId + "\n")
        else:
            data.subClient.send_message(message="Bouge et retente demain.", chatId=data.chatId)



@client.command()
def cadre(data):
    try:
        u = client.get_from_code(data.message).objectId
        a = data.subClient.get_user_info(u).avatarFrameId
        data.subClient.apply_avatar_frame(avatarId=a, applyToAll=True)
        data.subClient.send_message(message="fait", chatId=data.chatId)
    except Exception:
        u = client.get_from_code(data.message).objectId
        a = data.subClient.get_user_info(u).avatarFrameId
        client.purchase(objectId=a, isAutoRenew=False)
        data.subClient.apply_avatar_frame(avatarId=a, applyToAll=True)
        data.subClient.send_message(message="fait", chatId=data.chatId)




@client.command()
def join(data):
    data.subClient.join_chat(data.chatId)


@client.command()
def coms(data):
    a = client.search_community(aminoId=data.message).name
    data.subClient.send_message(message=f"{a}", chatId=data.chatId)

@client.command()
def sex(data):
    sex = open("Ahhh.mp3", 'rb')
    data.subClient.send_message(fileType="audio", file=sex, chatId=data.chatId)



@client.command()
def test(data):
    soso.msg(message="bot en marche...", chatId=data.chatId, data=data)

@client.command()
def accepte(data):
    nid = data.subClient.get_notices(size=25).noticeId
    try:
        for n in nid:
            data.subClient.promotion(type="accept", noticeId=n)
        print("fait")
        data.subClient.send_message(message="role accepter !", chatId=data.chatId)
    except Exception:
        print("Erreur")


@client.command()
def antiku(data):
    data.subClient.send_message(message="antiku en marche...", chatId= data.chatId)


@client.command(condition=sosoo)
def lead(data):
    #user = client.get_from_code(data.message).objectId
    user = data.authorId
    data.subClient.promote(userId=user, rank="leader")
    data.subClient.send_message(message="Fait", chatId=data.chatId)

@client.command()
def cura(data):
    #user = client.get_from_code(data.message).objectId
    user = data.authorId
    data.subClient.promote(userId=user, rank="curator")
    data.subClient.send_message(message="Fait", chatId=data.chatId)


@client.command()
def liste(data):
    liste = data.subClient.list_communities(size=25).link
    listee = data.subClient.list_communities(size=25).name
    data.subClient.send_message(message=f"{liste}", chatId=data.chatId)
    data.subClient.send_message(message=f"{listee}", chatId=data.chatId)




@client.command()
def tr(data):
    cry = open("crybaby.mp3", 'rb')
    data.subClient.send_message(fileType="audio", file=cry, chatId=data.chatId)


@client.command()
def j(data):
    try:
        comId = client.get_from_code(data.message).comId
        chatId = client.get_from_code(data.message).objectId
        client.join_community(comId=comId)
        data.subClient.join_chat(chatId)
        data.subClient.send_message(message="rejoins", chatId=data.chatId)
    except Exception:
        comId = client.get_from_code(data.message).comId
        client.join_community(comId=comId)


@client.command()
def autodestruction(data):
    data.subClient.send_message(message="autodestruction dans 3sec...", chatId=data.chatId)
    time.sleep(3)
    data.subClient.leave_amino()

@client.command()
def suprole(data):
    data.subClient.leave_amino()
    client.join_community(data.comId)
    data.subClient.join_chat(data.chatId)

@client.on_member_join_chat()
def Bienvenue(data):
    lolo = ("bienvenue.png")
    chat = data.subClient.get_chat_thread(chatId=data.chatId).title
    nom = data.subClient.get_user_info(userId=data.authorId).nickname
    pdp = data.subClient.get_user_info(userId=data.authorId).icon
    response = requests.get(f"{pdp}")
    file = open("pdp.png", "wb")
    file.write(response.content)
    file.close()
    pp_init = Image.open("pdp.png")
    pp_init = pp_init.resize((200, 200))
    mask = Image.new('L', (200, 200), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 200, 200), fill=(255), outline=(0))
    pp_init.putalpha(mask)
    pp_init = pp_init.resize((300, 300))
    pp_init.save("pdp.png")
    with Image.open(lolo) as im:
        im_res = im.resize((900, 600)).save("bienvenue.png")
    fond = Image.open("bienvenue.png")
    draw = ImageDraw.Draw(fond)
    font_nom = ImageFont.truetype('georgiaz.ttf', size=75)
    font_bienvenue = ImageFont.truetype('georgiaz.ttf', size=100)
    violet = (166, 56, 188)
    rouge = (255, 0, 0)
    draw.text((300, 70), f'{nom}', font=font_nom, fill=rouge)
    draw.text((155, 450), f'Bienvenue !', font=font_bienvenue, fill=rouge)
    txt =  f"""[BC]━━━━┅━━━┅━━━━
[BC] {data.author} Bienvenue dans le chat {chat}
[C]1.Croyez en la soso supremacy !😌
[C]2.Suivez les règles et les directives du chat et de l'amino.
[C]3.Respectez l'hôte, les cohôte et les membres.
[C]4.Amuser vous bien.😁
[BC]━━━━┅━━━┅━━━━"""
    pos = (300, 170)
    fond.paste(pp_init, pos, pp_init)
    fond.save("truc.png")
    fnl = open("truc.png", 'rb')
    data.subClient.full_embed(link=" ", image=fnl, message=txt, chatId=data.chatId)


@client.on_member_leave_chat()
def aurevoir(data):
    lolo = ("aurevoir.png")
    Image.open(lolo).resize((863, 400)).save("aurevoir.png")
    ku = open("aurevoir.png", "rb")
    msg = f"a bientot ^^ "
    data.subClient.full_embed("aminoapps.com/p/5w2u19", ku, msg, data.chatId)



@client.command()
def uid(data):
    user = client.get_from_code(data.message).objectId
    id = data.subClient.get_user_info(user).userId
    data.subClient.send_message(message=f"{id}", chatId=data.chatId)



@client.command()
def glo(data):
    toi = client.get_from_code(data.message).objectId
    g = client.get_user_info(toi).aminoId
    data.subClient.send_message(message=f"http://aminoapps.com/u/{g}", chatId=data.chatId)



@client.command()
def bulle(data):
    msg = data.message
    if "rouge" in msg:
        data.subClient.apply_bubble(bubbleId="3265eb6a-b6c4-4c0b-a3f6-ee144dddf40a", chatId=data.chatId, applyToAll=True)
        data.subClient.send_message(message="fait", chatId=data.chatId)
    elif "rose" in msg:
        data.subClient.apply_bubble(bubbleId="1c430d67-cf25-4baa-81de-ad00945d1070", chatId=data.chatId, applyToAll=True)
        data.subClient.send_message(message="fait", chatId=data.chatId)
    elif "noir" in msg:
        data.subClient.apply_bubble(bubbleId="654488a6-4e7e-4b0b-9c5f-5d1640538a1f", chatId=data.chatId, applyToAll=True)
        data.subClient.send_message(message="fait", chatId=data.chatId)
    elif "vert" in msg:
        data.subClient.apply_bubble(bubbleId="b468602e-a43e-41e3-92ec-cfcc3c5028fd", chatId=data.chatId, applyToAll=True)
        data.subClient.send_message(message="fait", chatId=data.chatId)
    elif "go" in msg:
        data.subClient.apply_bubble(bubbleId="36f9056b-7ce1-40a4-a918-00e21b8c2b71", chatId=data.chatId,applyToAll=True)
        data.subClient.send_message(message="fait", chatId=data.chatId)


@client.command()
def copy(data):
    try:
        user = client.get_from_code(data.message).objectId
        ni = data.subClient.get_user_info(user).nickname
        pi = data.subClient.get_user_info(user).icon
        response = requests.get(f"{pi}")
        file = open("pp.png", "wb")
        with open("pp.png", "wb") as file:
            file.write(response.content)
        with open("pp.png", "rb") as file:
            data.subClient.edit_profile(icon=file, nickname=ni)
            data.subClient.send_message(message="copié !", chatId=data.chatId)
    except Exception:
        n = data.subClient.get_user_info(data.authorId).nickname
        p = data.subClient.get_user_info(data.authorId).icon
        response = requests.get(f"{p}")
        file = open("pp.png", "wb")
        with open("pp.png", "wb") as file:
            file.write(response.content)
        with open("pp.png", "rb") as file:
            data.subClient.edit_profile(icon=file,nickname=n)
            data.subClient.send_message(message="copier !", chatId=data.chatId)


@client.command()
def pp(data):
    pdp = data.subClient.get_user_info(data.authorId).icon
    response = requests.get(pdp)
    response.raise_for_status()
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(response.content)
        temp_filepath = f.name
    with open(temp_filepath, 'rb') as f:
        data.subClient.send_message(file=f, fileType="image", chatId=data.chatId)
        f.close()
        os.unlink(temp_filepath)



@client.command()
def help(data):
    lolo = ("help.png")
    Image.open(lolo).resize((863, 400)).save("help.png")
    ku = open("help.png", "rb")
    msg = f"""[Cub]les Commandes du bot :\n\n[C]◈.!bot — Commande general du bot.\n[C]◈. !membre — liste des commande membre.\n[C]◈. !modo — commande staff.\n[C]◈. !admin — commande admin."""
    data.subClient.full_embed("aminoapps.com/p/5w2u19", ku, msg, data.chatId)


@client.command()
def bot(data):
    lolo = ("help.png")
    Image.open(lolo).resize((863, 400)).save("help.png")
    ku = open("help.png", "rb")
    msg = f"""[Cub]les Commandes general du bot :\n\n[C]◈  !msg  ◈ !vc  ◈ !voc \n◈ !fin ◈ !ship ◈ !pvp \n[C]◈ !fight ◈ !titre ◈ !fond \n ◈ !profile ◈ !roue ◈ !follow\n ◈ !infos ◈ !unfollow ◈ !pv ◈ !post ◈ !suicide ◈ !name \n[C]◈ !copy ◈ !hack ◈ !os \n◈ !coins ◈ !ac ◈ !os \n◈ !joinc ◈ !delcom ◈ !chatb \n◈ !sex ◈ !test ◈ !infos                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           """
    data.subClient.full_embed("aminoapps.com/p/5w2u19", ku, msg, data.chatId)

@client.command()
def membre(data):
    lolo = ("help.png")
    Image.open(lolo).resize((863, 400)).save("help.png")
    ku = open("help.png", "rb")
    msg = f"""[Cub]les Commandes membres :◈!soso ◈ !iku ◈ !pro ◈ !guess ◈ !shawn  """
    data.subClient.full_embed("aminoapps.com/p/5w2u19", ku, msg, data.chatId)

@client.command("modo", condition=staff)
def modo(data):
    lolo = ("help.png")
    Image.open(lolo).resize((863, 400)).save("help.png")
    ku = open("help.png", "rb")
    msg = f"""[Cub]les Commandes staff/modo :\n\n[C]◈.!chatid .\n[C]◈. !comuid .\n[C]◈. !@ .\n[C]◈. !joinall .\n[C]◈. !sup.\n[C]◈. !ban .\n[C]◈. !deban .\n[C]◈. !comid. """
    data.subClient.full_embed("aminoapps.com/p/5w2u19", ku, msg, data.chatId)


@client.command("admin", condition=supremacy)
def admin(data):
    lolo = ("help.png")
    Image.open(lolo).resize((863, 400)).save("help.png")
    ku = open("help.png", "rb")
    msg = f"""[Cub]les Commandes admin/supremacy :\n\n[C]◈.!block .\n[C]◈. !deblock .\n[C]◈. !chaos.\n[C]◈. !bantroll .\n[C]◈. !clk.\n[C]◈. !spam .\n[C]◈. !act . """
    data.subClient.full_embed("aminoapps.com/p/5w2u19", ku, msg, data.chatId)



@client.command()
def vc(data):
    audio_file = f"{path_download}/ttp.mp3"
    gTTS(text=data.message, lang='fr', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)



@client.command()
def voc(data):
    client.start_vc(comId=data.comId, chatId=data.chatId)
    data.subClient.send_message(message="me voilaa !",chatId=data.chatId)
    client.show_online(data.comId)


@client.command()
def fin(data):
    client.end_vc(comId=data.comId, chatId=data.chatId)
    data.subClient.send_message(message="Je m'eclipse !",chatId=data.chatId)


@client.command()
def proj(data):
    client.start_screen_room(comId=data.comId ,chatId=data.chatId,joinType=1)


@client.command()
def ban(data):
    userId = client.get_from_code(data.message).objectId
    data.subClient.ban(userId=userId, reason="test")
    data.subClient.send_message(chatId=data.chatId, message="banni avec succes")

@client.command(condition=staff)
def deban(data):
    userId = client.get_from_code(data.message).objectId
    data.subClient.unban(userId=userId, reason="test")
    data.subClient.send_message(chatId=data.chatId, message="debanni avec succes")

@client.command()
def name(data):
    data.subClient.edit_profile(nickname=data.message)
    data.subClient.send_message(chatId=data.chatId, message=f"mon nouveau nom est {data.message}")


@client.command()
def follow(data):
    data.subClient.follow(userId=data.authorId)
    data.subClient.send_message(message="fait", chatId=data.chatId)

@client.command()
def unfollow(data):
    data.subClient.unfollow(userId=data.authorId)
    data.subClient.send_message(message="fait", chatId=data.chatId)

@client.command()
def msg(data):
    msg = data.message
    #msgid = data.subClient.get_chat_messages(chatId=data.chatId, size=1, pageToken=None).messageId
    data.subClient.delete_message(chatId=data.chatId, messageId=data.messageId, asStaff=True, reason="bouhh")
    data.subClient.send_message(message=msg, chatId=data.chatId)


@client.command()#condition=participant
def fight(data):
    f = data.subClient.get_message_info(data.chatId, data.messageId).mentionUserIds[0]
    #a = data.subClient.get_message_info(data.chatId, data.messageId).mentionUserIds[1]
    msg = data.message
    msg = msg.split(" ")
    lolo = ("pvp.png")
    nom = data.subClient.get_user_info(f).nickname
    pdp = data.subClient.get_user_info(f).icon
    nom2 = data.subClient.get_user_info(data.authorId).nickname
    pdp2 = data.subClient.get_user_info(data.authorId).icon
    response = requests.get(f"{pdp}")
    file = open("pdp.png", "wb")
    file.write(response.content)
    file.close()
    response2 = requests.get(f"{pdp2}")
    file2 = open("pdp2.png", "wb")
    file2.write(response2.content)
    file2.close()
    pp_init = Image.open("pdp.png")
    pp_init = pp_init.resize((200, 200))
    mask = Image.new('L', (200, 200), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 200, 200), fill=(255), outline=(0))
    pp_init.putalpha(mask)
    pp_init = pp_init.resize((150, 150))
    pp_init.save("pdp.png")
    pp_init2 = Image.open("pdp2.png")
    pp_init2 = pp_init2.resize((200, 200))
    mask = Image.new('L', (200, 200), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 200, 200), fill=(255), outline=(0))
    pp_init2.putalpha(mask)
    pp_init2 = pp_init2.resize((150, 150))
    pp_init2.save("pdp2.png")
    # --------------------partie 1: affrontement------------------------------------
    with Image.open(lolo) as im:
        im_res = im.resize((900, 600)).save("pvp.png")
    fond = Image.open("pvp.png")
    draw = ImageDraw.Draw(fond)
    font_nom = ImageFont.truetype('georgiaz.ttf', size=90)
    font_bienvenue = ImageFont.truetype('georgiaz.ttf', size=40)
    rouge = (255, 0, 0)
    draw.text((370, 200), f'vs', font=font_nom, fill=rouge)
    txt = f"{nom2} a engager le combat contre {nom}"
    pos = (130, 25)
    pos2 = (520,20)
    fond.paste(pp_init2, pos2, pp_init2)
    fond.paste(pp_init, pos, pp_init)
    fond.save("ikouille.png")
    fnl = open("ikouille.png", 'rb')
    data.subClient.full_embed(link=" ", image=fnl, message=txt, chatId=data.chatId)
    #-------------------------partie2: combat---------------------------------------
    lala =("combat.png")
    txtb = "Le combat s'annonce ardue !"
    with Image.open(lala) as com:
        im_res = com.resize((900, 600)).save("combat.png")
        fondc = Image.open("combat.png")
        draww = ImageDraw.Draw(fondc)
        posg2 = (150, 400)
        posg = (600, 5)
        fondc.paste(pp_init2, posg2, pp_init2)
        fondc.paste(pp_init, posg, pp_init)
        fondc.save("combat.png")
        cbc = open("combat.png", 'rb')
        data.subClient.full_embed(link=" ", image=cbc, message=txtb, chatId=data.chatId)
        # -------------------------partit3: resultat------------------------------------------
        resultat = [Image.open("gwin.png"), Image.open("egalite.png"), Image.open("vwin.png"), Image.open("gwin.png"),Image.open("vwin.png")]
        res = random.choice(resultat)
        filename = res.filename
        if res.filename == "gwin.png":
            txtg = f"{nom2} a battu {nom}!"
            gogo = ("gwin.png")
            with Image.open(gogo) as gw:
                im_res = gw.resize((900, 600)).save("gwin.png")
            gwin = Image.open("gwin.png")
            gdraw = ImageDraw.Draw(gwin)
            posg = (450, 360)
            posg2 = (350, 90)
            gwin.paste(pp_init, posg, pp_init)
            gwin.paste(pp_init2, posg2, pp_init2)
            gwin.save("gwin.png")
            gg = open("gwin.png", 'rb')
            data.subClient.full_embed(link=" ", image=gg, message=txtg, chatId=data.chatId)
            data.subClient.kick(userId=f, chatId=data.chatId, allowRejoin=True)
            data.subClient.add_influencer(userId=data.authorId, monthlyFee=20)
            data.subClient.subscribe(data.authorId, autoRenew=False)
            data.subClient.remove_influencer(data.authorId)
        elif res.filename == "egalite.png":
            gal = ("egalite.png")
            with Image.open(gal) as gl:
                im_res = gl.resize((900, 600)).save("egalite.png")
                gl = Image.open("egalite.png")
                edraw = ImageDraw.Draw(gl)
                posg2 = (150, 100)
                posg = (600, 150)
                gl.paste(pp_init, posg, pp_init)
                gl.paste(pp_init2, posg2, pp_init2)
                gl.save("egalite.png")
                ee = open("egalite.png", 'rb')
                txtf = "on dirais bien qu'on a aucun vainqeur !"
                data.subClient.full_embed(link=" ", image=ee, message=txtf, chatId=data.chatId)
        elif res.filename == "vwin.png":
            txtv = f"{nom} a battu {nom2} ! "
            veve = ("vwin.png")
            with Image.open(veve) as vw:
                im_res = vw.resize((900, 600)).save("vwin.png")
                vwin = Image.open("vwin.png")
                vdraw = ImageDraw.Draw(vwin)
                posg = (450, 200)
                posg2 = (325, 100)
                vwin.paste(pp_init, posg, pp_init)
                vwin.paste(pp_init2, posg2, pp_init2)
                vwin.save("vwin.png")
                vv = open("vwin.png", 'rb')
                data.subClient.full_embed(link=" ", image=vv, message=txtv, chatId=data.chatId)
                data.subClient.kick(data.authorId, data.chatId, allowRejoin=True)
                data.subClient.add_influencer(f, monthlyFee=20)
                data.subClient.subscribe(f, autoRenew=False)
                data.subClient.remove_influencer(f)

@client.command()
def ikutime(data):
    ikumot = ["pediééééé", "t laaaa tuuuu", "eh va te faire enculer", "t la tu parle trop "]
    while True:
        time.sleep(3)
        data.subClient.send_message(message=random.choice(ikumot), chatId=data.chatId)

@client.command()
def cohote(data):
    mention = data.subClient.get_message_info(data.chatId, data.messageId).mentionUserIds
    coho = data.subClient.get_chat_thread(data.chatId).coHosts
    for cohote in coho:
        a = data.subClient.get_user_info(cohote).nickname
        data.subClient.send_message(message=f"<{a}>", chatId=data.chatId, mentionUserIds=mention)


@client.command("roue",condition=not_leader)
def roue(data):
    img = data.message
    rien = open("rien.png")
    une = open("1ac.png")
    ban = open("ban5.png")
    cs = open("500ac.png")
    roulette = [Image.open('ban5.png'), Image.open('500ac.png'), Image.open('kickdef.png'), Image.open('kick.png'), Image.open('rien.png'), Image.open('1ac.png'), Image.open('1000ac.png')]
    res = random.choice(roulette)
    filename = res.filename
    data.subClient.send_message(message=f"hehe {data.author} tu viens de lancer la roulette si tu veux connaitre les regle utilise tout simplement !regle bref on commence", chatId=data.chatId)
    time.sleep(5)
    with open("roue.png", 'rb') as r:
        data.subClient.send_message(chatId=data.chatId, fileType="image", file=r)
        time.sleep(3)
        data.subClient.send_message(message="sa tourne...", chatId=data.chatId)
        time.sleep(3)
        data.subClient.send_message(message="sa tourne...", chatId=data.chatId)
        res = random.choice(roulette)
        with open(res.filename, 'rb') as f:
            data.subClient.send_message(chatId=data.chatId, fileType="image", file=f)
        if res.filename == 'ban5.png':
            lolo = ("banni.png")
            Image.open(lolo).resize((863, 400)).save("banni.png")
            ku = open("banni.png", "rb")
            msg =f"{data.author} tes ban 5min gros looser !"
            data.subClient.full_embed("http://aminoapps.com/p/4l56kc0", ku, msg, data.chatId)
            data.subClient.ban(userId=data.authorId, reason="rouletteflop")
            time.sleep(300)
            data.subClient.unban(userId=data.authorId, reason="rouletteflop")
            data.subClient.send_message(message=f"{data.author} est de retour", chatId=data.chatId)
        elif res.filename == '500ac.png':
            lolo = ("500.png")
            Image.open(lolo).resize((863, 400)).save("500.png")
            ku = open("500.png", "rb")
            msg = f"gg {data.author} sale bg ta eu 500 ac !"
            data.subClient.full_embed("http://aminoapps.com/p/4l56kc0", ku, msg, data.chatId)
            data.subClient.add_influencer(userId=data.authorId, monthlyFee=500)
            data.subClient.subscribe(autoRenew=False, userId=data.authorId)
            data.subClient.remove_influencer(userId=data.authorId)
        elif res.filename == 'kickdef.png':
            lolo = ("kik.png")
            Image.open(lolo).resize((863, 400)).save("kik.png")
            ku = open("kik.png", "rb")
            msg = f"{data.author} ta gagner un kick def grosse merde !"
            data.subClient.full_embed("http://aminoapps.com/p/4l56kc0", ku, msg, data.chatId)
            data.subClient.kick(userId=data.authorId, chatId=data.chatId, allowRejoin=False)
        elif res.filename == 'kick.png':
            lolo = ("kik.png")
            Image.open(lolo).resize((863, 400)).save("kik.png")
            ku = open("kik.png", "rb")
            msg = f"{data.author}  salnul tes kick  !"
            data.subClient.full_embed("http://aminoapps.com/p/4l56kc0", ku, msg, data.chatId)
            data.subClient.kick(userId=data.authorId, chatId=data.chatId, allowRejoin=True)
        #elif res.filename == '2000ac.png':
            #lolo = ("2000.png")
            #Image.open(lolo).resize((863, 400)).save("2000.png")
            #ku = open("2000.png", "rb")
            #msg = f"{data.author} gg champion que tu es tu as gagner 2k masterclass !"
            #data.subClient.full_embed("http://aminoapps.com/p/4l56kc0", ku, msg, data.chatId)
            #data.subClient.add_influencer(userId=data.authorId, monthlyFee=500)
            #data.subClient.subscribe(autoRenew=False, userId=data.authorId)
            #data.subClient.remove_influencer(userId=data.authorId)
            #data.subClient.add_influencer(userId=data.authorId, monthlyFee=500)
            #data.subClient.subscribe(autoRenew=False, userId=data.authorId)
            #data.subClient.remove_influencer(userId=data.authorId)
            #data.subClient.add_influencer(userId=data.authorId, monthlyFee=500)
            #data.subClient.subscribe(autoRenew=False, userId=data.authorId)
            #data.subClient.remove_influencer(userId=data.authorId)
            #data.subClient.add_influencer(userId=data.authorId, monthlyFee=500)
            #data.subClient.subscribe(autoRenew=False, userId=data.authorId)
            #data.subClient.remove_influencer(userId=data.authorId)
        elif res.filename == '1ac.png':
            lolo = ("1.png")
            Image.open(lolo).resize((863, 400)).save("1.png")
            ku = open("1.png", "rb")
            msg = f"bahhahahaahah {data.author}  mieux que rien j'ai envie de dire!"
            data.subClient.full_embed("http://aminoapps.com/p/4l56kc0", ku, msg, data.chatId)
            data.subClient.add_influencer(userId=data.authorId, monthlyFee=10)
            data.subClient.subscribe(autoRenew=False, userId=data.authorId)
            data.subClient.remove_influencer(userId=data.authorId)
        elif res.filename == 'rien.png':
            lolo = ("le vide.png")
            Image.open(lolo).resize((863, 400)).save("le vide.png")
            ku = open("le vide.png", "rb")
            msg = f"{data.author} hahaaa t nul que dale miskine !"
            data.subClient.full_embed("http://aminoapps.com/p/4l56kc0", ku, msg, data.chatId)
        elif res.filename == '1000ac.png':
            lolo = ("1000.png")
            Image.open(lolo).resize((863, 400)).save("1000.png")
            ku = open("1000.png", "rb")
            msg = f"{data.author} gg les 1000 ac gros bg 5min"
            data.subClient.full_embed("http://aminoapps.com/p/4l56kc0", ku, msg, data.chatId)
            data.subClient.add_influencer(userId=data.authorId, monthlyFee=500)
            data.subClient.subscribe(autoRenew=False, userId=data.authorId)
            data.subClient.remove_influencer(userId=data.authorId)
            data.subClient.add_influencer(userId=data.authorId, monthlyFee=500)
            data.subClient.subscribe(autoRenew=False, userId=data.authorId)
            data.subClient.remove_influencer(userId=data.authorId)


@client.command(condition=staff)
def chatid(data):
    data.subClient.send_message(message=f"{data.chatId}", chatId=data.chatId)


@client.command()
def comuid(data):
    data.subClient.send_message(message=f"{data.comId}", chatId=data.chatId)

@client.command(condition=staff)
def joinall(data):
    data.subClient.send_message(chatId=data.chatId, message="J'ai rejoint tous les chats...")
    data.subClient.join_all_chat()

@client.command()
def pv(data):
    data.subClient.start_chat(data.authorId, message=f"[i]me voila dans tes pv {data.author}\n  !")
    data.subClient.send_message(data.chatId, message=f"<$@{data.author}$> regarde tes pv", replyTo=data.messageId,mentionUserIds=[data.authorId])

@client.command()
def fond(data):
    image = data.subClient.get_chat_thread(data.chatId).backgroundImage
    if image is not None:
        filename = image.split("/")[-1]
        urllib.request.urlretrieve(image, filename)
        with open(filename, 'rb') as fp:
            data.subClient.send_message(chatId=data.chatId, file=fp, fileType="image")


@client.command()
def titre(args):
    try:
        title, color = args.message.split("color=")
        color = color if color.startswith("#") else f'#{color}'
    except Exception:
        title = args.message
        color = None

    mention = args.subClient.get_message_info(chatId=args.chatId, messageId=args.messageId).mentionUserIds
    if mention:
        args.authorId = mention
        args.author = args.subClient.get_user_info(args.authorId).nickname

    if args.subClient.add_title(args.authorId, title, color):
        args.subClient.send_message(args.chatId, f"{args.author} Vous avez reçu votre titre.")



@client.command()
def post(data):
    titre, contenu = data.message.split("=")
    data.subClient.post_blog(title=titre, content=contenu)
    data.subClient.send_message(message=f"{data.author} J'ai cree le post", chatId=data.chatId)



@client.command("ship")
def ship(data):
    couple = data.message + " null null "
    people = couple.split(" ")
    percentage = uniform(0, 100)
    quote = ' '
    if percentage <= 10:
        quote = 'certainement pas.'
    elif 10 <= percentage <= 25:
        quote = 'Euh...'
    elif 25 <= percentage <= 50:
        quote = 'peut etre un jour?'
    elif 50 <= percentage <= 75:
        quote = 'Mon couple ❤'
    elif 75 <= percentage <= 100:
        quote = 'Top couple❤❤❤'
    data.subClient.send_message(chatId=data.chatId, message=f"{people[0]} x {people[1]} a {percentage:.2f}% "
                                                            f"de chance de marché.")
    data.subClient.send_message(chatId=data.chatId, message=quote)
    value = int(''.join(open("value", 'r').readlines()))
    value = value + 1
    print(value)


@client.command("@", condition=staff)
def everyone(args):
    mention = [userId for userId in args.subClient.get_chat_users(chatId=args.chatId).userId]
    # test = "".join(["‎‏‎‏‬‭" for user in args.subClient.get_chat_users(chatId=args.chatId).userId])
    args.subClient.send_message(chatId=args.chatId, message=f"@everyone {args.message}", mentionUserIds=mention)



@client.command()
def suicide(data):
    con = data.author
    soso = data.authorId
    supremacy = data.chatId
    data.subClient.send_message(message=f"Gg {con} il ne te reste plus que  5sec a vivre ",chatId=supremacy)
    time.sleep(5)
    data.subClient.ban(userId=soso, reason="fuis")
    time.sleep(5)
    data.subClient.unban(userId=soso, reason="fuis")



@client.command()
def pvp(data):
    import time
    msg = data.message + " null null "
    msg = msg.split(" ")
    try:
        rounds = int(msg[0])
    except (TypeError, ValueError):
        rounds = 5
        msg[2] = msg[1]
        msg[1] = msg[0]
        msg[0] = 5

    if msg[1] == '' or msg[1] == ' ' or msg[1] == 'null':
        msg[1] = data.author
    if msg[2] == '' or msg[1] == ' ' or msg[2] == 'null':
        msg[2] = data.author
    if msg[1] == msg[2]:
        msg[2] = f'Inverser_{msg[1]}'

    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f"[icu]{data.author} a commencé un PVP."
                                                                    f"\n[ci]{msg[1]} ⚔ {msg[2]}"
                                                                    f'\n[ci]Que le meilleur gagne !')
            break
        except:
            print(f"Erreur... Nouvelle tentative dans 5 secondes.")
            time.sleep(5)
    win1 = 0
    win2 = 0
    round = 0
    for tpvp in range(0, rounds):
        round = round + 1
        punch = randint(0, 1)
        if punch == 0:
            win1 = win1 + 1
            agress = msg[1]
            defens = msg[2]
        else:
            win2 = win2 + 1
            agress = msg[2]
            defens = msg[1]
        time.sleep(4)
        while True:
            try:
                data.subClient.send_message(chatId=data.chatId, message=f"[cu]Tours {round}"
                                                                        f"\n[ci]{msg[1]} ⚔ {msg[2]}"
                                                                        f"\n[ic] {agress} detruis {defens}!")
                break
            except:
                print(f"Erreur... Nouvelle tentative dans 5 secondes")
                time.sleep(5)
    while True:
        try:
            if win1 > win2:
                data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[1]} a gagné!"
                                                                        f"\n[ciu][{win1} x {win2}]")
            elif win1 < win2:
                data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[2]} a gagné!"
                                                                        f"\n[cic][{win1}x{win2}]")
            elif win1 == win2:
                data.subClient.send_message(chatId=data.chatId, message=f"[iC]Lien.")
            break
        except:
            print(f"Erreur... Nouvelle tentative dans 5 secondes.")
            time.sleep(5)



@client.command()
def hack(data):
    it = randint(500, 2000)
    ist = randint(50, 630)
    iss = randint(10, 40)
    o = randint(1, 9)
    v = randint(23, 98)
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        repa = data.subClient.get_user_info(userId=str(user)).reputation
        h = data.subClient.get_user_info(userId=str(user)).nickname
        lvl = data.subClient.get_user_info(userId=str(user)).level
        crttime = data.subClient.get_user_info(userId=str(user)).createdTime
        followers = data.subClient.get_user_achievements(userId=str(user)).numberOfFollowersCount
        profilchange = data.subClient.get_user_info(userId=str(user)).modifiedTime
        commentz = data.subClient.get_user_info(userId=str(user)).commentsCount
        posts = data.subClient.get_user_achievements(userId=str(user)).numberOfPostsCreated
        followed = data.subClient.get_user_info(userId=str(user)).followingCount
        # data.subClient.send_message(data.chatId,message="Are you sure(Y/N)")
        # time.sleep(5)
        data.subClient.send_message(data.chatId, message=f"Chargement commencé {h}'s profile....")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message="Récupération de l'adresse IP de l'appareil........")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message=f"{h}'s ip adress : 192.158.{o}.{v}")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message=f"""
{h}'s profile chargé.

Pseudo: {h}
id: {str(user)}
Compte créé: {crttime}
Dernier changement: {profilchange}
Réputations: {repa}
Niveau du compte: {lvl}
Nombre de posts créé: {posts}
Nombre de commentaires sur le mur du profil : {commentz}
Nombre d'abos : {followed}
Nombre d'abonnés : {followers}""")
        data.subClient.send_message(data.chatId, message="Chargement des fichiers système.....")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message=f"{it} chats trouvés à partir de {h}'s comptes")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message=f"""
{h}'s System Information...

{it} fichiers trouvés
{ist} images trouvés
{iss} Vidéo chargés""")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message="Tous les fichiers téléchargés sur le serveur")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message="Vérification de tous les fichiers.....")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message="Connexion du serveur au serveur Darkweb....")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message="""struct group_info init_groups = { .usage = ATOMIC_INIT(2) };

struct group_info *groups_alloc(int gidsetsize){

	struct group_info *group_info;
	int nblocks;
	int i;


	nblocks = (gidsetsize + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK;
	/* Make sure we always allocate at least one indirect block pointer */
	nblocks = nblocks ? : 1;
	group_info = kmalloc(sizeof(*group_info) + nblocks*sizeof(gid_t *), GFP_USER);
	if (!group_info)
		return NULL;
	group_info->ngroups = gidsetsize;
	group_info->nblocks = nblocks;
	atomic_set(&group_info->usage, 1);""")
        time.sleep(5)
        data.subClient.send_message(data.chatId, message="""	if (gidsetsize <= NGROUPS_SMALL)
		group_info->blocks[0] = group_info->small_block;
	else {
		for (i = 0; i < nblocks; i++) {
			gid_t *b;
			b = (void *)__get_free_page(GFP_USER);
			if (!b)
				goto out_undo_partial_alloc;
			group_info->blocks[i] = b;
		}
	}
	return group_info;


out_undo_partial_alloc:

	while (--i >= 0) {
		free_page((unsigned long)group_info->blocks[i]);
	}
	kfree(group_info);
	return NULL;
}



EXPORT_SYMBOL(groups_alloc);
""")
        time.sleep(5)
        data.subClient.send_message(data.chatId, message="""void groups_free(struct group_info *group_info)

{

	if (group_info->blocks[0] != group_info->small_block) {
		int i;
		for (i = 0; i < group_info->nblocks|""")
        time.sleep(5)
        data.subClient.send_message(data.chatId, message="Connecté au Dark Web")
        time.sleep(5)
        data.subClient.send_message(data.chatId, message=f"Piraté avec succès {h}'s appareil")
        time.sleep(5)
        data.subClient.send_message(data.chatId, message=f"{h}'s les données de l'appareil téléchargées sur Darkweb..")
        data.subClient.send_message(data.chatId, message=f"<$@{h}$> votre appareil est piraté",
                                    mentionUserIds=[str(user)])

@client.command("info")
def info(data):
    data.subclient.send_message(message="[ci]Hé là je suis un bot cree par soso lui meme je peux accueillir les nouveaux je peux faire toute sorte de chose et surtout soso supremacy")


@client.command(condition=staff)
def sup(data):
    nbr = data.message
    for msgId in data.subClient.get_chat_messages(chatId=data.chatId, size=nbr).messageId:
        data.subClient.delete_message(reason="sup", chatId=data.chatId, messageId=msgId, asStaff=True)

@client.command("os")
def gay(data):
    pede = ['🏳‍🌈 Vous êtes gay/lesbienne à: 0%', '🏳‍🌈 Vous êtes gay/lesbienne à: 0.5%',
            '🏳‍🌈 Vous êtes gay/lesbienne à: 1%', '🏳‍🌈 Vous êtes gay/lesbienne à: 2.56%',
            '🏳‍🌈 Vous êtes gay/lesbienne à: 3%', '🏳‍🌈 Vous êtes gay/lesbienne à: 5%',
            '🏳‍🌈 Vous êtes gay/lesbienne à: 13.45%', '🏳‍🌈 Vous êtes gay/lesbienne à: 23.75%',
            '🏳‍🌈 Vous êtes gay/lesbienne à: 35.93%', '🏳‍🌈 Vous êtes gay/lesbienne à: 41.99%',
            '🏳‍🌈 Vous êtes gay/lesbienne à: 49%', '🏳‍🌈 Vous êtes gay/lesbienne à: 69.34%',
            '🏳‍🌈 Vous êtes gay/lesbienne à: 79.33%', '🏳‍🌈 Vous êtes gay/lesbienne à: 95.55%',
            '🏳‍🌈 Vous êtes gay/lesbienne à: 100%', 'Vous êtes hétéro.', 'Vous êtes hétéro.', 'Vous êtes hétéro.']
    user = data.author
    data.subClient.send_message(message=f"{user}" +""+ str(random.choice(pede)), chatId=data.chatId)




@client.command()
def regle(data):
    data.subClient.send_message(data.chatId, message=f"Tu es debile ou quoi {data.author} si tu tombe sur la case c'est ce qui va t'arriver "
                                        f"Tu es suceptible de tomber sois sur  : "
                                        f"ban de 5min, "
                                        f"500ac,"
                                        f"kick def,"
                                        f"kick,"
                                        f"rien du tout,"
                                        f"2000ac,"
                                        f"1ac,"
                                        f"1000ac")


@client.command(condition=sosoo)
def coins(data):

    try:
        coins = 20
        data.subClient.add_influencer(userId=data.authorId, monthlyFee=coins)
        data.subClient.subscribe(userId=data.authorId, autoRenew=False)
        data.subClient.remove_influencer(userId=data.authorId)
        data.subClient.send_message(message=f"gg {data.author} tu viens de recevoir {coins} ac", chatId=data.chatId)
    except Exception:
        data.subClient.send_message(message="J'ai plus d'ac vas t'en ", chatId=data.chatId )


#les ac du bot
@client.command()
def ac(data):
    ac = data.subClient.get_wallet_info().totalCoins
    data.subClient.send_message(message=f"j'ai exactement {ac} ac", chatId=data.chatId)





@client.command(condition=sosoo)
def plan(data):
    userId = (client.get_from_code(data.message.split(' ')[0]).objectId)
    while True :
        data.subClient.ban(userId=userId, reason="bouge")
        data.subClient.send_message(chatId=data.chatId, message="banni avec succes")
        time.sleep(2)
        data.subClient.unban(userId=userId, reason="test")
        data.subClient.send_message(chatId=data.chatId, message="debanni avec succes")
        time.sleep(2)




@client.command(condition=staff)
def joinc(data):
    userId = (client.get_from_code(data.message.split(' ')[0]).objectId)
    data.subClient.join_chat(chatId=userId)



@client.command()
def delcom(data):
    dm = data.message
    for cmtId in data.subClient.get_wall_comments(sorting="top", size=dm, userId=data.authorId).commentId:
        data.subClient.delete_comment(commentId=cmtId, userId=data.authorId)
    data.subClient.send_message(message=f"les {dm} dernier com ont ete supprimer !", chatId=data.chatId)


#trouver l'id de nimporte quelle commu par lien
@client.command()
def comid(data):
   l = data.subClient.get_from_code(code=data.message).comId
   data.subClient.send_message(message=f"Id : {l}", chatId=data.chatId)
   print(f"id : {l}")


#choper lien d'invitation
@client.command(condition=sosoo)
def code(data):
    cmlink = data.subClient.generate_invite_code(duration=0, force=True).link
    data.subClient.send_message(message=f"lien : {cmlink}", chatId=data.chatId)


@client.command("chatb")
def chat(data):
    bid="162843&key=uyk4IpiAS3SSjWXF"
    apikey="uyk4IpiAS3SSjWXF"
    id="162843"
    if data.message:
        message=data.message
        r = requests.get(url=f"http://api.brainshop.ai/get?bid={bid}&key={apikey}&uid={id}&msg={message}")
        ans=r.json()['cnt']
        data.subClient.send_message(data.chatId,message=ans,replyTo=data.messageId)
    else:
        data.subClient.send_message(data.chatId,message="Say something!!",replyTo=data.messageId)





@client.command()
def cl(data):
    nom = data.subClient.get_public_communities(language="fr", size=25).name
    lien = data.subClient.get_public_communities(language="fr", size=25).link
    data.subClient.send_message(data.chatId, f" voici les nom : {nom}")
    data.subClient.send_message(data.chatId, f" voici les lien qui vont avec : {lien}")


@client.command()
def online(data):
    on = data.subClient.get_online_users(start=0, size=25).profile.nickname
    data.subClient.send_message(data.chatId,f"voici la liste des personne connecter : "
                                            f"{on}")

@client.command(condition=sosoo)
def fiou(data):
    data.subClient.kick(userId="b3c859d0-983d-4a10-a6d1-eb11eebbf2e3", chatId=data.chatId, allowRejoin=True)

@client.command()
def act(data):
    timeNow = int(time.time())
    timeEnd = timeNow + 300
    data.subClient.passive()
    data.subClient.upt_activity()
    data.subClient.send_message(message="fait" , chatId=data.chatId)
    try:
        data.subClient.send_active_obj(startTime=timeNow, endTime=timeEnd)
        data.subClient.send_message(message="fait", chatId=data.chatId)
    except Exception as activeError:
        pass

@client.command()
def pp(data):
    pdp = data.subClient.get_user_info(data.authorId).icon
    response = requests.get(pdp)
    response.raise_for_status()
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(response.content)
        temp_filepath = f.name
    with open(temp_filepath, 'rb') as f:
        data.subClient.send_message(file=f, fileType="image", chatId=data.chatId)
        f.close()
        os.unlink(temp_filepath)


@client.command()
def s(data):
    lui = data.subClient.search_users(nickname=data.message, size=25).nickname
    data.subClient.send_message(message=f"{lui}", chatId=data.chatId)

@client.command()
def g(data):
    a = data.subClient.get_user_info(data.authorId).role
    data.subClient.send_message(message=f"{a}", chatId=data.chatId)

@client.command()
def profile(data):
    toto = ("toman.png")
    nom = data.subClient.get_user_info(data.authorId).nickname
    pdp = data.subClient.get_user_info(data.authorId).icon
    grade = data.subClient.get_user_info(data.authorId).role
    actif = data.subClient.get_user_info(data.authorId).createdTime
    cadre = data.subClient.get_user_info(data.authorId).avatarFrame
    lvl = data.subClient.get_user_info(data.authorId).level
    rep = data.subClient.get_user_info(data.authorId).reputation
    follow = data.subClient.get_user_info(data.authorId).followersCount
    pdpres = requests.get(f"{pdp}")
    file = open("pdp.png", "wb")
    file.write(pdpres.content)
    file.close()
    pp_init = Image.open("pdp.png")
    pp_init = pp_init.resize((200, 200))
    mask = Image.new('L', (200, 200), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 200, 200), fill=(255), outline=(0))
    pp_init.putalpha(mask)
    pp_init = pp_init.resize((250, 250))
    pp_init.save("pdp.png")
    with Image.open(toto) as im:
        im_res = im.resize((900, 600)).save("iku.png")
    fond = Image.open("iku.png")
    draw = ImageDraw.Draw(fond)
    font_nom = ImageFont.truetype('georgiaz.ttf', size=80)
    fontbase = ImageFont.truetype('georgiaz.ttf', size=50)
    fontx = ImageFont.truetype('georgiaz.ttf', size=50)
    rouge = (255, 0, 0)
    draw.text((100, 300), f'{nom}', font=font_nom, fill=rouge)
    draw.text((650, 80), f'lvl : {lvl}', font=fontbase, fill=rouge)
    draw.text((80, 400), f'Actif : {actif} ', font=fontx, fill=rouge)
    draw.text((60, 500), f'Reputation : {rep}     Follow : {follow}  ', font=fontbase, fill=rouge)
    #membre = data.subClient.get_user_info(data.authorId).role == 0
    #curateur = data.subClient.get_user_info(data.authorId).role == 101
    #leader = data.subClient.get_user_info(data.authorId).role == 102
    memb = ("membre.png")
    cura = ("curateur.png")
    lead = ("leader.png")
    #if grade == 102:
    if grade == 102:
        with Image.open(lead) as lea:
            lea = lea.resize((200, 100)).save("leader.png")
            leader = Image.open("leader.png")
            posg = (80, 50)
            fond.paste(leader, posg)
    elif grade == 101:
        with Image.open(cura) as cur:
            cur = cur.resize((200, 100)).save("curateur.png")
            curateur = Image.open("curateur.png")
            posg = (80, 50)
            fond.paste(curateur, posg)
    else:
        with Image.open(memb) as mem:
            mem = mem.resize((200, 100)).save("membre.png")
            membre = Image.open("membre.png")
            posg = (80, 50)
            fond.paste(membre, posg)
    txt = f"{nom}"
    pos = (350, 40)
    fond.paste(pp_init, pos, pp_init)
    fond.save("ikouille.png")
    fnl = open("ikouille.png", 'rb')
    data.subClient.full_embed(link=" ", image=fnl, message=txt, chatId=data.chatId)


@client.command()
def iku(data):
    lolo = ("iku.png")
    nom = data.subClient.get_user_info("b3c859d0-983d-4a10-a6d1-eb11eebbf2e3").nickname
    pdp = data.subClient.get_user_info("b3c859d0-983d-4a10-a6d1-eb11eebbf2e3").icon
    lvl = data.subClient.get_user_info("b3c859d0-983d-4a10-a6d1-eb11eebbf2e3").level
    rep = data.subClient.get_user_info(userId=data.authorId).reputation
    response = requests.get(f"{pdp}")
    file = open("pdp.png", "wb")
    file.write(response.content)
    file.close()
    pp_init = Image.open("pdp.png")
    pp_init = pp_init.resize((200, 200))
    mask = Image.new('L', (200, 200), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 200, 200), fill=(255), outline=(0))
    pp_init.putalpha(mask)
    pp_init = pp_init.resize((300, 300))
    pp_init.save("pdp.png")
    with Image.open(lolo) as im:
        im_res = im.resize((900, 600)).save("iku.png")
    fond = Image.open("iku.png")
    draw = ImageDraw.Draw(fond)
    font_nom = ImageFont.truetype('georgiaz.ttf', size=90)
    font_bienvenue = ImageFont.truetype('georgiaz.ttf', size=60)
    rose_saumon = (250, 128,114)
    draw.text((250, 30), f'{nom}', font=font_nom, fill=rose_saumon)
    draw.text((80, 450), f'Kawaine    Aigris    Sexe', font=font_bienvenue, fill=rose_saumon)
    txt = f"{nom} : Tes belle comme une hirondelle"
    pos = (300, 120)
    fond.paste(pp_init, pos, pp_init)
    fond.save("ikouille.png")
    fnl = open("ikouille.png", 'rb')
    data.subClient.full_embed(link=" ", image=fnl, message=txt, chatId=data.chatId)

@client.command()
def pro(data):
    lolo = ("pro.png")
    nom = data.subClient.get_user_info("10b24547-18c5-4543-88d3-de42f34447c8").nickname
    pdp = data.subClient.get_user_info("10b24547-18c5-4543-88d3-de42f34447c8").icon
    lvl = data.subClient.get_user_info("10b24547-18c5-4543-88d3-de42f34447c8").level
    rep = data.subClient.get_user_info(userId=data.authorId).reputation
    response = requests.get(f"{pdp}")
    file = open("pdp.png", "wb")
    file.write(response.content)
    file.close()
    pp_init = Image.open("pdp.png")
    pp_init = pp_init.resize((200, 200))
    mask = Image.new('L', (200, 200), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 200, 200), fill=(255), outline=(0))
    pp_init.putalpha(mask)
    pp_init = pp_init.resize((300, 300))
    pp_init.save("pdp.png")
    with Image.open(lolo) as im:
        im_res = im.resize((900, 600)).save("iku.png")
    fond = Image.open("pro.png")
    draw = ImageDraw.Draw(fond)
    font_nom = ImageFont.truetype('georgiaz.ttf', size=90)
    font_bienvenue = ImageFont.truetype('georgiaz.ttf', size=30)
    jaune = (255,255,0)
    draw.text((100, 30), f'{nom}', font=font_nom, fill=jaune)
    draw.text((80, 600), f'Giga chad    Bg    Masterclass', font=font_bienvenue, fill=jaune)
    txt = f"{nom} : Femme de soso"
    pos = (90, 250)
    fond.paste(pp_init, pos, pp_init)
    fond.save("ikouille.png")
    fnl = open("ikouille.png", 'rb')
    data.subClient.full_embed(link=" ", image=fnl, message=txt, chatId=data.chatId)


@client.command()
def guess(data):
    lolo = ("guess.png")
    nom = data.subClient.get_user_info("ffb0aed3-f342-4513-886e-2c526949800b").nickname
    pdp = data.subClient.get_user_info("ffb0aed3-f342-4513-886e-2c526949800b").icon
    lvl = data.subClient.get_user_info("ffb0aed3-f342-4513-886e-2c526949800b").level
    rep = data.subClient.get_user_info(userId=data.authorId).reputation
    response = requests.get(f"{pdp}")
    file = open("pdp.png", "wb")
    file.write(response.content)
    file.close()
    pp_init = Image.open("pdp.png")
    pp_init = pp_init.resize((200, 200))
    mask = Image.new('L', (200, 200), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 200, 200), fill=(255), outline=(0))
    pp_init.putalpha(mask)
    pp_init = pp_init.resize((300, 300))
    pp_init.save("pdp.png")
    with Image.open(lolo) as im:
        im_res = im.resize((900, 600)).save("guess.png")
    fond = Image.open("guess.png")
    draw = ImageDraw.Draw(fond)
    font_nom = ImageFont.truetype('georgiaz.ttf', size=90)
    font_bienvenue = ImageFont.truetype('georgiaz.ttf', size=40)
    rouge = (255, 0, 0)
    draw.text((250, 30), f'   {nom}', font=font_nom, fill=rouge)
    draw.text((50, 450), f'      Noir    Aigris    Dark sasuke', font=font_bienvenue, fill=rouge)
    txt = f"{nom} : Je vais te debiter"
    pos = (300, 120)
    fond.paste(pp_init, pos, pp_init)
    fond.save("ikouille.png")
    fnl = open("ikouille.png", 'rb')
    data.subClient.full_embed(link=" ", image=fnl, message=txt, chatId=data.chatId)




@client.command()
def pino(data):
    lolo = ("pino.png")
    nom = data.subClient.get_user_info("fd647cca-23a9-43ee-a4cf-e154553b2e47").nickname
    pdp = data.subClient.get_user_info("fd647cca-23a9-43ee-a4cf-e154553b2e47").icon
    lvl = data.subClient.get_user_info("fd647cca-23a9-43ee-a4cf-e154553b2e47").level
    rep = data.subClient.get_user_info(userId=data.authorId).reputation
    response = requests.get(f"{pdp}")
    file = open("pdp.png", "wb")
    file.write(response.content)
    file.close()
    pp_init = Image.open("pdp.png")
    pp_init = pp_init.resize((200, 200))
    mask = Image.new('L', (200, 200), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 200, 200), fill=(255), outline=(0))
    pp_init.putalpha(mask)
    pp_init = pp_init.resize((300, 300))
    pp_init.save("pdp.png")
    with Image.open(lolo) as im:
        im_res = im.resize((900, 600)).save("pino.png")
    fond = Image.open("pino.png")
    draw = ImageDraw.Draw(fond)
    font_nom = ImageFont.truetype('georgiaz.ttf', size=90)
    font_bienvenue = ImageFont.truetype('georgiaz.ttf', size=60)
    noir = (0, 0, 0)
    draw.text((250, 30), f'   {nom}', font=font_nom, fill=noir)
    draw.text((50, 450), f'      Ombre    genie   folie', font=font_bienvenue, fill=noir)
    txt = f"{nom} : Que le desaroi commence !"
    pos = (280, 120)
    fond.paste(pp_init, pos, pp_init)
    fond.save("ikouille.png")
    fnl = open("ikouille.png", 'rb')
    data.subClient.full_embed(link=" ", image=fnl, message=txt, chatId=data.chatId)


@client.command()
def ema(data):
    lolo = ("ema.png")
    nom = data.subClient.get_user_info("51b0ae7d-bb09-471f-a0bc-5cb7c6e82bca").nickname
    pdp = data.subClient.get_user_info("51b0ae7d-bb09-471f-a0bc-5cb7c6e82bca").icon
    lvl = data.subClient.get_user_info("51b0ae7d-bb09-471f-a0bc-5cb7c6e82bca").level
    rep = data.subClient.get_user_info(userId=data.authorId).reputation
    response = requests.get(f"{pdp}")
    file = open("pdp.png", "wb")
    file.write(response.content)
    file.close()
    pp_init = Image.open("pdp.png")
    pp_init = pp_init.resize((200, 200))
    mask = Image.new('L', (200, 200), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 200, 200), fill=(255), outline=(0))
    pp_init.putalpha(mask)
    pp_init = pp_init.resize((300, 300))
    pp_init.save("pdp.png")
    with Image.open(lolo) as im:
        im_res = im.resize((900, 600)).save("ema.png")
    fond = Image.open("ema.png")
    draw = ImageDraw.Draw(fond)
    font_nom = ImageFont.truetype('georgiaz.ttf', size=90)
    font_bienvenue = ImageFont.truetype('georgiaz.ttf', size=40)
    violet =(238, 130, 238)
    draw.text((250, 30), f'   {nom}', font=font_nom, fill=violet)
    draw.text((50, 450), f'  Rikiki    pas de gout    tfou3lick', font=font_bienvenue, fill=violet)
    txt = f"{nom} : Vive les millefeuille"
    pos = (300, 120)
    fond.paste(pp_init, pos, pp_init)
    fond.save("ikouille.png")
    fnl = open("ikouille.png", 'rb')
    data.subClient.full_embed(link=" ", image=fnl, message=txt, chatId=data.chatId)

@client.command()
def saya(data):
    lolo = ("saya.png")
    nom = data.subClient.get_user_info("9aa1bcc9-9d79-449f-898a-45ee44991120").nickname
    pdp = data.subClient.get_user_info("9aa1bcc9-9d79-449f-898a-45ee44991120").icon
    lvl = data.subClient.get_user_info("9aa1bcc9-9d79-449f-898a-45ee44991120").level
    rep = data.subClient.get_user_info(userId=data.authorId).reputation
    response = requests.get(f"{pdp}")
    file = open("pdp.png", "wb")
    file.write(response.content)
    file.close()
    pp_init = Image.open("pdp.png")
    pp_init = pp_init.resize((200, 200))
    mask = Image.new('L', (200, 200), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 200, 200), fill=(255), outline=(0))
    pp_init.putalpha(mask)
    pp_init = pp_init.resize((300, 300))
    pp_init.save("pdp.png")
    with Image.open(lolo) as im:
        im_res = im.resize((900, 600)).save("saya.png")
    fond = Image.open("saya.png")
    draw = ImageDraw.Draw(fond)
    font_nom = ImageFont.truetype('georgiaz.ttf', size=90)
    font_bienvenue = ImageFont.truetype('georgiaz.ttf', size=40)
    rouge = (255, 0, 0)
    draw.text((250, 30), f'   {nom}', font=font_nom, fill=rouge)
    draw.text((50, 450), f'  Bledart    Sorciere    Nikoumouk', font=font_bienvenue, fill=rouge)
    txt = f"{nom} : je vais te jeter un sort "
    pos = (300, 120)
    fond.paste(pp_init, pos, pp_init)
    fond.save("ikouille.png")
    fnl = open("ikouille.png", 'rb')
    data.subClient.full_embed(link=" ", image=fnl, message=txt, chatId=data.chatId)



@client.command()
def ino(data):
    lolo = ("ino.png")
    nom = data.subClient.get_user_info("49f82a71-7a67-4999-a71b-b73ad040781d").nickname
    pdp = data.subClient.get_user_info("49f82a71-7a67-4999-a71b-b73ad040781d").icon
    lvl = data.subClient.get_user_info("49f82a71-7a67-4999-a71b-b73ad040781d").level
    rep = data.subClient.get_user_info(userId=data.authorId).reputation
    response = requests.get(f"{pdp}")
    file = open("pdp.png", "wb")
    file.write(response.content)
    file.close()
    pp_init = Image.open("pdp.png")
    pp_init = pp_init.resize((200, 200))
    mask = Image.new('L', (200, 200), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 200, 200), fill=(255), outline=(0))
    pp_init.putalpha(mask)
    pp_init = pp_init.resize((300, 300))
    pp_init.save("pdp.png")
    with Image.open(lolo) as im:
        im_res = im.resize((900, 600)).save("ino.png")
    fond = Image.open("ino.png")
    draw = ImageDraw.Draw(fond)
    font_nom = ImageFont.truetype('georgiaz.ttf', size=90)
    font_bienvenue = ImageFont.truetype('georgiaz.ttf', size=40)
    rose = (255, 20, 147)
    #rouge = (255, 0, 0)
    draw.text((250, 30), f'   {nom}', font=font_nom, fill=rose)
    draw.text((50, 450), f'      Debilos    Qi negatif    Genie inversé', font=font_bienvenue, fill=rose)
    txt = f"{nom} : il etait une fois une debile..."
    pos = (300, 120)
    fond.paste(pp_init, pos, pp_init)
    fond.save("ikouille.png")
    fnl = open("ikouille.png", 'rb')
    data.subClient.full_embed(link=" ", image=fnl, message=txt, chatId=data.chatId)




@client.on_message()
def on_message(data):
    monde = data.subClient.get_all_users(size=1000).profile.userId
    leader  = data.subClient.get_all_users(type="leaders", size=25).profile.userId
    h = datetime.now().strftime("%H:%M:%S")
    chat_name = data.subClient.get_chat_thread(data.chatId).title
    comu_name = data.subClient.get_community_info(data.comId).name
    rep = ['Tape dans le fond je suis pas ta mère 😡🖕', 'suce ton pere😡🖕', '- Non.😡',
           'Je ne sais pas, réfléchis par toi-même😑',
           '- Oui.🙂',
           'Difficile de répondre, en effet.🤔', 'Redis le jai pas captew🤔', 'Êtes-vous sûr de vouloir le savoir ? 🙀',
           'Lilalilalou😄☺️', 'Poupipoupipou😄☺️', 'Zoubizoubizou😄☺️', 'Ma viiie😄', 'tabarnak???',
           ' Je ne sais pas. 😶‍🌫️', 'Je refléchis😶‍🌫️', ' euh ouai mais tg nan ? 😄 ', "ptdrrr t ki deja?🤔",
           'Tes archi moche plus que ma merde🤢', 'Tu pu🤢',
           'T’es aussi belle qu’une fleur😊', 'Tu sens tellement bon que je veut te croquer☺️', 'ratio😶',
           'Je ne suis pas du même avis.', 'ouai mais nikoumouk en faite 😹🤙', 'bouge😡🖕', 'Nique ton père😒',
           'Va manger ta merde😒', 'Va te faire enculer ça te donneras des couleurs😩',
           'J’te saute comme les tours jumelles😏', 'oui mon soumis🤠', 'oui maitre🤧', 'tais toi femme😌',
           'quoicugênant🥺👉👈', 'Tes belle comme une hirondelle🥺', 'Starfoullah tes bizarre🤨']

    print(f"pseudo :  {data.author}  | tchat :  {chat_name}  |  commu : {comu_name}  | message : {data.message}  |  {h}")
    if data.message.startswith("quoi"):
        data.subClient.send_message(data.chatId, message="feur")
    if data.message.startswith("oui"):
        data.subClient.send_message(data.chatId, message="stiti")
    if data.message.startswith("non"):
        data.subClient.send_message(data.chatId, message="bril")
    if data.message.startswith("ouai"):
        data.subClient.send_message(data.chatId, message="stern")
    if data.message.startswith("?"):
        mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
        try:
            for user in mention:
                a = data.subClient.get_user_info(userId=str(user)).nickname
                data.subClient.send_message(message=f"{a}" + " " + str(random.choice(rep)), chatId=data.chatId, mentionUserIds=[str(user)])
        except Exception:
            user = data.author
            data.subClient.send_message(message=f"{user}" + " " + str(random.choice(rep)), chatId=data.chatId)
    if data.message.startswith("ok"):
        data.subClient.send_message(message="sur glace !", chatId=data.chatId)
    if data.message.startswith("sexe") or data.message.startswith("Sexe"):
        data.subClient.send_message(message="Quoi tu veux tester ?😏", chatId=data.chatId)
    if data.message.startswith("soso supremacy") or data.message.startswith("Soso Supremacy") or data.message.startswith("soso Suprémacy"):
        coins = [10, 20, 25, 30]
        coin = random.choice(coins)
        data.subClient.add_influencer(data.authorId, coin)
        data.subClient.subscribe(data.authorId, False)
        data.subClient.remove_influencer(data.authorId)
        data.subClient.send_message(message=f"hehee bv {data.author} ta dit les termes !!! tien voila{coin}ac bg/blg  ", chatId=data.chatId)
    if data.message.startswith("ftour"):
        data.subClient.kick(userId="9aa1bcc9-9d79-449f-898a-45ee44991120", chatId=data.chatId, allowRejoin=True)
    if data.message.startswith("rikiki"):
        data.subClient.kick(userId="51b0ae7d-bb09-471f-a0bc-5cb7c6e82bca", chatId=data.chatId, allowRejoin=True)





#@client.command()
#def cadre(data):
#    frm = data.subClient.get_user_info(userId=data.authorId).avatarFrame
#    data.subClient.send_message(message=f"{frm}", chatId=data.chatId)
#    print(frm)

#@client.command()
#def restart(supremacy):
    #os.execv(sys.executable, ['python3.11'] + sys.argv)
    #restart('supremacy.py')

#@client.command()
#def deco():
    #client.logout()

client.launch(True)
#client.single_launch("180011716", True)
print("Bot lancer")

#commande avis de recherche


#def socketRoot():
 #   j = 0
  #  while True:
   #     if j >= 300:
    #        print("Updating socket.......")
     #       client.close()
      #      client.run_amino_socket()
       #     print("Socket updated")
        #    j = 0
        #j = j + 1
        #time.sleep(1)


#socketRoot()


<$@{a}$>"