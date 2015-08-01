#!/usr/bin/python

import os


os.system('clear')


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


