import tweepy
import time
from time import sleep
import datetime
import sys

consumer_key        = "***************************"
consumer_secret     = "**************************************************"
access_token        = "**************************************************"
access_token_secret = "**************************************************"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

search1  = ("#phdchat -filter:retweets AND -filter:replies")
search2  = ("#acwri OR #ecrchat OR #phdforum OR #phdadvice OR #phdlife OR #phdweekend OR #gradschool OR #phdgang OR #phdhelp OR #planningyourphd -filter:retweets AND -filter:replies")

running = True
while running == True:

    x=0
    y=0
    for tweet in tweepy.Cursor(api.search,
                               q=search1,
                               result_type="recent",
                               lang='en').items(1):

	if tweet.user.screen_name == "@dannyroyfl" or tweet.user.screen_name == "@floridabear88":
		print (tweet.user.screen_name)
		print ("avoiding spam users")
 		break

        if x==0:

	    print ("tweet content: ", tweet.text)
            print ("length of original tweet: ", len(tweet.text))
 
	    if "#bigdick" in tweet.text or "#bigcock" in tweet.text or "bigdick" in tweet.text or "bigcock" in tweet.text or "#testingjon" in tweet.text:
	        print "spam found"
	        break

            y+=1
            try:
		tweet.retweet()
		x+=1

	    except tweepy.TweepError as e:
		print (e)
		if 'Failed to send request' in e.reason:
		    time.sleep(240)
            except StopIteration:
		break

        if x==0:
            print "no luck with #phdchat, trying others.."
            y+=1
            for tweet in tweepy.Cursor(api.search,
                                       q=search2,
                                       result_type="recent",
                                       lang='en').items(1):

	        if tweet.user.screen_name == "@dannyroyfl" or tweet.user.screen_name == "@floridabear88":
		    print (tweet.user.screen_name)
		    print ("avoiding spam users")
 		    break

        	if x==0:

	   	    print ("tweet content: ", tweet.text)
                    print ("length of original tweet: ", len(tweet.text))
 
	   	    if "#bigdick" in tweet.text or "#bigcock" in tweet.text or "bigdick" in tweet.text or "bigcock" in tweet.text or "#testingjon" in tweet.text:
	                print "spam found"
			break
                try:
                    tweet.favorite()
		    tweet.retweet()
		    x+=1
                    y+=1

		except tweepy.TweepError as e:
		    print (e)
		    if 'Failed to send request' in e.reason:
		        time.sleep(240)
                except StopIteration:
                    break
                    

    if y == 2:
        time.sleep(360)
    elif y==3:
        time.sleep(540)
    else:
        time.sleep(180)
