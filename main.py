try:
	import  sys, os,json,requests,re,random,names,requesck
	import names
	from requesck import check
except ImportError as e:
	os.system('pip install requests')
	os.system('pip install names')
	os.system('pip install requesck')
	
	

A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
M ="\033[1;96m"

os.system('clear')
TB = f"""                           
    {B} ██████{M}╗{B}██{M}╗  {B}██{M}╗{B}███████{M}╗ {B}██████{M}╗{B}██{M}╗  {B}██{M}╗
    {B}██{M}╔════╝{B}██{M}║  {B}██{M}║{B}██{M}╔════╝{B}██{M}╔════╝{B}██{M}║ {B}██{M}╔╝
    {B}██{M}║     {B}███████{M}║{B}█████{M}╗  {B}██{M}║     {B}█████{M}╔╝ 
    {B}██{M}║     {B}██{M}╔══{B}██{M}║{B}██{M}╔══╝  {B}██{M}║     {B}██{M}╔═{B}██{M}╗ 
    {B}╚{B}██████{M}╗{B}██{M}║  {B}██{M}║{B}███████{M}╗╚{B}██████{M}╗{B}██{M}║  {B}██{M}╗
    {M} ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
    
    {H} < \033[1;92mTHE TOOL IS CHECKER-EMAIL-TSM{H} >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ
{A}---------------------------
"""
Start = f"""                           
    {B} ██████{M}╗{B}██{M}╗  {B}██{M}╗{B}███████{M}╗ {B}██████{M}╗{B}██{M}╗  {B}██{M}╗
    {B}██{M}╔════╝{B}██{M}║  {B}██{M}║{B}██{M}╔════╝{B}██{M}╔════╝{B}██{M}║ {B}██{M}╔╝
    {B}██{M}║     {B}███████{M}║{B}█████{M}╗  {B}██{M}║     {B}█████{M}╔╝ 
    {B}██{M}║     {B}██{M}╔══{B}██{M}║{B}██{M}╔══╝  {B}██{M}║     {B}██{M}╔═{B}██{M}╗ 
    {B}╚{B}██████{M}╗{B}██{M}║  {B}██{M}║{B}███████{M}╗╚{B}██████{M}╗{B}██{M}║  {B}██{M}╗
    {M} ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
    
    {H} < \033[1;92mTHE TOOL IS CHECKER-EMAIL-TSM{H} >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ
 {A}---------------------------
 \033[1;91m(\033[1;92m1\033[1;91m) \033[1;90m\033[1;97m CHECKER INSTAGRAM
 \033[1;91m(\033[1;92m2\033[1;91m) \033[1;90m\033[1;97m CHECKER TIKTOK
 \033[1;91m(\033[1;92m3\033[1;91m) \033[1;90m\033[1;97m CHECKER TWITTER
 \033[1;91m(\033[1;92m3\033[1;91m) \033[1;90m\033[1;97m CHECKER FACEBOOK
 \033[1;91m(\033[1;92m3\033[1;91m) \033[1;90m\033[1;97m CHECKER SNAPCHAT
 \033[1;91m(\033[1;92m0\033[1;91m) \033[1;90m\033[1;91m EXIT  
"""
def gmail(email,ID,token,message):
	
	sidraok = (str(message)+"\n────── • ✧✧ • ──────\n ⌯ Email 📧 : " + str(email) + "\n────── • ✧✧ • ──────\n ⚖️ Tele : @SidraTools")
	response = check.gmail(str(email))
	if (response) ==True:
		print(E+email)
		requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(sidraok))
		f=open('Email-Ok.txt','a')
		f.write(str(sidraok)+"\n")
		f.close()
	elif (response) ==False:
		print (H+email)
		
def hotmail(email,ID,token,message):
	
	sidraok = (str(message)+"\n────── • ✧✧ • ──────\n ⌯ Email 📧 : " + str(email) + "\n────── • ✧✧ • ──────\n ⚖️ Tele : @SidraTools")
	response = check.hotmail(str(email))
	if (response) ==True:
		print(E+email)
		requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(sidraok))
		f=open('Email-Ok.txt','a')
		f.write(str(sidraok)+"\n")
		f.close()
	elif (response) ==False:
		print (H+email)
		
def yahoo(email,ID,token,message):
	
	sidraok = (str(message)+"\n────── • ✧✧ • ──────\n ⌯ Email 📧 : " + str(email) + "\n────── • ✧✧ • ──────\n ⚖️ Tele : @SidraTools")
	response = check.yahoo(str(email))
	if (response) ==True:
		print(E+email)
		requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(sidraok))
		f=open('Email-Ok.txt','a')
		f.write(str(sidraok)+"\n")
		f.close()
	elif (response) ==False:
		print (H+email)
		
def mailur(email,ID,token,message):
	
	sidraok = (str(message)+"\n────── • ✧✧ • ──────\n ⌯ Email 📧 : " + str(email) + "\n────── • ✧✧ • ──────\n ⚖️ Tele : @SidraTools")
	response = check.mailur(str(email))
	if (response) ==True:
		print(E+email)
		requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(sidraok))
		f=open('Email-Ok.txt','a')
		f.write(str(sidraok)+"\n")
		f.close()
	elif (response) ==False:
		print (H+email)


def instagram():
	os.system('clear')
	print(TB)
	print(A+"("+E+"⌯"+A+") "+B+" ┌───── • ✧✧ • ─────┐")
	print(A+"("+E+"1"+A+") "+E+" Checker-Email-Random")
	print(A+"("+E+"2"+A+") "+H+" Checker-Email-List   ")
	print(A+"("+E+"0"+A+") "+A+" Exit")
	print(A+"("+E+"⌯"+A+") "+B+" └───── • ✧✧ • ─────┘")
	BTO=input("\n"+A+"("+E+"⌯"+A+")"+B+ " Choose Checker :"+C)
	if str(BTO)=="1":
		os.system('clear')
		print(TB)
		ID = input(A+"("+E+"⌯"+A+")"+H+ " ID  : "+C)
		token = input(A+"("+E+"⌯"+A+")"+H+ " TOKEN : "+C)
		SK = input(A+"("+E+"⌯"+A+")"+H+ " DOMAIN : "+C)
		os.system('clear')
		print(TB)
		SA = '0987654321'
		i=0	
		while True:
			i+=1
			if i == 101:
				i=0		
			SM = names.get_first_name()
			email=(SM[0:-1] + "%d" % (i+1) +str(SK))
			#email = str(SM)+str(SB)+str(SK)
			message = (" ⌯ Hi pro Email Instagram ✓ ⌯ ")
			checker = check.instagram(str(email))
			if (checker) ==True:
				print(E+email)
				if ("@gmail.com") in email:
					gmail(email,ID,token,message)
				if ("@hotmail.com") in email:
					hotmail(email,ID,token,message)
				if ("@outlook.com") in email:
					hotmail(email,ID,token,message)
				if ("@mail.ru") in email:
					mailru(email,ID,token,message)
				if ("@yahoo.com") in email:
					yahoo(email,ID,token,message)
				
			elif (checker) ==False:
				print(A+email)
				

	if str(BTO)=="2":
		os.system('clear')
		print(TB)
		ID = input(A+"("+E+"⌯"+A+")"+H+ " ID  : "+C)
		token = input(A+"("+E+"⌯"+A+")"+H+ " TOKEN : "+C)
		SK = input(A+"("+E+"⌯"+A+")"+H+ " File : "+C)
		os.system('clear')
		print(TB)
		file = open(SK, 'r')
		while True:
			email = file.readline().split('\n')[0]
			if email == '':
				print(A+"The examination has been completed.   "+E+fil)
				break
			message = (" ⌯ Hi pro Email Instagram ✓ ⌯ ")
			checker = check.instagram(str(email))
			if (checker) ==True:
				print(E+email)
				if ("@gmail.com") in email:
					gmail(email,ID,token,message)
				if ("@hotmail.com") in email:
					hotmail(email,ID,token,message)
				if ("@outlook.com") in email:
					hotmail(email,ID,token,message)
				if ("@mail.ru") in email:
					mailru(email,ID,token,message)
				if ("@yahoo.com") in email:
					yahoo(email,ID,token,message)
				
			elif (checker) ==False:
				print(A+email)
				
				
def tiktok():
	os.system('clear')
	print(TB)
	print(A+"("+E+"⌯"+A+") "+B+" ┌───── • ✧✧ • ─────┐")
	print(A+"("+E+"1"+A+") "+E+" Checker-Email-Random")
	print(A+"("+E+"2"+A+") "+H+" Checker-Email-List   ")
	print(A+"("+E+"0"+A+") "+A+" Exit")
	print(A+"("+E+"⌯"+A+") "+B+" └───── • ✧✧ • ─────┘")
	BTO=input("\n"+A+"("+E+"⌯"+A+")"+B+ " Choose Checker :"+C)
	if str(BTO)=="1":
		os.system('clear')
		print(TB)
		ID = input(A+"("+E+"⌯"+A+")"+H+ " ID  : "+C)
		token = input(A+"("+E+"⌯"+A+")"+H+ " TOKEN : "+C)
		SK = input(A+"("+E+"⌯"+A+")"+H+ " DOMAIN : "+C)
		os.system('clear')
		print(TB)
		SA = '0987654321'
		i=0	
		while True:
			i+=1
			if i == 101:
				i=0		
			SM = names.get_first_name()
			email=(SM[0:-1] + "_%d" % (i+1) + str(SK))
			#email = str(SM)+str(SB)+str(SK)
			message = (" ⌯ Hi pro Email Tiktok ✓ ⌯ ")
			checker = check.tiktok(str(email))
			if (checker) ==True:
				print(E+email)
				if ("@gmail.com") in email:
					gmail(email,ID,token,message)
				if ("@hotmail.com") in email:
					hotmail(email,ID,token,message)
				if ("@outlook.com") in email:
					hotmail(email,ID,token,message)
				if ("@mail.ru") in email:
					mailru(email,ID,token,message)
				if ("@yahoo.com") in email:
					yahoo(email,ID,token,message)
				
			elif (checker) ==False:
				print(A+email)
				

	if str(BTO)=="2":
		os.system('clear')
		print(TB)
		ID = input(A+"("+E+"⌯"+A+")"+H+ " ID  : "+C)
		token = input(A+"("+E+"⌯"+A+")"+H+ " TOKEN : "+C)
		SK = input(A+"("+E+"⌯"+A+")"+H+ " File : "+C)
		os.system('clear')
		print(TB)
		file = open(SK, 'r')
		while True:
			email = file.readline().split('\n')[0]
			if email == '':
				print(A+"The examination has been completed.   "+E+fil)
				break
			message = (" ⌯ Hi pro Email Tiktok ✓ ⌯ ")
			checker = check.tiktok(str(email))
			if (checker) ==True:
				print(E+email)
				if ("@gmail.com") in email:
					gmail(email,ID,token,message)
				if ("@hotmail.com") in email:
					hotmail(email,ID,token,message)
				if ("@outlook.com") in email:
					hotmail(email,ID,token,message)
				if ("@mail.ru") in email:
					mailru(email,ID,token,message)
				if ("@yahoo.com") in email:
					yahoo(email,ID,token,message)
				
			elif (checker) ==False:
				print(A+email)
				
				
def twitter():
	os.system('clear')
	print(TB)
	print(A+"("+E+"⌯"+A+") "+B+" ┌───── • ✧✧ • ─────┐")
	print(A+"("+E+"1"+A+") "+E+" Checker-Email-Random")
	print(A+"("+E+"2"+A+") "+H+" Checker-Email-List   ")
	print(A+"("+E+"0"+A+") "+A+" Exit")
	print(A+"("+E+"⌯"+A+") "+B+" └───── • ✧✧ • ─────┘")
	BTO=input("\n"+A+"("+E+"⌯"+A+")"+B+ " Choose Checker :"+C)
	if str(BTO)=="1":
		os.system('clear')
		print(TB)
		ID = input(A+"("+E+"⌯"+A+")"+H+ " ID  : "+C)
		token = input(A+"("+E+"⌯"+A+")"+H+ " TOKEN : "+C)
		SK = input(A+"("+E+"⌯"+A+")"+H+ " DOMAIN : "+C)
		os.system('clear')
		print(TB)
		SA = '0987654321'
		i=0	
		while True:
			i+=1
			if i == 101:
				i=0		
			SM = names.get_first_name()
			email=(SM[0:-1] + "_%d" % (i+1) + str(SK))
			#email = str(SM)+str(SB)+str(SK)
			message = (" ⌯ Hi pro Email Twitter ✓ ⌯ ")
			checker = check.twitter(str(email))
			if (checker) ==True:
				print(E+email)
				if ("@gmail.com") in email:
					gmail(email,ID,token,message)
				if ("@hotmail.com") in email:
					hotmail(email,ID,token,message)
				if ("@outlook.com") in email:
					hotmail(email,ID,token,message)
				if ("@mail.ru") in email:
					mailru(email,ID,token,message)
				if ("@yahoo.com") in email:
					yahoo(email,ID,token,message)
				
			elif (checker) ==False:
				print(A+email)
				

	if str(BTO)=="2":
		os.system('clear')
		print(TB)
		ID = input(A+"("+E+"⌯"+A+")"+H+ " ID  : "+C)
		token = input(A+"("+E+"⌯"+A+")"+H+ " TOKEN : "+C)
		SK = input(A+"("+E+"⌯"+A+")"+H+ " File : "+C)
		os.system('clear')
		print(TB)
		file = open(SK, 'r')
		while True:
			email = file.readline().split('\n')[0]
			if email == '':
				print(A+"The examination has been completed.   "+E+fil)
				break
			message = (" ⌯ Hi pro Email Twitter ✓ ⌯ ")
			checker = check.twitter(str(email))
			if (checker) ==True:
				print(E+email)
				if ("@gmail.com") in email:
					gmail(email,ID,token,message)
				if ("@hotmail.com") in email:
					hotmail(email,ID,token,message)
				if ("@outlook.com") in email:
					hotmail(email,ID,token,message)
				if ("@mail.ru") in email:
					mailru(email,ID,token,message)
				if ("@yahoo.com") in email:
					yahoo(email,ID,token,message)
				
			elif (checker) ==False:
				print(A+email)
				
def facebook():
	os.system('clear')
	print(TB)
	print(A+"("+E+"⌯"+A+") "+B+" ┌───── • ✧✧ • ─────┐")
	print(A+"("+E+"1"+A+") "+E+" Checker-Email-Random")
	print(A+"("+E+"2"+A+") "+H+" Checker-Email-List   ")
	print(A+"("+E+"0"+A+") "+A+" Exit")
	print(A+"("+E+"⌯"+A+") "+B+" └───── • ✧✧ • ─────┘")
	BTO=input("\n"+A+"("+E+"⌯"+A+")"+B+ " Choose Checker :"+C)
	if str(BTO)=="1":
		os.system('clear')
		print(TB)
		ID = input(A+"("+E+"⌯"+A+")"+H+ " ID  : "+C)
		token = input(A+"("+E+"⌯"+A+")"+H+ " TOKEN : "+C)
		SK = input(A+"("+E+"⌯"+A+")"+H+ " DOMAIN : "+C)
		os.system('clear')
		print(TB)
		SA = '0987654321'
		i=0	
		while True:
			i+=1
			if i == 101:
				i=0		
			SM = names.get_first_name()
			email=(SM[0:-1] + "_%d" % (i+1) + str(SK))
			#email = str(SM)+str(SB)+str(SK)
			message = (" ⌯ Hi pro Email Facebook ✓ ⌯ ")
			checker = check.facebook(str(email))
			if (checker) ==True:
				print(E+email)
				if ("@gmail.com") in email:
					gmail(email,ID,token,message)
				if ("@hotmail.com") in email:
					hotmail(email,ID,token,message)
				if ("@outlook.com") in email:
					hotmail(email,ID,token,message)
				if ("@mail.ru") in email:
					mailru(email,ID,token,message)
				if ("@yahoo.com") in email:
					yahoo(email,ID,token,message)
				
			elif (checker) ==False:
				print(A+email)

	if str(BTO)=="2":
		os.system('clear')
		print(TB)
		ID = input(A+"("+E+"⌯"+A+")"+H+ " ID  : "+C)
		token = input(A+"("+E+"⌯"+A+")"+H+ " TOKEN : "+C)
		SK = input(A+"("+E+"⌯"+A+")"+H+ " File : "+C)
		os.system('clear')
		print(TB)
		file = open(SK, 'r')
		while True:
			email = file.readline().split('\n')[0]
			if email == '':
				print(A+"The examination has been completed.   "+E+fil)
				break
			message = (" ⌯ Hi pro Email Facebook ✓ ⌯ ")
			checker = check.facebook(str(email))
			if (checker) ==True:
				print(E+email)
				if ("@gmail.com") in email:
					gmail(email,ID,token,message)
				if ("@hotmail.com") in email:
					hotmail(email,ID,token,message)
				if ("@outlook.com") in email:
					hotmail(email,ID,token,message)
				if ("@mail.ru") in email:
					mailru(email,ID,token,message)
				if ("@yahoo.com") in email:
					yahoo(email,ID,token,message)
				
			elif (checker) ==False:
				print(A+email)
				
				
def snapchat():
	os.system('clear')
	print(TB)
	print(A+"("+E+"⌯"+A+") "+B+" ┌───── • ✧✧ • ─────┐")
	print(A+"("+E+"1"+A+") "+E+" Checker-Email-Random")
	print(A+"("+E+"2"+A+") "+H+" Checker-Email-List   ")
	print(A+"("+E+"0"+A+") "+A+" Exit")
	print(A+"("+E+"⌯"+A+") "+B+" └───── • ✧✧ • ─────┘")
	BTO=input("\n"+A+"("+E+"⌯"+A+")"+B+ " Choose Checker :"+C)
	if str(BTO)=="1":
		os.system('clear')
		print(TB)
		ID = input(A+"("+E+"⌯"+A+")"+H+ " ID  : "+C)
		token = input(A+"("+E+"⌯"+A+")"+H+ " TOKEN : "+C)
		SK = input(A+"("+E+"⌯"+A+")"+H+ " DOMAIN : "+C)
		os.system('clear')
		print(TB)
		SA = '0987654321'
		i=0	
		while True:
			i+=1
			if i == 101:
				i=0		
			SM = names.get_first_name()
			email=(SM[0:-1] + "_%d" % (i+1) + str(SK))
			#email = str(SM)+str(SB)+str(SK)
			message = (" ⌯ Hi pro Email Snapchat ✓ ⌯ ")
			checker = check.snapchat(str(email))
			if (checker) ==True:
				print(E+email)
				if ("@gmail.com") in email:
					gmail(email,ID,token,message)
				if ("@hotmail.com") in email:
					hotmail(email,ID,token,message)
				if ("@outlook.com") in email:
					hotmail(email,ID,token,message)
				if ("@mail.ru") in email:
					mailru(email,ID,token,message)
				if ("@yahoo.com") in email:
					yahoo(email,ID,token,message)
				
			elif (checker) ==False:
				print(A+email)
				

	if str(BTO)=="2":
		os.system('clear')
		print(TB)
		ID = input(A+"("+E+"⌯"+A+")"+H+ " ID  : "+C)
		token = input(A+"("+E+"⌯"+A+")"+H+ " TOKEN : "+C)
		SK = input(A+"("+E+"⌯"+A+")"+H+ " File : "+C)
		os.system('clear')
		print(TB)
		file = open(SK, 'r')
		while True:
			email = file.readline().split('\n')[0]
			if email == '':
				print(A+"The examination has been completed.   "+E+fil)
				break
			message = (" ⌯ Hi pro Email Snapchat ✓ ⌯ ")
			checker = check.snapchat(str(email))
			if (checker) ==True:
				print(E+email)
				if ("@gmail.com") in email:
					gmail(email,ID,token,message)
				if ("@hotmail.com") in email:
					hotmail(email,ID,token,message)
				if ("@outlook.com") in email:
					hotmail(email,ID,token,message)
				if ("@mail.ru") in email:
					mailru(email,ID,token,message)
				if ("@yahoo.com") in email:
					yahoo(email,ID,token,message)
				
			elif (checker) ==False:
				print(A+email)
				
				

def HACK():
  os.system('clear')
  print (Start)
  SidraELEzz=input("\n"+A+" ("+E+"⌯"+A+")"+B+ " Choose Number :"+C)
  if SidraELEzz =="1":
    instagram()
  elif SidraELEzz =="2":
    tiktok()
  elif SidraELEzz =="3":
    twitter()
  elif SidraELEzz =="4":
    facebook()
  elif SidraELEzz =="5":
    snapchat()
  
  else:
    exit('  goodluck')

HACK() if __name__ == '__main__' else exit('Sorry, something wrong, please try again later.')
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://sidrabot.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
