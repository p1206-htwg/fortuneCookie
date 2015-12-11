#!/usr/bin/python
# -*- coding: cp1252 -*-
import string
import time
import os
from os.path import basename


#---months to number converter---
def month_converter(monthWord):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(monthWord) + 1

start = time.time()			#Laufzeit um script zu durchlaufen
  
sub_dir = "C:\Users\Ait\Downloads\Max-rep\Data"
link = 'https:\/'									#separator bestimmen um links zu löschen
link2 = 'http:\/'									#separator bestimmen um links zu löschen
team = raw_input('geben Sie den Mannschaftsnamen ein: ')

for file in os.listdir(sub_dir):

	fnew = os.path.splitext(file)[0]				#Dateiname ohne textendung
	f1 = fnew+"_clean.txt"							#Dateiname erweitern um "_clean"

	if file.endswith(".txt"):
		txt_in = open(os.path.join(sub_dir,file), "r").read()   #lesen der Datei
		txt_out = open(os.path.join(sub_dir,f1), "w")      		#schreiben der Datei


		#Ein Array mit dem Index für Anfang und Ende aller twitter msgs in der txt file wird erstellt
		beg_arr = [n for n in xrange(len(txt_in)) if txt_in.find('{"created_at', n) == n]
		end_arr = [n for n in xrange(len(txt_in)) if txt_in.find('","source":"', n) == n]

		for i in range(0,len(beg_arr)):						#schleife von 0 bis Anzahl der Elemente im Array

			monthBeg = beg_arr[i]+19     			  		#String für Orientierungspunkt
			monthWord = txt_in[monthBeg:monthBeg+3]
			month = str(month_converter(monthWord))         #Monat als Zahl
			day = txt_in[monthBeg+4:monthBeg+6]             #Tag als Zahl
			year = txt_in[monthBeg+22:monthBeg+26]          #Jahr als Zahl
			msgtime = txt_in[monthBeg+7:monthBeg+15]           #Zeit als hh:mm:ss
			date = day + "/" + month + "/" + year           #Datum als dd/mm/yyyy

			bom = beg_arr[i]+109              			    #begin of msg
			eom = end_arr[i]             				    #end of msg
			tmsg = txt_in[bom:eom]                          #twitter msg
			
			if team in tmsg:
				tmsg = tmsg.split(link, 1)[0]					#string teilen, der Teil mit dem Link wird entfernt
				tmsg = tmsg.split(link2, 1)[0]					#string teilen, der Teil mit dem Link wird entfernt

				if tmsg.startswith('RT'):
					tmsg = tmsg.replace('RT', "")
				
				tmsg_lst = tmsg.split()	
				matching = [s for s in tmsg_lst if "@" in s] #get all the items containing @ in the list
				
				for i in range(0,len(matching)):
					tmsg = tmsg.replace(matching[i], "")	#lösche gefundene wörter
				
				matching = [s for s in tmsg_lst if "\u" in s] #get all the items containing /u in the list
				
				for i in range(0,len(matching)):
					tmsg = tmsg.replace(matching[i], "")	#lösche gefundene wörter
					
				tmsg = " ".join(tmsg.split())				#alle doppelten/zuviele leerzeichen entfernen
				txt_out.write(date +" "+ msgtime +" "+ tmsg + "\n")	#txt_out.write(date +" "+ msgtime +" "+ tmsg + "\n")


		print 'It took', time.time()-start, 'seconds.'
		txt_out.close()        #schließen der Datei

