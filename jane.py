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

            c.send("Let me google that for you: " + link + "")
        if e.text.startswith("$lookup"):

            user = e.text.replace("$lookup ", "")
            
            c.send("Lookup: [[User:" + user + "|User page]] - [[User talk:" + user + "|Talk page]] - [[Special:Contributions/" + user + "|Contributions]]")

        if e.text == "$love":
        
            c.send("I love you " + e.user + " ~<3")
        if e.text.startswith("$rule"):

            i = e.text.replace("$rule ", "")
            i = int(i) - 1

            if i > 9 or i < 0:

                c.send("No rule at this index!")
                return
            rules = [
                "Personal attacks, harassment, sexual harassment, insults or bullying.",
                "Racial bigotry, sexually degrading language, or other hate speech.",
                "Extreme use of profanity/cursing or directing it towards another user is not permitted.",
                "Violation of personal privacy. This includes revealing personal information about users (e.g. real name, location, age, gender, etc) and violating confidentiality on particular issues (such as issues asked to be kept confidential by other users or administrators).",
                "Linking to external sources, such as websites, which violate the aforementioned rules. Notably, publicly linking to websites such as Facebook or MySpace that violate personal privacy, is not permitted without prior consent from the user whose privacy might be violated.",
                "Trolling or general irritation or disruption of other users. This often includes, but is not limited to; excessive usage of capital letters, punctuation marks, deliberate distortions of the English language (such as \"133t\" or \"Dolan\" speak), and excessive usage of languages other than English. Making arrangements to troll or otherwise disrupt another chat room or service is not permitted in our chatroom. This does not prevent you from joining another chatroom, linking another chatroom, or encouraging others to visit if the topic of conversation is likely to be of interest.",
                "Being a dick. As a guideline, don't go out of your way to irritate others. (And especially do not try to test the admin's and/or chat moderator's patience and/or limits.) Vicious abuse is grounds for sanctions.",
                "Whining. Users who ask for something from another chat user and are refused it should not stoop to complaining. It is acceptable to be persistent, but in a mature manner.",
                "Discussion of real world issues and events is generally permitted. However, before raising any of these points or joining a discussion on these you should remember that your fellow chatters may hold strong views in these areas. Where a particular subject appears to be causing distress, offense, or is otherwise disrupting the ability for others to enjoy chat, a moderator at their discretion may direct that a conversation either be closed or moved into private chat. This may be done either by request to a mod, or by the mod's own initiative, when those factors are present. In the event of mods disagreeing to end a discussion, the decision to ends takes precedence unless there are more active mods who disagree with the decision than agree. Moderators should avoid closing discussions outside of a publicly made request when they are involved in the discussion (unless they are the only active mod).",
                "Spamming. The meaning should be obvious. Don't say the same thing six times because no one is responding to you. Don't keep yammering on about a subject nobody cares about. Meaningless and/or random posts can also be considered spam, alongside disruptive internet memes."
            ]

            c.send(rules[i])
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
