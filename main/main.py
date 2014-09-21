#    ROOT_BOT 1.5
#    (C) 2014 root_user, Svetlana A. Tkachenko
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


import socket
import sys
import random
import time
server = "irc.esper.net"       
channel = "#test1234"
botnick = "root_bot"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
print "connecting to:"+server
# Connect
irc.connect((server, 6667))
# Register - send NICK and USER
irc.send("NICK "+ botnick +"\n")
print('Sent NICK')
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :I am a bot! \n")
print('Sent USER')

# Loop
while 1:
   time.sleep(1);
   # Receive
   text=irc.recv(2040)
   # Print to console if something is received
   if(text):
       print text
   # Pong
   if text.find('PING') != -1:                         
      irc.send('PONG ' + text.split() [1] + '\r\n')
      print('Ponged to the server')
   # Join channels on 001 numeric
   if text.find('001') != -1:
       irc.send("JOIN "+ channel +"\n")        #join the chan
       print("Sent JOIN\r\n")
   # Say Something
   if text.find(':!say') !=-1: 
       t = text.split(':!say') 
       to = t[1].strip() 
       irc.send('PRIVMSG '+channel+' :' + str(to) +'\r\n')
   # Roll dice
   if text.find(':!dice') !=-1: 
       print('Found valid command DICE')
       rand=random.randrange(1,12)
       rand=str(rand)	#convert to string, python doesn't like it when strings/numbers are mixed.
       irc.send('PRIVMSG '+channel+' :I rolled a ' + rand + '!\r\n')
