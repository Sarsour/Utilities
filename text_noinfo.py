'''
I used the Twilio client which is a good platform.  You have to make an account online.  If you go with the free trial,
it will say something like 'From my Twilio trial:' before the actual message
'''

from twilio.rest import Client

accountSID = 'XXX'
authToken = 'XXX'
myTwilioNumber = '+XXX'
myCellPhone = '+XXX'
message = 'Hi'

client = Client(accountSID, authToken)
message = client.messages.create(body='Hi', from_=myTwilioNumber, to=myCellPhone)