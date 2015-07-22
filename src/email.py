#################################################
#
# Blender Notifier 0.1 - Email Module
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
# Blender Notifier - Email

# Set the frames that will trigger the script
frames = [3,5]

def sendEmail(curFrame):

    ################################
   #                              #
  #     Start of configuration   #
 #                              #
################################

    # Script Options:

    sendEmail = 1           # 0 = don't send email , 1 = send email
    noSpam = 1              # 0 = nothing happens, 1 = include in the message some random text

    # Configure SMTP:

    smtpServer = 'smtp.gmail.com'   # your smtp server address (e.g. smtp.gmail.com)
    smtpPort = 587                  # smpt port, the standard is 25 (but gmail is 587)
    smtpUser = 'youruser@gmail.com' # username (sometimes with @domain, sometimes without)
    smtpPass = 'yourpassword'       # password

    # Email settings:

    emailSender = 'youremail@gmail.com'                         # sender email
    emailRecipients = ['email1@yahoo.com','email2@yahoo.com'] # list of destinatary
    emailSubject = 'Render almost ready :) Current Frame: ' + str(curFrame) 

    emailText = "Hey, I'm sending this email from Blender.\n\n"\
                "Cool !!!!\n\n"\
                "It¿¥s a report of the progress of a render, a particle baking,\n"\
                "a fluid simulation baking or other use I didn't think"\
                "\n\n"\
                "See you\n"\
                "Dalai"



    emailMsg = "To: " + emailRecipients[0] + "\n"\
            "Subject: " + emailSubject + "\n"\
            "\n" + emailText

    ################################
   #                              #
  #     Function Start           #
 #                              #
################################

    import smtplib # you need to install full Python Version
    import random # to create the noSpam message

    #emailMsg = open('mssg.txt', 'r').read()

    if noSpam == 1:

        spamMSG = []

        for i in emailText:
            spamMSG.append(i)

        spamMSG.sort()
        random.shuffle(spamMSG)

        newText = ""
        for i in range(len(spamMSG)):
            newText += spamMSG.pop()

        emailMsg += "\n"*5
        emailMsg += "<End of Message>\n"
        emailMsg += "<Please ignore the rest of the message>\n\n"
        emailMsg += newText

    if sendEmail == 1:
        try:
            session = smtplib.SMTP(smtpServer,smtpPort)
            session.ehlo()
            session.starttls()
            session.ehlo()
            session.login(smtpUser, smtpPass)

            smtpResult = session.sendmail(emailSender, emailRecipients, emailMsg)

            session.close()
        except:
            print "Fail to send the email"

        if smtpResult:
            errstr = ""
            for recip in smtpResult.keys():
                errstr = """Could not delivery mail to: %s

        Server said: %s
        %s

        %s""" % (recip, smtpResult[recip][0], smtpResult[recip][1], errstr)
            raise smtplib.SMTPException, errstr

        print "Email message sent:"
        print "["+emailMsg+"]"

    ################################
   #                              #
  #         Main Function        #
 #                              #
################################

import Blender

if Blender.bylink:
    curFrame = Blender.Get("curframe")
    if curFrame in frames:
        sendEmail(curFrame)
