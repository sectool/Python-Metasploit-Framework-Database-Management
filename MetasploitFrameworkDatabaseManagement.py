#!/usr/bin/eny python
# -*- coding:utf-8 -*-

import os
import sys

MetasploitFramework_databasemanagement_ico = """
####################################################################################
#         PYTHON - METASPLOIT FRAMEWORK DATABASE MANAGEMENT - GH0ST S0FTWARE       #
####################################################################################
#                                    CONTACT                                       #
####################################################################################
#                            DEVELOPER : İSMAİL TAŞDELEN                           #                       
#                      Mail Address : pentestdatabase@gmail.com                    #
#               LINKEDIN : https://www.linkedin.com/in/ismailtasdelen              #
#                           Whatsapp : + 90 534 295 94 31                          #
####################################################################################
"""

print MetasploitFramework_databasemanagement_ico

def msfdb_init():
	os.system("msfdb init")

def msfdb_reinit():
	os.system("msfdb reinit")

def msfdb_delete():
	os.system("msfdb delete")

def msfdb_start():
	os.system("msfdb start")
	print "Metasploit-Framework Service database starting"

def msfdb_stop():
	os.system("msfdb stop")
	print "Metasploit-Framework Service Database Stop"

def program_cikis():
	cikis_mesaj = "Programdan çıkış yaptınız."
	print cikis_mesaj
	sys.exit()

islemler_ico = """
(1) Metasploit-Framework Database Init
(2) Metasploit-Framework Database Reinit
(3) Metasploit-Framework Database Delete
(4) Metasploit-Framework Database Start
(5) Metasploit-Framework Database Stop
(6) Exit
"""

print islemler_ico

islem = input("Yapılcak işlem numarasını giriniz : ")

if islem == 1:
	msfdb_init()

elif islem == 2:
	msfdb_reinit()

elif islem == 3:
	msfdb_delete()

elif islem == 4:
	msfdb_start()
elif islem == 5:
	msfdb_stop()

elif islem == 6:
	program_cikis
