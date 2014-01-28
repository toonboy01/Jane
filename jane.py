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

    is_true = False
 
    for i in range(len(sysops)):
    
        if sysops[i] == user:
        
            is_true = True
    return is_true
            
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

        """
        User commands
        """
        if e.text == "$info":

            c.send("I am Quality Control running the Jane software package written by [[User:Lil' Miss Rarity|my operator]].")
        if e.text.startswith("$lmgtfy"):

            query = e.text.replace("$lmgtfy ", "")
            querystring = query.replace(" ", "+")

            link = "http://lmgtfy.com/?q=" + querystring

            c.send("Let me google that for you: " + query + "")
        if e.text.startswith("$lookup"):

            user = e.text.replace("$lookup ", "")
            
            c.send("Lookup: [[User:" + user + "|User page]] - [[User talk:" + user + "|Talk page]] - [[Special:Contributions/" + user + "|Contributions]]")

        if e.text == "$love":
        
            c.send("I love you " + e.user + " ~<3")
        if e.text == "$rules":

            c.send("Please read the [[Fallout Wiki:Chat#Chat_rules|chat rules]]")
        if e.text == "$source":
        
            c.send("My source can be loacted here: https://github.com/DoctorWhooves/Jane")

        """
        Sysop only commands
        """
        if query_user(e.user) == True or e.user == "Lil' Miss Rarity":
        
            if e.text == "$quit":

                c.send("Now exiting...")
                sys.exit()

"""
Setup
Gather login information and pass it
to the required class methods
"""
username = sys.argv[1]
password = sys.argv[2]
subdomain = sys.argv[3]

#Site URL
wiki = "http://" + subdomain + ".wikia.com"
api = wiki + "/api.php"

#New Tybot object
tybot = tybot.tybot(username, password, api)

#Get list of admins
sysops = tybot.get_users_by_group("sysop")

#Start chatbot
if __name__ == "__main__":

    jane = Jane(username, password, wiki)
    jane.start()
