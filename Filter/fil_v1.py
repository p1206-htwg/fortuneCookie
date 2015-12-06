#!/usr/bin/python
# -*- coding: cp1252 -*-
import string

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

for i in range(0,len(beg_arr)):						#schleife von 0 bis Anzahl der Elemente im Array

	monthBeg = beg_arr[i]+19     			  		#String für Orientierungspunkt
	monthWord = txt_in[monthBeg:monthBeg+3]
	month = str(month_converter(monthWord))         #Monat als Zahl
	day = txt_in[monthBeg+4:monthBeg+6]             #Tag als Zahl
	year = txt_in[monthBeg+22:monthBeg+26]          #Jahr als Zahl
	time = txt_in[monthBeg+7:monthBeg+15]           #Zeit als hh:mm:ss
	date = day + "/" + month + "/" + year           #Datum als dd/mm/yyyy

	bom = beg_arr[i]+109              			    #begin of msg
	eom = end_arr[i]             				    #end of msg
	tmsg = txt_in[bom:eom]                          #twitter msg
	txt_out.write(date +" "+ time +" "+ tmsg + "\n")

txt_out.close()        #schließen der Datei

