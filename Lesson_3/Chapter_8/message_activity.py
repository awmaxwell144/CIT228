#message_activity.py

from messages import show_messages as show, send_messages as send
def show_messages(messages):
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello", "good morning", "how are you doing?"]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)