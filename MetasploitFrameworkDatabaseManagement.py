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
star = "####################################################################################"

print MetasploitFramework_databasemanagement_ico

def msfdb_init():
	os.system("msfdb init")

def msfdb_reinit():
	os.system("msfdb reinit")

def msfdb_delete():
	os.system("msfdb delete")
	veritabani_kaldirildi_mesaj_ico = "Metasploit-Framework Veritabanı Kaldırıldı."
	print star
	print veritabani_kaldirildi_mesaj_ico
	
def msfdb_start():
	os.system("msfdb start")
	servis_baslatma_mesaj_ico = "Metasploit-Framework Service Database Starting.."
	print star
	print servis_baslatma_mesaj_ico
	
def msfdb_stop():
	os.system("msfdb stop")
	servis_durdurma_mesaj_ico = "Metasploit-Framework Service Database Stop.."
	print star
	print servis_durdurma_mesaj_ico

def program_cikis():
	cikis_mesaj = "Programdan çıkış yaptınız.."
	print star
	print cikis_mesaj
	sys.exit()

islemler_ico = """
(1) Metasploit-Framework Database Init
(2) Metasploit-Framework Database Reinit
(3) Metasploit-Framework Database Delete
(4) Metasploit-Framework Service Database Start
(5) Metasploit-Framework Service Database Stop
(6) Exit
"""

print islemler_ico

print star

islem = input("Yapılcak işlem numarasını giriniz : ")

if islem == 1:
	print star
	msfdb_init()
	print star

elif islem == 2:
	print star
	msfdb_reinit()
	print star

elif islem == 3:
	print star
	msfdb_delete()
	print star

elif islem == 4:
	print star
	msfdb_start()
	print star
	
elif islem == 5:
	print star
	msfdb_stop()
	print star

elif islem == 6:
	print star
	program_cikis
	print star
