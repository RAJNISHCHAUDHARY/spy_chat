#--------------------------------------------------Starting of project---------------------------------------------------------------------------

import sys      #Here we use import function to import other files information in  this page
from termcolor import colored,cprint
import colorama
colorama.init()
from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from datetime import datetime
print colored('|\t\t\t*******hello welcome to spy chat messenger*******\t\t\t ', 'red', attrs=['reverse', 'blink'])


#list of the status messages
STATUS_MESSAGES = ['My name is Rajnish, Rajnish Chaudhary', 'Hii i am using spy chat messanger', 'Dont call only spy chat']

print colored ("\t\t\t****Hello! Welcome in the secret chat messanger****",'green', attrs=['reverse','blink'])

question = "\t\t\t****Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)?**** "
existing = raw_input(question)

#---------------------------------------------------------Here be add our status-----------------------------------------------------------------
def new_user():

    spy_name = raw_input("\t\t******If you want to enjoy the chat on massenger then***** \n \t\tplease enter your name: ")
    spy_salutaions = raw_input("\t\tWhat should be call you MR or MS : ")

    if spy_salutaions.upper() == "MR":
        spy_name = (spy_salutaions+ " " + spy_name)
    elif spy_salutaions.upper() == "MS":
        spy_name =  (spy_salutaions + spy_name)


    else:
     print colored("\t\t****Invalid sir name*****",'red', attrs=['reverse','blink'])
     exit(-1)
   #variables initializations for more details of spy
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_age = raw_input ("\t\tPlease provide  your age ")
    print colored("\t\tHello " +spy_name+ " \t\tAge : "+ spy_age +".\n \t\t....Welcome to massenger....,", 'blue', attrs=['reverse', 'blink'])
    spy_rating =  raw_input ("\t\tPlease provide your rattings :")
    spy_rating = float(spy_rating)
    if spy_age > 12 and spy_age <50:

#welcome message based on their rattings,
          if spy_rating > 4.5:
            print("You are good one spy. ")
          elif spy_rating > 3.5 and spy_rating <=4.5:
            print ("You are the well spy. ")
          elif spy_rating >= 2.5 and spy_rating <=3.5:
            print("You can  do more  better....")
          else:
            print("We can always use someone in office to help...")

#make spy is online
          spy_is_online = True

    else:
        print ("\t\t\tAuthentications complete. \n\t\t\tWelcome :" + spy_name + " \n\t\t\tAge :  " + str(
            spy_age) + " \n\t\t\tand ratting : " + str(
            spy_rating)) + " \n\t\t\tYou are now online :"
#--------------------------------------------------------we use default user-----------------------------------------------------------------------
def default_user():

 print colored("\t\t\tspy_name : Rajnish", 'green', attrs=['reverse', 'blink'])
 print colored("\t\t\tspy_salutation: MR", 'white', attrs=['reverse', 'blink'])
 print colored("\t\t\tspy_age : 21", 'red', attrs=['reverse', 'blink'])
 print colored("\t\t\tspy_rating : 4.5", 'yellow', attrs=['reverse', 'blink'])
 print colored("\t\t\tspy_is_online: True", 'green', attrs=['reverse', 'blink'])

def add_status():
    updated_status_message = None

    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("\t\t\t****Do you want to select from the older status (y/n)?**** ")
#-------------------------------------------------------For default user only--------------------------------------------------------------------
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
#-------------------------------------------For select the status messages from the list---------------------------------------------------------
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

#--------------------------------This function are create for add a new friend in the friends list-----------------------------------------------
def add_friend():
    new_friend = Spy('', '', 0, 0.0)
#Here you give the new friend name
    new_friend.name = raw_input("***Please add your new friend's name:*** ")
    new_friend.salutation = raw_input("***What should want to you call Mr. or Ms.?***: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name
#Here you give the age of friend
    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)
#Here you give the rating of your friend
    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. Please provide valid name'

    return len(friends)

#----------------------------------This block are used to select a friend in the list--------------------------------------------------------------
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

#-------------------------------Here we now write a code to send a secret message to your friend--------------------------------------------------
def send_message():
    friend_choice = select_a_friend()
                                                             #Here we input the message or genrate a message which send to the other spy
    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    i=3
    while i>0:
        text = raw_input("What do you want to say? ")
        if len(text)<=100 and len(text)>0:                   #Here we maintain the aevrage number of chracter or word spoken by the spy


            Steganography.encode(original_image, output_path, text)

            new_chat = ChatMessage(text, True)

            friends[friend_choice].chats.append(new_chat)
                                                              #your secret message is ready to send the spy
            print "***Your secret message image is ready!***"
            i=0
        else:
            print "You have done something Wrong Please Check again and retry"
            i=i-1

#-------------------------------------------Here you can read the messages---------------------------------------------------------------------

def read_message():
    sender = select_a_friend()                             #Here we select the friend(spy) to send the message

    output_path = raw_input("***What is the name of the file?***")

    secret_text = Steganography.decode(output_path)        #Steganography are used to encode message in a image

    new_chat = ChatMessage(secret_text, False)

    friends[sender].chats.append(new_chat)

    print "***Your secret message has been saved!***"      #our secret mesage are saved and ready to view by user

#------------------------------------Here we can read the older messages or communication of two friends-----------------------------------------
def read_chat_history():
    read_for = select_a_friend()
#------------------------------------------now we give color to particular date ,time ,username and message--------------------------------------
    #print '\n6'
    now=datetime.now()                 #Here we give datetime.now function
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
           a =now.strftime("%b %d %Y") #Here we using variable
           b=now.strftime("%H: %M :%S")
           text = colored(a,'yellow')
           text1 =colored(b,'blue')
           text2 =(text +"at"+text1)
           d=colored(chat.message,'cyan')
           c=colored(friends[read_for].name,"green")
           print ("\n\n\t\t\t"+text2+ "%s said:[%s]") %(c,d)
#--------------------------------------------------------Now be are able to do chat with spy------------------------------------------------------
def start_chat(spy):
    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:

        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True
#----------------------------------------------here we use menu list------------------------------------------------------------------------------
        while show_menu:
            menu_choices = "***What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Ask for default user or new user \n"
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

                else:
                    show_menu = False
    else:

        print 'Sorry you are not of the correct age to be a spy'    #if your choice are not correct


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
choice = raw_input("\t\t\t******If you are new user then enter Y   ***** \n\t\t\t\t\t\tor\n \t\t\t*****If you are default user then enter N.  ***** ")
if str.upper(choice) == "Y":
    new_user()


elif str.upper(choice) == "N":
    default_user()
#-----------------------------------------------------End of project----------------------------------------------------------------------------