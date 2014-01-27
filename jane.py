#!/usr/bin/python
# -*- coding: utf-8 -*-

##########################################################################
# Jane - A stweard bot for operation on Wikia wikis. 
#    Copyright (C) 2014  Benjamin Williams cataclysmicpinkiepie@gmail.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##########################################################################

import tybot
import chatbot
import getpass
import sys

"""
Wiki commands
These functions are called by the bot and perform 
site tasks.
"""
def query_user(user):

    """
    See if a user is in a certain rights group
    """
    global sysops

    #debug
    print sysops

    for name in sysops:
    
        if name == user:
        
            return True
            print "true"
        else:
        
            return False
            
"""
Chat bot
This class contains all of the code needed to operate 
the chat aspect of the bot. It also calls functions
from Wiki comands
"""
class Jane(chatbot.ChatBot):

    def __init__(self, username, password, site):

        chatbot.ChatBot.__init__(self, username, password, site)

    def on_welcome(self, c, e):

        #Send welcome message
        c.send("-ss-")

    def on_message(self, c, e):
        
        if e.text == "$info":

            c.send("I am Quality Control running the Jane software package written by [[User:Lil' Miss Rarity|my operator]].")
        if e.text == "$love":
        
            c.send("I love you " + e.user + " ~<3")
        if e.text == "$source":
        
            c.send("My source can be loacted here: https://github.com/DoctorWhooves/Jane")
        if query_user(e.user) == True or e.user == "Lil' Miss Rarity":
        
            if e.text == "$test":
            
                c.send("This is a sysop only command!")
            if e.text == "$quit":

                c.send("Now exiting...")
                sys.exit()

"""
Setup
Gather login information and pass it
to the required class methods
"""
username = raw_input("Username: ")
password = getpass.getpass("Password: ")
subdomain = raw_input("Subdomain: ")

#Site URL
wiki = "http://" + subdomain + ".wikia.com"
api = wiki + "/api.php"

#New Tybot object
tybot = tybot.tybot(username, password, api)

#Get list of admins
sysops = tybot.get_users_by_group("sysop")

#debug
print sysops

#Start chatbot
if __name__ == "__main__":

    jane = Jane(username, password, wiki)
    jane.start()
