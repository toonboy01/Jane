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

class Jane(chatbot.ChatBot):

    def __init__(self, username, password, site):

        chatbot.ChatBot.__init__(self, username, password, site)

    def on_welcome(self, c, e):

        #Send welcome message
        c.send("Where is Mr. House?")

#Gather setup info
username = raw_input("Username: ")
password = getpass.getpass("Password: ")
subdomain = raw_input("Wiki: ")

#Site URL
wiki = "http://" + subdomain + ".wikia.com"

if __name__ == "__main__":

    jane = Jane(username, password, wiki)
    jane.start()
