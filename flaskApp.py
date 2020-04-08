from flask import Flask, request, make_response, Response
from twilio.twiml.messaging_response import MessagingResponse
from db import ResponsesDB
from messaging import Message
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sms_reply():
    user_message = request.form['Body']

    twml = MessagingResponse()
    tmsg = Message()
    tmsg.get_last_message()


    if user_message.strip().lower() == 'cog':
        twml.message('-\n\nWelcome Bainet!')
        twml.message(tmsg.twilio_responses['start'])

        response = make_response(str(twml))

        for resp in tmsg.twilio_responses:
            response.set_cookie(
                f'{resp}',
                value='',
                expires=0
            )

        return response
    elif user_message.strip().lower() == 'ok':
        # check if all responses are filled in

        saved_cookies = dict(request.cookies)
        filled_responses = {key: saved_cookies[key] for key in saved_cookies if '$' not in key}
        print(filled_responses)

        if len(filled_responses) == 9:
            rdb = ResponsesDB()

            rdb.response_values.update(filled_responses)
            rdb.insert_into_db()

            twml.message('-\n\nReport sent, thank you. Goodbye!')
            return str(twml)
        else:
            twml.message('-\n\nSomething went wrong. Text "cog" to restart report.')
            return str(twml)
    else:
        twilio_response = tmsg.last_twilio_message.split()[-1][:-1]
        # the twilio response comes from the dict with last_message (key), response(value) pairs in messaging.py

        if twilio_response in tmsg.twilio_responses:
            print(twilio_response)
            print(user_message)
            print('========================================')

            twml.message(tmsg.twilio_responses[twilio_response])

            response = make_response(str(twml))
            expires = datetime.utcnow() + timedelta(hours=1)
            response.set_cookie(
                f'{twilio_response}',
                value=user_message,
                expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT')
            )

            return response
        else:
            # program comes here when done reporting
            # user may or may not respond

            twml.message("-\n\nWelcome. Text 'cog' for report.")

            response = make_response(str(twml))

            for resp in tmsg.twilio_responses:
                response.set_cookie(
                    f'{resp}',
                    value='',
                    expires=0
                )

            return response


if __name__ == '__main__':
    app.run(debug=True)