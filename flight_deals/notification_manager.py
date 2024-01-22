from twilio.rest import Client

TWILIO_SID = "AC2bba1184eb547c022d53369b64d576a4"
TWILIO_AUTH_TOKEN = "a18681623a9c22efd8b742c9f5425ae9"
TWILIO_VIRTUAL_NUMBER = "+16073884959"
TWILIO_VERIFIED_NUMBER = "+917406279538"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

        print(message.sid)