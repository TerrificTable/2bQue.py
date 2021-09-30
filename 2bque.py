import requests, json, webbrowser, os
from colorama import Fore, Style

err = f"[{Fore.RED}-{Style.RESET_ALL}]"
out = f"[{Fore.GREEN}:{Style.RESET_ALL}]"
inf = f"[{Fore.YELLOW}i{Style.RESET_ALL}]"
inp = f"[{Fore.MAGENTA}>{Style.RESET_ALL}]"
log = f"[{Fore.CYAN}={Style.RESET_ALL}]"
finish = f"press [{Fore.YELLOW}ENTER{Style.RESET_ALL}] to exit"

que = requests.get("https://2bqueue.info/queue")
queueCount = json.loads(que.text)

players = requests.get("https://2bqueue.info/players")
playerNames = json.loads(players.text)

os.system("cls; clear")
os.system("title [2bQue.py - by. Terrific]")
os.system("mode 110, 30")
print(f'''{Fore.CYAN}
██████╗ ██████╗  ██████╗ ██╗   ██╗███████╗{Fore.RED}   ██████╗ ██╗   ██╗{Fore.CYAN}
╚════██╗██╔══██╗██╔═══██╗██║   ██║██╔════╝{Fore.RED}   ██╔══██╗╚██╗ ██╔╝{Fore.CYAN}
  ███╔═╝██████╦╝██║██╗██║██║   ██║█████╗  {Fore.RED}   ██████╔╝ ╚████╔╝{Fore.CYAN}
██╔══╝  ██╔══██╗╚██████╔╝██║   ██║██╔══╝  {Fore.RED}   ██╔═══╝   ╚██╔╝{Fore.CYAN}
███████╗██████╦╝ ╚═██╔═╝ ╚██████╔╝███████╗{Fore.RED}██╗██║        ██║{Fore.CYAN}
╚══════╝╚═════╝    ╚═╝    ╚═════╝ ╚══════╝{Fore.RED}╚═╝╚═╝        ╚═╝{Fore.CYAN}
{Style.RESET_ALL}''')

def getplayer(opt: str):
    if str(opt) == "que":    
        queplayers = playerNames['queue']["players"]
        print(f'{out} Players in Regular Queue: ')
        for i in range(len(queplayers)):
            print(f"{out} {i}. " + queplayers[i])
    elif str(opt) == "server": 
        serverplayers = playerNames['server']["players"]
        print(f'{out} Players on Regular Queue: ')
        for i in range(len(serverplayers)):
            print(f"{out} {i}. " + serverplayers[i])

def getskin(deb: str):
    skin = input(f"{inp} Input Username $ {Fore.BLUE}")
    webbrowser.open("https://minotar.net/armor/body/" + skin, new=2)
    if deb == "True":
        webbrowser.open('https://minotar.net/skin/' + skin, new=2)
    else:
        pass

def screen():
    print(f"""{Fore.MAGENTA}
{Fore.YELLOW}[x]{Style.RESET_ALL}{Fore.MAGENTA}================================{Fore.YELLOW}[x]{Style.RESET_ALL}{Fore.MAGENTA}
 ║  {Fore.RED}[1]{Style.RESET_ALL}{Fore.MAGENTA}:  {Fore.WHITE}Queue Length{Style.RESET_ALL}{Fore.MAGENTA}              ║
 ║  {Fore.RED}[2]{Style.RESET_ALL}{Fore.MAGENTA}:  {Fore.WHITE}Players in Queue{Style.RESET_ALL}{Fore.MAGENTA}          ║
 ║  {Fore.RED}[3]{Style.RESET_ALL}{Fore.MAGENTA}:  {Fore.WHITE}Players in Server{Style.RESET_ALL}{Fore.MAGENTA}         ║
 ║  {Fore.RED}[4]{Style.RESET_ALL}{Fore.MAGENTA}:  {Fore.WHITE}Skin Downloader{Style.RESET_ALL}{Fore.MAGENTA}           ║
 ║  {Fore.RED}[5]{Style.RESET_ALL}{Fore.MAGENTA}:  {Fore.WHITE}Exit{Style.RESET_ALL}{Fore.MAGENTA}                      ║
{Fore.YELLOW}[x]{Style.RESET_ALL}{Fore.MAGENTA}================================{Fore.YELLOW}[x]{Style.RESET_ALL}
""")

    choise = input(f'{inp} $ {Fore.BLUE}')
    if choise == '1':
        print(f'{out} Priority Queue Length: ' + str(queueCount['prio']))
        print(f'{out} Regular Queue Length: ' + str(queueCount['regular']))
        print(f'{out} Total Players in Queue: ' + str(queueCount['total']))
        input(); screen()
    elif choise == '2':
        getplayer("que")
        input(); screen()
    elif choise == '3':
        getplayer("server")
        input(); screen()
    elif choise == '4':
        getskin("True")
        input(); screen()
    else:
        print(f'{err} That is not an option! ')
        input(); screen()
screen()
