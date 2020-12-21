# coding:utf-8
# heker emang gini semua dibikin susah xD
# only for py3

from os import system
from platform import python_version as versi
import time, sys
try:
	from requests import *
	from bs4 import BeautifulSoup as par
	from prettytable import PrettyTable
except:
	exit("[!] MODULE BELUM TERINSTALL SEMUA..\n    SILAHKAN BACA README.md DAHULU")

if versi().split(".")[0] != "3":
	exit("ketik: python "+sys.argv[0])

color = {
	"hijau":"\x1b[1;92m",
	"putih":"\x1b[1;97m",
	"merah":"\x1b[1;91m",
	"kuning":"\x1b[1;93m",
	"biru":"\x1b[1;94m",
	"cyan":"\x1b[1;96m"
	}

notic = {
	"warning":"%s[%s!%s]"%(color["putih"],color["kuning"],color["putih"]),
	"error":"%s[%s×%s]"%(color["putih"],color["merah"],color["putih"]),
	"catatan":"%s[%s+%s]"%(color["putih"],color["hijau"],color["putih"]),
	"input":"%s[%s=%s]"%(color["putih"],color["hijau"],color["putih"]),
	"succes":"%s[%s✓%s]"%(color["putih"],color["hijau"],color["putih"])
	}

list_domain = [
		"orgfree.com","6te.net",
		"ueuo.com","eu5.org","noads.biz",
		"coolpage.biz","freeoda.com",
		"freevar.com","freetzi.com",
		"xp3.biz"]

url_regist1 = "https://www.freewebhostingarea.com/cgi-bin/create_account.cgi"
url_regist2 = "https://newserv.freewha.com/cgi-bin/create_ini.cgi"
url_server  = "https://project-rizky.000webhostapp.com/server.php"
logo = """
%s _ _ _ _____ _____
| | | |  |  |  _  |        %sFree%sWha%s
| | | |     |     | %s+-------------------+%s
|_____|__|__|__|__|    %sTEAM%s: %sXIUZCODE%s
"""%(color["cyan"],color["merah"],color["putih"],color["cyan"],color["putih"],color["cyan"],color["putih"],color["merah"],color["kuning"],color["putih"])


class Regis1:
	def reg0():
		system("clear")
		print(logo)
		nama_web = input(notic["input"]+" NAMA WEBSITE: ").replace(" ","-")
		while nama_web == "":
			nama_web = input(notic["input"]+" NAMA WEBSITE: ").replace(" ","-")
		system("clear")
		print(logo)
		x = PrettyTable(["NOMOR","DOMAIN"])
		for domain in range(len(list_domain)):
			x.add_row([str(domain+1),list_domain[domain]])
		print(x)
		print(notic["input"]+" NAMA WEBSITE: "+nama_web)
		try:
			domai = int(input(notic["input"]+" DOMAIN      : "))
			while domai == "":
				domai = int(input(notic["input"]+" DOMAIN      : "))
			owh = list_domain[domai-1]
		except (ValueError, IndexError):
			exit(notic["warning"]+" Masukan Angka Sesuai List Domain")
		print(notic["warning"]+" TUNGGU SEBENTAR ...")
		time.sleep(2)
		Regis1.reg1(nama_web, owh)

	def reg1(web, dom):
		system("clear")
		print(logo)
		head1 = {
			"Host":"www.freewebhostingarea.com",
			"Connection":"keep-alive",
			"Content-Lenght":"59",
			"Origin":"https://freewha.com",
			"Upgrade-Insecure-Requests":"1",
			"Content-Type":"application/x-www-form-urlencoded",
			"User-Agent":get(url_server).json()["user"],
			"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
			"Referer":"https://freewha.com/",
			"Accept-Encoding":"gzip, deflate",
			"Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
		data1 = {
			"thirdLevelDomain":web,
			"domain":dom,
			"action":"check_domain"
			}
		chekin = par(post(url_regist1, headers=head1, data=data1).text, "html.parser")
		if "Subdomain must be at least 3 characters" in chekin:
			exit(notic["warning"]+" SUBDOMAIN MINIMAL 3 KARAKTER")
		value = chekin.find("input",{"name":"agree"}).get("value")
		print(notic["input"]+" NAMA WEBSITE: "+web)
		print(notic["input"]+" DOMAIN ANDA : "+dom)
		set_user = input(notic["input"]+" INPUT EMAIL : ")
		while set_user == "":
			set_user = input(notic["input"]+" INPUT EMAIL : ")
		set_pasw = input(notic["input"]+" SET PASSWORD: ")
		while set_pasw == "":
			set_pasw = input(notic["input"]+" SET PASSWORD: ")
		print(notic["warning"]+" TUNGGU SEBENTAR ...")
		time.sleep(2)
		webs = web+"."+dom
		Regis2.reg2(webs, set_user, set_pasw, value)

class Regis2:
	def reg2(website, user, pasw, valagre):
		system("clear")
		print(logo)
		head2 = {
			"Host": "newserv.freewha.com",
			"content-length": "124",
			"origin": "https://www.freewebhostingarea.com",
			"upgrade-insecure-requests": "1",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": get(url_server).json()["user"],
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
			"referer": "https://www.freewebhostingarea.com/cgi-bin/create_account.cgi",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
		data2 = {
			"action": "validate",
			"domainName": website,
			"email": user,
			"password": pasw,
			"confirmPassword": pasw,
			"agree": valagre
			}

		cookie = {"FreeWHA-persistent":"checked"}
		chekin = post(url_regist2, headers=head2, data=data2, cookies=cookie).text
		if "This account already exists!" in chekin:
			exit(notic["error"]+" USER SUDAH TERSEDIA\n    REGIS DENGAN EMAIL BARU LAGI")
		elif "ATTENTION!!" in chekin:
			system("clear")
			print(logo)
			print(notic["succes"]+" WEBSITE BERHASIL DIBUAT.")
			print("-"*40)
			print(notic["succes"]+" LOGIN INFO:")
			print("    * CPANEL   : http://"+website+"/cpanel")
			print("    * USERNAME : "+website)
			print("    * PASSWORD : "+pasw)
			print("-"*40)
			print(notic["succes"]+" FTP INFO:")
			print("    * FTP      : http://"+website+"/ftp")
			print("    * HOST     : "+website)
			print("    * USERNAME : "+website)
			print("    * PASSWORD : "+pasw)
			print("-"*40)
		else:
			exit(notic["warning"]+" KESALAHAN TEKNIS\n    COBA BUAT ULANG")

if __name__=="__main__":
	try:
		Regis1.reg0()
	except Exception as error:
		print(notic["error"],str(error))
