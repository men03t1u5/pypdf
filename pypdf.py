#!/usr/bin/python

import os


os.system('clear')


#Uncomment for sound intro
#os.system('play -n -q synth pl G2 pl B2 pl D3 pl G3 pl D4 pl G4 \
               #delay 0 .05 .1 .15 .2 .25 remix - fade 0 4 .1 norm -1')




#Uncomment for sound effect	
#os.system('play -q -n -c1 synth sin %-8 sin %-5 sin %-1 sin %-12 fade h 0.1 1 0.1')
#os.system('clear')
a = "\t"
print (a * 7) + "|"
print (a * 7) + "|"
print "A Stupid Script for Shell Lovers\t\t\t|\n" + (a * 7 )+"|" +"\n"+(a * 7) + "|"
print (a * 7) + "|"
print (a * 7) + "|"

print "Required:\t\t\t\t\t\t|\n- sudo apt-get install pdftohtml\t\t\t|\n- sudo apt-get install elinks\t\t\t\t|"
print "Usage: python pypdf.py\t\t\t\t\t|"
print "Author: MEN03T1U$\t\t\t\t\t|"
print "Brought to you by: NAHC\t\t\t\t\t|\n"+(a * 7) + "|"+"\n"+(a * 7) + "|"+"\n\t\t\t\t\t\t\t|\n\t\t\t\t\t\t\t|\n\t\t\t\t\t\t\t|"
print "========================================================"
cho = raw_input("Pdf file to read on shell>")


print "\n\nBuilding your file.\nThis may take a few secs"
os.system("pdftohtml -stdout "+ cho + "> my.pdf.html; elinks my.pdf.html")


