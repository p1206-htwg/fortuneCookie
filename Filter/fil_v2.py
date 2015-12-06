#!/usr/bin/python
# -*- coding: cp1252 -*-

#---months to number converter---
def month_converter(monthWord):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(monthWord) + 1

txt_in = open('TwitterData-10_11_2015_11_28_38.txt').read()            		#lesen der Datei
txt_out = open("clean_twitter.txt", "w")      		#schreiben der Datei


#Ein Array mit dem Index für Anfang und Ende aller twitter msgs in der txt file wird erstellt
beg_arr = [n for n in xrange(len(txt_in)) if txt_in.find('{"created_at', n) == n]
end_arr = [n for n in xrange(len(txt_in)) if txt_in.find('","source":"', n) == n]


for i in range(0,len(beg_arr)):						#schleife von 0 bis Anzahl der Elemente im Array

	txt_out.write(txt_in[beg_arr[i]+23:beg_arr[i]+25] + "/" + str(month_converter(txt_in[beg_arr[i]+19:beg_arr[i]+22])) + "/" + txt_in[beg_arr[i]+41:beg_arr[i]+45] +" "+ txt_in[beg_arr[i]+26:beg_arr[i]+34] +" "+ txt_in[beg_arr[i]+109:end_arr[i]] + "\n")

txt_out.close()        #schließen der Datei

