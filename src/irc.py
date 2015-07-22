#################################################
#
# Blender Notifier 0.1 - IRC Module
# by Dalai Felinto
# Rio de Janeiro, Brazil
#
# dfelinto@yahoo.com
# http://blenderecia.orgfree.com
#
# CC, GPL, whatever, just give me some credit
# and email-me or send me a message in my Blog
# if you are using it (I would love to know) :)
#
# To use properly edit the configuration parameters
# until the "Function Start"
#
# 27th September 2008
#################################################
#
# Blender Notifier - IRC

# Set the frames that will trigger the script
frames = [4,10]

# Set the IRC configuration

network = 'irc.freenode.net'    # irc network address
port = 6667                     # irc port (usually 6667)

toNick = "yournickhere"             # your nickname (destinatary)
fromNick = "BN_" + str(toNick)  # don't need to change - ths user that will send the message

ircMsg = "We are in frame: "    # message, frame number automatically added in the end
ircDelay = 10                   # (5-10) pause in seconds to send the message
sendIRC = 1                     # 1 = send, 0 = no send (for testing)

    ################################
   #                              #
  #         Function Start       #
 #                              #
################################

import Blender
import socket
from time import sleep


def IRCConnect(toNick, fromNick, ircMsg, network, port):
    carryon = True
    IRCsocket = None

    try:
        IRCsocket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

    except socket.error, msg:
        print msg
        carryon = False

    if carryon == True:
        try:
            IRCsocket.connect ((network, port))

        except socket.error, msg:
            IRCsocket.close()
            IRCsocket = None
            carryon = False
            print msg

    if carryon == True:
        try:
            trash = IRCsocket.recv (4096)

            IRCsocket.send ( 'NICK %s\r\n'%fromNick )
            IRCsocket.send ( 'USER %s 0 * :Blender Notifier\r\n'%fromNick )
            IRCsocket.send ( 'PRIVMSG %s : %s.\r\n'%(toNick, ircMsg) )
            IRCsocket.send ( 'QUIT %s\r\n' )
            trash = IRCsocket.recv (4096)
            sleep(ircDelay) #to give enough time to complete the conexion

            IRCsocket.close()

        except socket.error, (errno, msg):
            print "IRC Exception %s %s while receiving "%(errno,msg)
            carryon=False

        else:
            print "IRC message sent:"
            print "["+ircMsg+"]"


    ################################
   #                              #
  #         Main Function        #
 #                              #
################################

if Blender.bylink:
    curFrame = Blender.Get("curframe")
    print curFrame
    if curFrame in frames:
        ircMsg += str(curFrame)
        if (sendIRC == 1):
            IRCConnect(toNick, fromNick, ircMsg, network, port)
        else:
            print "Working offline"


# ######################################
#
#   Thanks Jean-Baptiste PERIN for BZoo
#   Thanks for troubled and jesterKing
#   for the support in testing
#
# ######################################
