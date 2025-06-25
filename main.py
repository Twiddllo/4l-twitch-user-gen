import time
import threading, random, string, json, requests
from colorama import Fore
import os
os.system(" ")


with open("config.json") as config:
    config = json.load(config)
    numb = config['numbers']
    whl = config['while']
    ammount = config['ammount']
    letters = config['letters']

def get_username() -> str:
    if not hasattr(get_username, "usernames"):
        with open("user.txt", "r") as file:
            get_username.usernames = file.read().splitlines()
            get_username.index = 0  

    if get_username.index < len(get_username.usernames):
        username = get_username.usernames[get_username.index]
        get_username.index += 1
        return username
    else:
        return "".join(random.choices(string.ascii_letters, k=letters))


def check(username):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-GB',
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Origin': 'https://www.twitch.tv',
        'Referer': 'https://www.twitch.tv/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    data = '[{"operationName":"UsernameValidator_User","variables":{"username":"' + username + '"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660"}}}]'


    r = requests.post('https://gql.twitch.tv/gql', headers=headers, data=data).json()[0]["data"]["isUsernameAvailable"]
    if r == True:
        print(f"{Fore.GREEN}+{Fore.RESET} [{username}]")
        return True
    else:
        print(f"{Fore.RED}-{Fore.RESET} [{username}]")
        return False

if whl == True:
    while True:
        x = threading.Thread(target=check, args=(get_username(),)).start()
        if x == False:
            time.sleep(10)
else:
    for i in range(ammount):
        x = threading.Thread(target=check, args=(get_username(),)).start()
        if x == False:
            time.sleep(10)