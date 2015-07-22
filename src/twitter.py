#################################################
#
# Blender Notifier 0.1 - Twitter Module
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
# Blender Notifier - Twitter

# Set the frames that will trigger the script
frames = [5,10]


# Twitter username and password
twitterUser = ""    # your twitter account login
twitterPass = ""    # your twitter password
twitterMsg  = "We are in Frame: " # message, the frame number is added later

sendTwitter = 1             #1 = send, 0 = no send (for testing)

    ################################
   #                              #
  #         Function Start       #
 #                              #
################################

import urllib2, urllib, base64
import Blender

# Generate authentication string to send in HTTP request header
def tweet(curframe):
    try:
        auth = base64.encodestring("%s:%s" % (twitterUser, twitterPass)).strip()
        urllib2.urlopen(urllib2.Request("http://twitter.com/statuses/update.json",
            urllib.urlencode({"status":twitterMsg}), {"Authorization": "Basic %s" %auth}))

    except:
        print "We couldn't sent the message at frame " + str(curframe)

    else:
        print "Twitter message sent:"
        print "["+twitterMsg+"]"

if Blender.bylink:
    curFrame = Blender.Get("curframe")
    print curFrame
    if curFrame in frames:
        twitterMsg += str(curFrame)

        if (sendTwitter == 1):
            tweet(curFrame)
        else:
            print "Working offline"
            print twitterMsg


# Twitter Plug-in by Ryan Paul
# http://arstechnica.com/journals/linux.ars/2007/08/29/send-twitter-updates-from-xchat-using-python
