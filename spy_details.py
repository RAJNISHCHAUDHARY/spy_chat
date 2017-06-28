from datetime import datetime

#spy name list
class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#here is the block of who send the message
class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

#Here is the list of friends
spy = Spy('Rajnish', 'Mr.', 21, 4.7)
friend_one = Spy('Manish', 'Mr.', 4.5, 22)
friend_two = Spy('Jony', 'Mr.', 4.39, 23)
friend_three = Spy('Archit', 'Mr.', 4.95, 21)
friend_four = spy('sumit','Mr.',4.4,21)

friends = [friend_one, friend_two, friend_three, friend_four]