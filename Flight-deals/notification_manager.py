from twilio.rest import Client
MY_API_KEY = "d91f5251328704ca3ad7d7da3ee0c024"
account_sid ="AC5376766960e1e6d93cd4862503bdf524"
auth_token ="d6fcd6c0d26033f99c81b07cb6a3ad98"
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="+17088093573",
            to="+46793323636",
        )
        # Prints if successfully sent.
        print(message.sid)