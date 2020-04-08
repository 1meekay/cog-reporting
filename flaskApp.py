from flask import Flask, request, make_response, Response
from twilio.twiml.messaging_response import MessagingResponse
from db import ResponsesDB
from messaging import Message
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sms_reply():
    # print('\n\n', request.form.to_dict(), '\n\n')

    user_message = request.form['Body']

    rdb = ResponsesDB()
    twml = MessagingResponse()


    tmsg = Message()
    tmsg.get_last_message()

    print('========================================')
    print('\n\nLast message:', tmsg.last_twilio_message, '\n\n')

    print('\n\nCOOKIES\n\n')
    print(request.cookies)
    print('\n\n')

    from pprint import pprint
    pprint(dict(request.cookies))
    # print(list(request.cookies.keys()))
    print('========================================')



    if user_message.strip().lower() == 'cog':
        twml.message('-\n\nWelcome Bainet!')
        twml.message(tmsg.twilio_responses['Bainet'])

        response = make_response(str(twml))

        for resp in tmsg.twilio_responses:
            response.set_cookie(
                f'{resp}',
                value='',
                expires=0
            )

        return response
        # return str(twml)
    else:
        twilio_response = tmsg.last_twilio_message.split()[-1][:-1]

        if twilio_response in tmsg.twilio_responses:
            print(twilio_response)
            print(user_message)
            print('\n')

            # rdb.insert(twilio_response, int(user_message))

            twml.message(tmsg.twilio_responses[twilio_response])

            response = make_response(str(twml))
            expires = datetime.utcnow() + timedelta(hours=1)
            response.set_cookie(
                f'{twilio_response}',
                value=int(user_message),
                expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT')
            )

            return response

            # return response

            # if twilio_response == 'choir_meetings':
            #     pass

                # print(rdb.response_values)
                # rdb.insert_into_db()

                # '''
                # THE ISSUE IS THAT ResponsesDB object GETS INITIALIZED EVERY TIME A MESSAGE IS SENT
                #
                # remedy with database?
                # need intermediate storage..
                # cookies?
                # '''
        else:
            # program comes here when done reporting

            # twml.message(f"-\n\nMy last message was '{tmsg.last_twilio_message}'")
            # twml.message(f"-\n\nMy last message was '{tmsg.last_twilio_message.split()[-1][:-1]}'")
            twml.message("-\n\nWelcome. Text 'cog' for report.")

            return str(twml)




    # if tmsg.last_twilio_message == '---DONE HERE---':
    #     # process values?
    #     db.insert_into_db()
    # else:
    #     twilio_response.message(tmsg.twilio_responses[tmsg.last_twilio_message])
    #     # twilio_response.message(tmsg.twilio_responses[tmsg.last_twilio_message.split()[1][:-1]])
    #     print(tmsg.last_twilio_message.split()[1][:-1])
    #     # db.insert(user_message)


if __name__ == '__main__':
    app.run(debug=True)
