from twilio.rest import Client

class VoiceAlertDispatcher:
    def __init__(self):
        self.account_sid = "{{TWILIO_ACCOUNT_SID}}"  # assumed to be securely stored
        self.auth_token = "{{TWILIO_AUTH_TOKEN}}"
        self.from_number = "+14159998888"  # replace with verified Twilio number
        self.to_number = "+19252397291"  # your confirmed number
        self.client = Client(self.account_sid, self.auth_token)

    def send_voice_alert(self, message):
        call = self.client.calls.create(
            twiml=f'<Response><Say>{message}</Say></Response>',
            to=self.to_number,
            from_=self.from_number
        )
        return call.sid

# Example call
dispatcher = VoiceAlertDispatcher()
dispatcher.send_voice_alert("🚨 This is Builder Core calling to notify you of a critical event.")