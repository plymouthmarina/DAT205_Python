import twitter
import datetime
import time
import urllib2
from _codecs import encode
from BeautifulSoup import BeautifulSoup

# Get the timestamp.
format = "%a %b %d %H:%M:%S %Y"
today = datetime.datetime.today()
print 'Now     :', today
s = today.strftime(format)
print 'strftime:', s

#Load in my keys and secrets from the credentials file into a list.
file = open('C:\Users\Marina\Documents\LiClipse Workspace\TwitterAPI\TwitterCredentials.txt')
cred = file.readline().strip().split(',')

api = twitter.Api(consumer_key=cred[0], consumer_secret=cred[1], access_token_key=cred[2], access_token_secret=cred[3])

print api.VerifyCredentials()

# Open and read the History file.
f = open('C:\Users\Marina\AppData\Local\Google\Chrome\User Data\Default\Current Session', 'rb')
data = f.read()

print(data)
f.close()

print(data.find('http'))

# Specify substring start.
startindex = data.rfind('http')

# Specify substring end.
endindex = data.find(chr(0),startindex)

data2 = data[startindex:endindex]

print(data2)

# Acquire the title of the last viewed page.
soup = BeautifulSoup(urllib2.urlopen(data2))
soupTitle = soup.title.string

print soupTitle

# Publish a status on Twitter
def publishStatus():
    myStatus = api.PostUpdate('I absolutely love ' + soupTitle)
    print (myStatus)
   
while True:
    publishStatus()
    time.sleep(3600)
