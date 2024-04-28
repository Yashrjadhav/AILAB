import re
import random

responses = {
    r'(hi|hello|hey)': ['Hey there!', 'Hi, how can I help you?', 'Hello, what\'s up?'],
}

def respond(message):
    message = message.lower()
    for pattern, response_list in responses.items():
        match = re.match(pattern, message)
        if match:
            response = random.choice(response_list)
            if '{}' in response:
                response = response.format(*match.groups())
            return response
    return 'I\'m not sure how to respond to that.'

print('Hey there, I\'m Chatty, a friendly chatbot. Type "bye" or "exit" to leave the conversation.')
while True:
    message = input('> ')
    if message.lower() in ['bye', 'exit']:
        print('Bye for now! Take care.')
        break
    else:
        print(respond(message))
