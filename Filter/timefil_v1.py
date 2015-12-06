#!/usr/bin/python
# -*- coding: cp1252 -*-
from datetime import datetime, time


#---months to number converter---
def month_converter(monthWord):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(monthWord) + 1

txt_in = open('twitter.txt').read()            		#lesen der Datei
txt_out = open("clean_twitter.txt", "w")      		#schreiben der Datei


#Ein Array mit dem Index für Anfang und Ende aller twitter msgs in der txt file wird erstellt
beg_arr = [n for n in xrange(len(txt_in)) if txt_in.find('{"created_at', n) == n]
end_arr = [n for n in xrange(len(txt_in)) if txt_in.find('","source":"', n) == n]

#print len(beg_arr)									#Anzahl der Elemente im Array
#print len(end_arr)
cln_msg = []										#declare as  list

starthour = input('Filtern von[hh]:')
startmin = input('Filtern von[mm]:')
endhour = input('Filtern bis[hh]:')
endmin = input('Filtern bis[mm]:')

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
	tmsg = txt_in[bom:eom]                          #twitter msg
	
	temptime = datetime.strptime(msgtime, "%X")
	if temptime >= datetime(1900,1,1,starthour,startmin) and temptime <= datetime(1900,1,1,endhour,endmin):
		cln_msg.append (date +" "+ msgtime +" "+ tmsg)		#liste mit msgs fängt bei 0 an 
 

result = set(line for line in cln_msg)
txt_out.write("\n".join(result))

txt_out.close()        #schließen der Datei

#answer = raw_input() #You should use "input()" in python 3.x, because python 3.x doesn't have a function named "raw_input".
