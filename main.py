from spy_details import spy, Spy, ChatMessage, friend_one,friend_two,friend_three
from steganography.steganography import Steganography
from datetime import datetime
#from name_spy import spy
#list of the status messages
friends = [friend_one, friend_two, friend_three]
STATUS_MESSAGES = ['My name is Rajnish, Rajnish Chaudhary', 'Hii i am using spy chat messanger', 'Dont call only spy chat']

print "\t\t\t****Hello! Welcome in the secret chat messanger****"

question = "\t\t\t****Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)?**** "
existing = raw_input(question)

#Here be add our status
def add_status():
    updated_status_message = None

    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("\t\t\t****Do you want to select from the older status (y/n)?**** ")
#For default user only
    if default.upper() == "N":
        new_status_message = raw_input("\t\t\t****Please enter your new status**** ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1
#For select the status messages from the list
        message_selection = int(raw_input("\nPlease select status from the list "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Please enter  y or n.'
#For update your new status messages
    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message

#This function are create for add a new friend in the friends list
def add_friend():
    new_friend = Spy('', '', 0, 0.0)
#Here you give the new friend name
    new_friend.name = raw_input("***Please add your new friend's name:*** ")
    new_friend.salutation = raw_input("***What should want to you call Mr. or Ms.?***: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name
#Here you give the age of friend
    new_friend.age = raw_input("***Please enter the spy Age?")
    new_friend.age = int(new_friend.age)
#Here you give the rating of your friend
    new_friend.rating = raw_input("***Please provide the Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. Please provide valid name'

    return len(friends)

#This block are used to select a friend in the list
def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salutation, friend.name,
                                                                friend.age,
                                                                friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("***Choose from your friends***")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

#Here we now write a code to send a secret message to your friend
def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.png"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text, True)

    friends[friend_choice].chats.append(new_chat)

    print "***Your secret message image is ready!***"

#Here you can read the messages
def read_message():
    sender = select_a_friend()

    output_path = raw_input("***What is the name of the file?***")

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text, False)

    friends[sender].chats.append(new_chat)

    print "***Your secret message has been saved!***"

#Here we can read the older messages or communication of two friends
def read_chat_history():
    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)

def delete(friends):
            if len(friends) == 0:
                print "You have no friend currently"
            counter = 1
            for temp in friends:
                print"\n\t%d\t%s" % (counter, temp)
                counter = counter + 1
            select_friend = raw_input("\nSelect a friend :\t")
            select_friend = int(select_friend)
            i = len(friends)
            if i == 0:
                print "You have No friend to Delete\n"
            else:
                temp1 = select_friend
                temp = 0
                lis = []
                while temp1 < len(friends):
                    friends[temp1 - 1] = friends[temp1]
                    temp1 = temp1 + 1
                temp1 = 1
                while temp < len(friends) - 1:
                    lis.append(friends[temp])
                    print "\n\t%d\t%s" % (temp1, friends[temp])
                    temp = temp + 1
                    temp1 = temp1 + 1
                    friends = lis
            return friends
#Now be are able to do chat with spy
def start_chat(spy):
    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:

        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "***What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Delete friend \n 7.Close applications"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                elif menu_choice ==6:
                    delete()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'


if existing == "Y":
    start_chat(spy)
else:

    spy = Spy('', '', 0, 0.0)

    spy.name = raw_input("***Welcome to spy chat, you must tell me your spy name first***: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("***Should I call you Mr. or Ms.?***: ")

        spy.age = raw_input("***What is your age?***")
        spy.age = int(spy.age)

        spy.rating = raw_input("***What is your spy rating?***")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please add a valid spy name'