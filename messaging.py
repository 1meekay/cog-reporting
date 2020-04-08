from twilio.rest import Client
import os

accountSID = os.environ.get('twilioAccountSID')
authToken = os.environ.get('twilioAuthToken')

class Message:
    def __init__(self):
        self.client = Client(accountSID, authToken)
        # self.last_twilio_message = self.get_last_message()
        self.last_twilio_message = None

        self.twilio_responses = {
            'Bainet': '-\n\nrevivals?',
            'revivals': '-\n\nvisits?',
            'visits': '-\n\nspecial_services?',
            'special_services': '-\n\nsermons?',
            'sermons': '-\n\npersonal_evangelism_meetings?',
            'personal_evangelism_meetings': '-\n\nlectures?',
            'lectures': '-\n\nworker_classes?',
            'worker_classes': '-\n\ncounseling_hours?',
            'counseling_hours': '-\n\nchoir_meetings?',
            'choir_meetings': '-\n\nReport sent, thank you!',
        }


    def get_last_message(self):
        last_twilio_message_sid = self.client.messages.list(from_='+18604510554')[0].sid
        self.last_twilio_message = self.client.messages.get(last_twilio_message_sid).fetch().body.split('\n')[-1]


    # def get_last_message(self):
    #     last_twilio_message_sid = self.client.messages.list(from_='+18604510554')[0].sid
    #     last_twilio_message = self.client.messages.get(last_twilio_message_sid).fetch().body.split('\n')[-1]
    #
    #     return last_twilio_message