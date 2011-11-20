#!/usr/bin/python2.4
# coding=UTF-8
import urllib2
from BeautifulSoup import BeautifulSoup
import re
import codecs
import textwrap
try:
    def alphabets():
        while True:
            try:
                alphabet = raw_input("Enter the alphabet(eg. 'a' or 'b' to get all words.. Type 'quit' for quiting+): ")
                if alphabet == "quit":
                    print "\nQuiting!!!\n"
                    break
                url = "http://ta.wiktionary.org/wiki/சிறப்பு:PrefixIndex/"+alphabet
                req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
                con = urllib2.urlopen( req )
                soup = BeautifulSoup(con)
                all_words = soup.find("table", {"id" : "mw-prefixindex-list-table"}).findAll("a")
                print "="*40
                print "Words listed for Alphabet %r" %alphabet
                print "="*40+"\n"
                for i in all_words:
                  print i.contents[0]
            except KeyboardInterrupt:
               print "\n\nQuitting!!"
               break 
            except:
                print "Sorry!! given alphabet %r not found" %alphabet
                print " or some internet connection!!"          
    def words():
        while True:
            try:
                word = raw_input("Enter the word:")
                url = "http://ta.wiktionary.org/wiki/"+word
                print url
                req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
                con = urllib2.urlopen( req )
                soup = BeautifulSoup(con)
                meaning_of_word = soup.find("div", {"class":"mw-content-ltr"})
                ul = meaning_of_word.findAll("ul")[1]
                total_string = ''
                for li in ul.findAll(text=True):
                    #dedented_text = textwrap.dedent(li).strip()
                    #print textwrap.fill(dedented_text,width=200)
                    for i in li:
                         total_string += i
                         total_string += " "
                print total_string
            except KeyboardInterrupt:
               print "\n\nQuitting!!"
               break 

    c = raw_input("Enter \n '1' for see all words for given alphabets \n '2' to get meaning of word in tamil\nEnter choice: ")
    if c == "1":
        alphabets()
    if c == "2":        
        words()
        
except KeyboardInterrupt:
   print "\n\nQuitting!!"
