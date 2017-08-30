'''
I used the Twilio client which is a good platform.  You have to make an account online.  If you go with the free trial,
it will say something like 'From my Twilio trial:' before the actual message
'''

from twilio.rest import Client

accountSID = 'AC56459528c18755677dc4e268436c4eae'
authToken = '38872c3d6eecf4dd583e733213faa4fc'
myTwilioNumber = '+15715703472'
myCellPhone = '+15712328207'
message = 'Hi mom, this is bilal'

client = Client(accountSID, authToken)
message = client.messages.create(body='Hi Mom, this is Bilal', from_=myTwilioNumber, to=myCellPhone)