import time
from relayr import Client
from relayr.dataconnection import MqttStream
try:
    import json
except ImportError:
    import simplejson as json

with open('apikeys.txt', 'r') as keyFile:
    keyFile = open('apikeys.txt', 'r')
    CLIENT_TOKEN = keyFile.readline().rstrip()
    DEVICE_ID = keyFile.readline().rstrip()
keyFile.closed

c = Client(token=CLIENT_TOKEN)
dev = c.get_device(id=DEVICE_ID)
def mqtt_callback(topic, payload):
    print('%s %s' % (topic, payload))
stream = MqttStream(mqtt_callback, [dev])
stream.start()
time.sleep(10)
stream.stop()




#example code where I scraped json to see how to do that
# sound = twitter.statuses.user_timeline.tweets(screen_name="amandapalmer", since_id = int(readData),
#                                                    exclude_replies = "true", include_rts = "false")
#
# #step through list of last tweets
# for i in lastTweets:
#     #strip the text out of the json of the tweet
#     thisTweet = i['text']

