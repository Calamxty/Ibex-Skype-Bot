""" 
Creator			: @Calamxty (Email/XMPP: iAmCalamity@riseup.net)

Description		: Ibex Skype Bot was basically made out of boredom. A side-project I'd work on whenever I'd Skype with people.
				: It's a pretty simple bot. Some of the stuff I did could've been done more efficiently, however, I don't care.
				: I simply just added stuff whenever I'd come up with an idea of a function/feature. 
"""
import os,sys,time,Skype4Py,urllib2,config
from bs4 import BeautifulSoup
from random import choice
s = Skype4Py.Skype()
s.Attach() #Attach to Skype. Make sure to accept permissions from Skype client!
config.botAccount = s.CurrentUserHandle
tag = "["+config.name+"]: "
os.system('cls')
print config.name+" bot currently running on Skype account: "+config.botAccount+"\nIf any errors occur, they will be printed here."
def inMSG(checklist, messagelol):
    return set(checklist).intersection(messagelol.split())
def Ibex(Message, Status):
	chat = Message.Chat
	members = chat.MemberObjects
	msg = Message.Body
	send = Message.Chat.SendMessage
	sAlias = Message.FromDisplayName
	sUsername = Message.FromHandle
	roles = ['MASTER','CREATOR','ADMIN']
	for name in members:
		if inMSG(roles,name.Role):
			config.admin.append(name.Handle)
#Handling messages and AFK System and link titles
	if Status == 'SENT' or (Status == 'RECEIVED'):
		if inMSG(config.afkList, sUsername):
			config.afkList.remove(sUsername)
			config.afkList.remove(sAlias)
			send(tag+"Welcome back, %s! You're no longer marked as AFK." % sAlias)
		if inMSG(config.welcomeMSG, msg.lower()) and sUsername != config.botAccount:
			send(tag+"Hello, %s!" % sAlias)
		if inMSG(config.afkMSG, msg.lower()):
			config.afkList.append(sUsername)
			config.afkList.append(sAlias)
			send(tag+"You are now marked as AFK, %s!\nUsers who try to contact you will be notified.\nType anything to be marked as back." % sAlias)
		if inMSG(config.afkList, msg.lower()):
			send(tag+"That person is AFK.")
		if inMSG(config.blacklist, msg.lower()):
			send(tag+"Do not say that word!")
			time.sleep(1)
			send("/kick %s" % sUsername)
		if msg.startswith('https://') or msg.startswith('http://') or msg.startswith('www.'):
			url = config.getCleanURL(msg)
			titleCheck = config.getTitle(url)
			titleCheck = titleCheck.replace('', '', 1)
			send('[Title]: ' + titleCheck)
#Commands
		if msg.lower() == '!ping':
			send(tag+"PONG. Connection active. (dance)")
		if msg.lower() == '!help':
			help = open(os.getcwd() + '\\db\\help.txt','r')
			send(help)
		if msg.lower() == '!rules':
			rules = open(os.getcwd() + '\\db\\rules.txt','r')
			send(rules)
		if msg.lower() == '!commands':
			commands = open(os.getcwd() + '\\db\\cmds.txt','r')
			send(commands)
		if msg.lower() == '!info':
			if chat.Topic == '':
				chatName = chat.Name
			else:
				chatName = chat.Topic
			send(tag+'Current Call Timer: '+config.timer+'/'+config.timerGoal+' HOURS\nTopic: '+chatName+'\nCall Status: '+callStatus+'\nMessage Count: ' + str(len(chat.Messages))+'\nMember Count: '+str(len(chat.Members)) +'\nBot Account: '+config.botAccount)
		if msg.lower().startswith('!timer '):
			timer = msg.replace('!timer ','',1)
			config.timer = timer
			send('/topic '+timer+'/'+config.timerGoal+' HOURS | Call Record: 125 Hours')
		if msg.lower() == '!time':
			send('Current Call Time: '+config.timer)
		if msg.lower().startswith('!ask '):
			question = msg.replace('!ask ','',1)
			response = choice(config.askResponses)
			send(tag+'Question Asked: '+question+'\n[Answer]: '+response)
		if msg.lower().startswith('!isup '):
			check = msg.replace('!isup ', '', 1)
			url = config.getCleanURL(check)
			send(tag + config.isUP(url))
		if msg.lower().startswith('!ping '):
			check = msg.replace('!ping ', '', 1)
			ping = urllib2.urlopen('http://api.hackertarget.com/nping/?q='+check).read()
			send(tag+ ping)
		if msg.lower().startswith('!tinyurl '):
			url = msg.replace('!tinyurl ', '', 1)
			url = config.getCleanURL(url)
			tiny = urllib2.urlopen('http://tinyurl.com/api-create.php?url=' + url).read()
			send(tag+tiny)
		if msg.lower().startswith('!trace '):
			ip = msg.replace('!trace ', '', 1)
			xml = urllib2.urlopen('http://freegeoip.net/xml/'+ip).read()
			ipinfo = BeautifulSoup(xml)
			send(tag+'Target: '+ip+' traced by '+senderDisplay+' ('+senderHandle+'). \n\nIP Address: %s' % ipinfo.ip.text+'\nCountry: %s' % ipinfo.countryname.text+'\nState: %s' % ipinfo.regionname.text+'\nCity: %s' % ipinfo.city.text+'\nZip Code: %s' % ipinfo.zipcode.text+'\nLatitude: %s' % ipinfo.latitude.text +'\nLongitude: %s' % ipinfo.longitude.text + '\nArea Code: %s' % ipinfo.areacode.text)
		if msg.lower().startswith('!weather '):
			if config.weatherKey != '':
				location = msg.replace('!weather ','',1)
				xml2 = urllib2.urlopen('http://api.wunderground.com/api/'+config.weatherKey+'/conditions/q/'+location+'.xml').read() 
				weather = BeautifulSoup(xml2)
				send(tag+'Weather information for '+location+' requested by '+senderDisplay+'\n\nLocation: %s' %weather.observation_location.city.text+'\nCurrent Temp: %s' % weather.temperature_string.text + ' | '+ weather.weather.text + '\n%s' % weather.observation_time.text)
			else:
				send(tag+'No weather key found. Please read/edit config.py')
		if msg == '!anime':
			anime = open(os.getcwd() + '\\db\\anime.txt','r').readlines()
			send('[Random Anime]: ' + choice(anime))
		if msg == '!movie':
			movie = open(os.getcwd() + '\\db\\movies.txt','r').readlines()
			send('[Random Movie]: ' + choice(movie))
		if msg.startswith('!topic '):
			topic = msg.replace('!topic ','',1)
			if topic.startswith('!'):
				send('Please do not start the topic with \'!\'. Thank you.')
			else:
				send('/topic '+topic+' | Call Record: 125 Hours')
				
#Admin Commands
	if Status == 'SENT' or inMSG(config.admin, sUsername):
		if msg.lower() == '!lock topic':
			send('/set options +TOPIC_AND_PIC_LOCKED_FOR_USERS')
		if msg.lower() == '!nuke':
			send('/topic Chat Nuked by %s' % sAlias)
			time.sleep(1)
			send('Chat being nuked in 5..4..3..2..1..')
			time.sleep(5)
			for name in members:
				kick = name.Handle
				if inMSG(config.admin,kick):
					pass
				else:
					send('/kick '+kick)
			send('Nuke successful. Admins left in the chat. Please type /leave')
		if msg.startswith('!kick '):
			kick = msg.replace('!kick ','',1)
			send('You are being kicked, '+kick)
			time.sleep(1)
			send('/kick '+kick)
		if msg.startswith('!ban '):
			ban = msg.replace('!ban ','',1)
			send('You are being banned, '+ban)
			time.sleep(1)
			send('/kickban '+ban)
			

s.OnMessageStatus = Ibex
while True:
    raw_input('')