
import os
from twilio.rest import Client
from credentials import account_sid, auth_token

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12058824151',
                     to='+14088194119',
                 )

print(message.sid)
