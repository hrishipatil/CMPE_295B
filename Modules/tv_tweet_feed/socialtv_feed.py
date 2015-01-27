#python script to fetch and store(JSON format) social tv feed for tv shows using tweepy 
#Test search : Fetches tweets for the tv shows 
#Source code reference:http://sentdex.com
#Refer:http://sentdex.com/sentiment-analysisbig-data-and-python-tutorials-algorithmic-trading/how-to-use-the-twitter-api-1-1-to-stream-tweets-in-python/ 
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

# Please refer your twitter app details and insert the values below
ckey=''
csecret=''
atoken=''
asecret=''

class listener(StreamListener):
    def on_data(self,data):
        try:
            print data
        
            #storing(appending) the data in twitDB.csv file
            saveFile=open('twitDB.csv','a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException,e:
            print 'failed ondata,',str(e)
            time.sleep(5)     
    
    def on_error(self,status):
        print status

auth= OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=["tvshows"])
#try replacing the above tracking string with any other search string
# like if you want feed for the tv show "The Mentalist", just replace the above string with "#TheMentalist"                  