# Ibex-Skype-Bot
A Skype bot I used to work on. Recently got it to work again so figured I'd edit it a bit and upload it here

##Requirements:
- Skype4Py
	  - https://pypi.python.org/pypi/Skype4Py/
- BeautifulSoup 4.3.2
	  - https://pypi.python.org/pypi/beautifulsoup4/4.3.2
- Skype that works with Skype4Py (If on Windows)
	  - http://lmgtfy.com/?q=Skype+6.10.0.104 (Can't give you DL, but can point in right direction)

##Important Notes	: 
  I made this on my windows computer, but a few simple changes and I've had it run on Fedora 20 as well.
	I came across the issue of Microsoft disabling their chat API and changing the group chat to work differently,
	HOWEVER, I am able to use Skype 6.10.0.104 and get it to work. It doesn't work in group chats outright, though.
	It started off only working in private messages, until I decided to try to add a friend through private message, 
	creating a group that way, and the bot managed to work! It's a bit of effort, but to me it was worth it.
