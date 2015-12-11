#!/usr/bin/python
# -*- coding: cp1252 -*-
from datetime import datetime, time


#---months to number converter---
def month_converter(monthWord):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(monthWord) + 1

txt_in = open('TwitterData-10_12_2015_14_00_01.txt').read()            		#lesen der Datei
txt_out = open("TwitterData-10_12_2015_14_00_01_clean.txt", "w")      							#schreiben der Datei
	
starthour = input('Filtern von[hh]:')
startmin = input('Filtern von[mm]:')
endhour = input('Filtern bis[hh]:')
endmin = input('Filtern bis[mm]:')

#Ein Array mit dem Index für Anfang und Ende aller twitter msgs in der txt file wird erstellt
beg_arr = [n for n in xrange(len(txt_in)) if txt_in.find('{"created_at', n) == n]
end_arr = [n for n in xrange(len(txt_in)) if txt_in.find('","source":"', n) == n]

cln_msg = []										#declare as  list
link = 'https:\/'									#separator bestimmen um links zu löschen
link2 = 'http:\/'									#separator bestimmen um links zu löschen

for i in range(0,len(beg_arr)):						#schleife von 0 bis Anzahl der Elemente im Array

	monthBeg = beg_arr[i]+19     			  		#String für Orientierungspunkt
	monthWord = txt_in[monthBeg:monthBeg+3]
	month = str(month_converter(monthWord))         #Monat als Zahl
	day = txt_in[monthBeg+4:monthBeg+6]             #Tag als Zahl
	year = txt_in[monthBeg+22:monthBeg+26]          #Jahr als Zahl
	msgtime = txt_in[monthBeg+7:monthBeg+15]        #Zeit als hh:mm:ss
	date = day + "/" + month + "/" + year           #Datum als dd/mm/yyyy
	bom = beg_arr[i]+109              			    #begin of msg
	eom = end_arr[i]             				    #end of msg
	tmsgl = txt_in[bom:eom]                         #twitter msg mit links
	tmsg = tmsgl.split(link, 1)[0]					#string teilen, der Teil mit dem Link wird entfernt
	tmsg = tmsgl.split(link2, 1)[0]					#string teilen, der Teil mit dem Link wird entfernt

	temptime = datetime.strptime(msgtime, "%X")		#Datierung in ein Time-objekt umwandeln

	if tmsg.startswith('RT'):
		tmsg = tmsg.replace('RT', "")
	
	tmsg_lst = tmsg.split()	
	matching = [s for s in tmsg_lst if "@" in s] #get all the items containing @ in the list
	
	for i in range(0,len(matching)):
		tmsg = tmsg.replace(matching[i], "")	#lösche gefundene wörter
	
	matching = [s for s in tmsg_lst if "\u" in s] #get all the items containing @ in the list
	
	for i in range(0,len(matching)):
		tmsg = tmsg.replace(matching[i], "")	#lösche gefundene wörter
		
	
	tmsg = " ".join(tmsg.split())				#alle doppelten/zuviele leerzeichen entfernen

	if temptime >= datetime(1900,1,1,starthour,startmin) and temptime <= datetime(1900,1,1,endhour,endmin):
		cln_msg.append (date +" "+ msgtime +" "+ tmsg)		#liste mit msgs fängt bei 0 an 
 
 #mit find stelle suchen und mit replace ersetzen


result = set(line for line in cln_msg)
txt_out.write("\n".join(result))

txt_out.close()        #schließen der Datei

#answer = raw_input() #You should use "input()" in python 3.x, because python 3.x doesn't have a function named "raw_input".
