
# -*- coding: utf-8 -*-
# =========================================================================================================================================
import os
import random
import smtplib
import sys
import getpass
import time
# =======================       Arez        ================================================================================================
os.system('clear')
print ('''
     _     ______  _______  ________                       
    | |    |    /  |     |         /                
   |   |   |/ /    |             /    
  |     |  |  /    |_____      /
  |-----|  |  \    |         /         
  |     |  |   \   |_____| /________  
                            By \033[93m@Ravo_m\033[97m
''')
print(" ")
#########################   Zanyari kase ##########################
User = raw_input('\033[94m[?] \033[97mEmail \033[92mkat\033[97m :\033[93m ')
passworde = getpass.getpass('\033[94m[?]\033[97m Pass \033[91mpordakat\033[97m :\033[93m ')
print(" ")
Email Fake = raw_input('\033[94m[?]\033[97m Bo  \033[91mQurbani\033[97m : \033[93m')
message = raw_input('\033[94m[?]\033[97m Namyak \033[92mBnusa\033[97m : \033[93m')
print(" ")
hani = input('\033[94m[?] \033[97mNumber of \033[92mnardn\033[97m : \033[93m')
print(" ")
print("\033[94m[*] \033[97mSending : ")
############################### Zanyari Server ##################
smtp_server = 'smtp.gmail.com'
port = 587

##########################  Login ############################
try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passworde)
###################### SENDING #########################################
    for i in range(1, hani+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + message
        server.sendmail(user,victime,msg)
        print ("\033[94m[✔]\033[97m namaka \033[92mNardra\033[97m  :\033[93m %i") % i
        sys.stdout.flush()
    server.quit()
    print ('\033[93m[✔]\033[97m Hamuu \033[97mMessage was\033[92m Nardrwakan\033[97m ')
    
    
except KeyboardInterrupt:
    print ('[✘] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(" ")
    print("\033[94m[✘] \033[91mError \033[97m:")
    print ('\033[94m[✘] \033[97mThe \033[93musername \033[97mor \033[93mpassword \033[97myou entered is incorrect.')
    print ("\033[94m[!] \033[97mCheck if the Options of 'Applications are less secure' is enabled\nCheck at https://myaccount.google.com/lesssecureapps")
    sys.exit()
