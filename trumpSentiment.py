import tweepy
from textblob import TextBlob
import sys

# This will be a list with names of companies with stocks
Stocks = []

#Stuff for authenticating twitter

# Print method for different language formats. 
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

consumer_key = 'mkX9OKKoKZjG7JNwxxVAEiLLT'
consumer_secret = 'BQTtBEAwWXhkaullELpPRODOZpg5TjKnsYXp38th8rrkvFvbMP'

access_token = '474211753-GGA3VRgznjCtvbaCXMgF3BxAPuTa5bdaKZnqwkxM'
access_token_secret = 'LgWIU4L4ApmRTsH6gmL3QDp3YkSlF1ehuFIM0kxAq0b8K'

#Authentication step
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

# Not a fittin name, but here we take the most recent tweets
# Then we check them up agains our list of tweets to see if the tweet is new
# If the tweet is new we write it to a new file along with the Sentiment analysis
def searchTweets():
	public_tweets = api.search('Trump')
	trump_tweets = api.user_timeline(screen_name = 'realDonaldTrump',count=10)
	if checkifExists(trump_tweets[0].text) != True:
		analysis = TextBlob(trump_tweets[0].text)
		line = trump_tweets[0].text + ": " + str(analysis.polarity)
		sendToFile(line)
	else:
		print("This tweet already exists")

	# Just some code for debugging in terminal - REMOVE LATER
	#for tweet in trump_tweets:
	#	print("_______________________________________________________")
	#	uprint(tweet.text)
	#	analysis = TextBlob(tweet.text)
	#	uprint("The analysis polarity is %s" % str(analysis.polarity))
	#	print("_______________________________________________________")

# We write the tweet and analysis to our file, and make a new line
def sendToFile(content):
	fileName = 'Tweet_Sentiment.txt'
	target = open(fileName,'w')
	target.write(content)
	target.write("\n")
	target.close()

# Checks if the tweet already existist in our textFile.
# If it exists then we return true, if not we return false.
def checkifExists(content):
	fileName = 'Tweet_Sentiment.txt'
	target = open(fileName)
	value = target.readline()
	count = 0
	for x in range (0,4):
		if value[x] == content[x]:
			count += 1
		else:
			break
	if(count==4):
		return True
	else:
		return False

searchTweets()