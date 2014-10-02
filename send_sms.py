from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect
from flask import Markup
from flask import render_template
import twilio.twiml
from twilio.rest import TwilioRestClient
from pprint import pprint
# Your Account Sid and Auth Token from twilio.com/user/account
def sms():

	resp = twilio.twiml.Response()
    	msg = str(request.values['Body'])
    	l = msg.split("#")
    	a = l[0]
    	mid = " @ aisle "
    	x = l[1]
    	w = " says "
    	y = l[2]
	print l
	account_sid = "AC165eff86cf356130f0b5ed4f928fbcd4"
	auth_token = "73ee93adbf5031b083bf7df9a2e143be"
	client = TwilioRestClient(account_sid, auth_token)
	message = client.messages.create(body="Hey! "+x +mid +a +w +y,
	to="+16123561005", # Replace with your phone number
	from_="+17639511604") # Replace with your Twilio number
	print message.sid
	#return message.sid

if __name__ == "__main__":
    app.run(debug=True)
