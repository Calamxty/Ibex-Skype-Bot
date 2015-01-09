""" These you can edit however you want. """

name = "Ibex" #The bot's tag. (Ex: "[Ibex]: This is a message!")

admin = ['echo123','skype.name'] #Add as many as you want. These are admins that ARENT the bot account

timerGoal = '168' #By default the timer's goal is set to a week. (Ex: 0/168 HOURS)

weatherKey = '' #Get one from http://www.wunderground.com/ for weather API (XML)

""" These you can edit, but would recommend to leave alone """

blacklist = [] #You can add words you can black list. The users will be kicked if they used these words.

welcomeMSG = ['hi','hii','hiii','hiiii','hello','hey','heyy','heyyy','heyyyy','heyyyyy','hii','hola','helloo','helllo','hellloo','sup','supp','yo','yoo','yooo','yoooo','yooooo','watsup','whats up','holaa','oi','greetings'] #You can add more if you want.

afkMSG = ['brb','be right back','!afk','afk','gtg','g2g','gotta go'] #You can add more if you want.

askResponses = ['Signs point to yes.','Yes.','Reply hazy, try again.','Without a doubt.','My sources say no.','As I see it, yes.','You may rely on it.','Concentrate and ask again.','Outlook not so good.','It is decidedly so.','Better not tell you now.','Very doubtful.','Yes - definitely.','It is certain.','Cannot predict now.','Most likely.','Ask again later.','My reply is no.','Outlook good.','Don\'t count on it.','FIND OUT IN THE NEXT EPISODE OF DRAGON BALL Z']


""" These you don't need to edit and you probably shouldn't """
botAccount = '' #Leave blank. It automatically detects it.
afkList = [] #Leave Alone, use !afk or type "brb" or "be right back" to be marked as AFK
timer = '0' #This is for the call timer. Set it by doing !timer [number]
""" These are functions. Don't fuck with this shit, yo. """
import hashlib,os,random,re,urllib2
#Thanks to my nigga AzuTaki for a better method of getting titles and the isUP command.
def getBetween(source, start, stop):
	data = re.compile(start + '(.*?)' + stop).search(source)
	if data:
		found = data.group(1)
		return found.replace('\n', '')
	else:
		return False
def getCleanURL(url):
	cleanURL = url.replace('https://', '', 1)
	cleanURL = cleanURL.replace('http://', '', 1)
	cleanURL = cleanURL.replace('www.', '', 1)
	cleanURL = 'http://' + cleanURL
	return cleanURL
def getTitle(url): 
	try:
		source = urllib2.urlopen(url).read()
		title  = getBetween(source, '<title>', '</title>')
		return title
	except:
		return False
def isUP(url):
	try:
		source = urllib2.urlopen('http://www.downforeveryoneorjustme.com/' + url).read()
		if source.find('It\'s just you.') != -1:
			return 'Website Responsive.'
		elif source.find('It\'s not just you!') != -1:
			return 'Website seems to be down.'
		elif source.find('Huh?') != -1:
			return 'Invalid Website. Try again.'
		else:
			return 'UNKNOWN'
	except:
		return 'UNKNOWN ERROR'