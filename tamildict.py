#!/usr/bin/python2.4
# coding=UTF-8
#
#=BEGIN E2T DICTIONARY GPL
#
# This file is part of the tamil dictionary terminal.
#
# Copyright(c) 2011 POTI, Inc.
# http://www.sathia27.wordpress.com
#
# This file may be licensed under the terms of of the
# GNU General Public License Version 2 (the ``GPL'').
#
# Software distributed under the License is distributed
# on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
# express or implied. See the GPL for the specific language
# governing rights and limitations.
#
# You should have received a copy of the GPL along with this
# program. If not, go to http://www.gnu.org/licenses/gpl.html
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#=END E2T DICTIONARY GPL
#
import urllib2
from BeautifulSoup import BeautifulSoup
try:
    def alphabets():
        """Here get all words, listed by alphabet which was entered by user"""
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
        """Here get meaning of word in tamil, for word that was entered by user"""
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
                    for i in li:
                         total_string += i
                         total_string += " "
                print total_string
            except KeyboardInterrupt:
                print "\n\nQuitting!!"
                break 
            except:
                print "Sorry!! given word %r not found" %word
                print " or some internet connection!!"
    c = raw_input("Enter \n '1' for see all words for given alphabets \n '2' to get meaning of word in tamil\nEnter choice: ")
    if c == "1":
        alphabets()
    if c == "2":        
        words()
        
except KeyboardInterrupt:
   print "\n\nQuitting!!"
