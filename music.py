from BotAmino import *
import io
import json 
from time import sleep
from functools import wraps
import requests
drivers = []
music_chat=[]

url=" #use ur own url from replit"

def checklive(data):
     return data.chatId in music_chat


client = BotAmino("")


def music_route(chatId=None,route=None,message=None):
     json_data={"chatId":chatId,"message":message}

     r=requests.get(f"{url}/{route}",json=json_data).text
     return r

@client.command("vc")
def vcc(data):
    
        client.start_vc(data.comId,data.chatId)
        sleep(3)
        client.send(json.dumps({"o":{"ndcId":data.comId,"threadId":data.chatId,"id":"337496"},"t":200}))


@client.command("end_vc")
def vcc(data):
    client.end_vc(data.comId,data.chatId)
    music_chat.remove(data.chatId)
    music_route(chatId=data.chatId,route="playlist_clear")



# Play command - starts playing music
@client.command("play")
def play_music(data):
    result = music_route(message=data.message,chatId= data.chatId,route="play")
    data.subClient.send_message(data.chatId, result, replyTo=data.messageId)

# Pause command - pauses the currently playing music
@client.command("pause")
def pause_music(data):
    music_route(data.chatId,"pause")

# Resume command - resumes the previously paused music
@client.command("resume")
def resume_music(data):
    music_route(data.chatId,"resume")

# Mute command - mutes the audio output
@client.command("mute")
def mute_audio(data):
    music_route(data.chatId,"mute")

# Add song command - adds a new song to the playlist
@client.command("add_song")
def add_new_song(data):
    result = music_route(message=data.message, chatId=data.chatId,route="add_song")
    data.subClient.send_message(data.chatId, message=result, replyTo=data.messageId)

# Next command - skips to the next song in the playlist
@client.command("next")
def skip_to_next_song(data):
    result = music_route(data.chatId,"next")
    data.subClient.send_message(data.chatId, message=result, replyTo=data.messageId)

# Previous command - goes back to the previous song in the playlist
@client.command("previous")
def go_to_previous_song(data):
    result = music_route(data.chatId,"previous")
    data.subClient.send_message(data.chatId, message=result, replyTo=data.messageId)

# Stop command - stops the playlist
@client.command("stop")
def stop_playlist(data):
    music_route(data.chatId,"stop")
    data.subClient.send_message(data.chatId, message="Playlist stopped", replyTo=data.messageId)

# Volume command - changes the volume of the audio output
@client.command("volume")
def change_volume(data):
    music_route(chatId=data.chatId,route="volume",message=data.message)


# Unmute command - unmutes the audio output
@client.command("unmute")
def unmute_audio(data):
    music_route(data.chatId,"unmute")




# Playlist command - displays the list of songs in the current playlist
@client.command("playlist")
def playlist(data):
     r=music_route(data.chatId,"playlist")
     data.subClient.send_message(data.chatId,message=r,replyTo=data.messageId)


@client.event("on_voice_chat_end")
def on_chat_(data):
    try:
        commuId = int(data.json["ndcId"])
        subClient = client.get_community(commuId)
    except Exception:
        return

    args = Parameters(data, subClient)
    if args.chatId in music_chat:
         music_route(args.chatId,"playlist_clear")
         music_chat.remove(args.chatId)

@client.event("on_screen_room_end")
def on_c_invi(data):
    try:
        commuId = int(data.json["ndcId"])
        subClient = client.get_community(commuId)
    except Exception:
        return

    args = Parameters(data, subClient)
    if args.chatId in music_chat:
         music_route(args.chatId,"playlist_clear")
         music_chat.remove(args.chatId)         



@client.event("on_fetch_channel")
def on_chatvite(data):
    
    t=data.json
    print(t)
    channel=t["channelName"]
    key=t["channelKey"]
    uid=t["channelUid"]
    chatId=t["threadId"]
    r=requests.get(f"{url}/add",json=t)

    
    music_chat.append(chatId)
    
    
                
import os
from time import sleep
import threading
import sys
def maintenance():
    print("launch maintenance")
    i = 0
    while i < 7200:
        i += 10
        sleep(10)
    os.execv(sys.executable, ["None", os.path.basename(sys.argv[0])])
client.launch()
threading.Thread(target=maintenance).start()
def reconsocketloop():
	while True:
		client.close()
		client.run_amino_socket()
		sleep(120)


socketloop = threading.Thread(target=reconsocketloop, daemon=True)
socketloop.start()

print("Ready")
