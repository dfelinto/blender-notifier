# Blender Notifier

``This project started as Blender Notifier and was designed for Blender 2.49 as Script Links.
It will eventually be replaced by an addon for more recent Blenders.``

Original README
---------------
	
In this repository you will find three scripts:
	- BN_email
	- BN_irc
	- BN_twitter

1. Enable Script Links in your scene, and choose the script you want to use.
2. I suggest to use them either as FrameChange (for physic baking) or Render (for animations).
3. Change the configuration in the first lines of your script
4. Test it
5. Run it
6. Send me a commentary in my Blog (whatever your language is - or in Portuguese/Spanish/French/English)
7. That is it, enjoy it.


Know Issues:
	- the script is called in the beggining of the frame, before all calculations/rendering
	- the email Notifier takes too long
	- twitter API is outdated

History:
	This project started for fun. A long time ago I was setting a webpage in a server which PHP php_mail() function was disable. Therefore I created a socket connection with a smtp server to contourn this problem and it worked.

	After 8 years, I decided to go over this experience and try to send emails in Python using my favorite 3D application. After my first lines of code I realized that this project has some potential and I decided to expand it to send IRC messages.
	I downloaded BZoo, an open Blender project with a good IRC implementation and after a lot of tests (thanks jesterKing and troubled) I got it working.
	I was still looking forward for some challenge and Mike (Pan) suggested me to implement a Twitter interface as well... Well, why not?


Things I would like to do (but I decided to release earlier):

	- attach the last rendered frame or a screenshot in the email notification.
	-	create a common interface to select your Notifier system and add the password in run-time
	- MSN Notifier system
	- change the email Notifier to use socket library instead of smtplib. Why? Well, why not? I would like to recreate my original experience as closer as possible :)

Original implementation 2008
