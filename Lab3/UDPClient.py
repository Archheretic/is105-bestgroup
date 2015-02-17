# -*- coding: latin-1 -*-

from socket import *
import re
import time
#
#   serverName is set as localhost which is a reference to the ip 127.0.0.1
#   serverPort is set to the same port as the server the client tries to send
#   information to. AF_INET, SOCK_DGRAM is parameters to the function socket
#   which refers to IPv4 and UDP.
#   "re.match(r"^[a-zæ-å]*$", message" is a regular expression that checks that
#   the string only contains the chars inside the [].
#
#   clientSocket.sendto(message,(serverName, serverPort))
#   Sends the string message to @serverName, @serverPort
#
def client(answer, message):

    message = answer + "#" + message
    serverName = "localhost"
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    clientSocket.sendto(message,(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print modifiedMessage
    clientSocket.close()
    quit()
#
#   This is the first function that the user is presented with.
#   This function is for presenting the user his options, and its also were
#   he makes his choices.
#
def choices():

    print "\nWelcome to our program!\nWe got numerous options for you, so ",
    print "listen carefully.\nThe options are marked with a number, write the ",
    print "number to choose option:"
    time.sleep(5)
    print "1. Convert lowercase words to uppercase."
    time.sleep(1)
    print "2. Convert numbers from the decimal system to roman numerals."
    time.sleep(1)
    print "3. Convert from roman numerals to the decimal system."
    time.sleep(1)
    print "4. Add two roman numbers."
    time.sleep(1)
    print "5. Subtract two roman numbers."
    time.sleep(1)
    print "6. Multiply two roman numbers."
    time.sleep(2)

    valid_answer = False
    while valid_answer == False:
        answer = raw_input("I choose option: ")
        if (re.match(r"^[1-6]*$", answer)):
            valid_answer = True
        elif (re.match(r"^[qQ]*$", answer)):
            print "Goodbye!"
            quit()
        else:
            print "pick an option 1-6, type q to quit the program"

    __chosen_procedure__(answer)
#
#   This function checks the answer the user gave and sends him to the function
#   of choice.
#
def __chosen_procedure__(answer):

    if answer == "1":
        __lowercase_to_uppercase__(answer)

    if answer == "2":
        __decimal_to_roman__(answer)

    if answer == "3":
        __roman_to_decimal__(answer)

    if answer == "4" or "5" or "6":
        __roman_math__(answer)
#
#   The function that handles the request to turn lowercase words to uppercase
#   words.
#
def __lowercase_to_uppercase__(answer):

    lowercase = False
    while lowercase == False:
        message = raw_input("Input lowercase sentence: ")
        if (re.match(r"^[a-zæ-å]*$", message)):
            lowercase = True
        else:
            print "Only the lowercase letters a-å are allowed"

    client(answer, message)
#
#   The function that handles the request to turn decimal numbers to roman
#   numerals.
#
def __decimal_to_roman__(answer):

    valid_answer = False
    while valid_answer == False:
        message = raw_input("Input decimal number to convert: ")
        if (re.match(r"^[0-9]*$", message)):
            valid_answer = True
        else:
            print "Only numbers 0-9 are allowed"

    client(answer, message)
#
#   The function that handles the request to turn roman numerals into decimal
#   numbers.
#
def __roman_to_decimal__(answer):

    valid_answer = False
    while valid_answer == False:
        message = raw_input("Input roman numerals to convert: ")
        if (re.match(r"^[IVXLCDM]*$", message)):
            valid_answer = True
        else:
            print "Only the roman numerals I V X L C D M are allowed!"

    client(answer, message)
#
#   The function that handles requests to either add, subtract or multiply
#   with roman numerals.
#
def __roman_math__(answer):

    if answer == "4":
        math = "add"

    elif answer == "5":
        math = "subtract"

    else:
        math = "multiply"

    valid_answer = False
    while valid_answer == False:

        print "Input the roman numberals you want to %s." % math

        message = raw_input('Use this form "XL@IV":  ')
        if (re.match(r"^[IVXLCDM@]*$", message)):
            tmpmessage = __test_if_two__(message)
            if (re.match(r"^[IVXLCDM]*$", tmpmessage)):
                valid_answer = True
        else:
            print "Only the roman numerals I V X L C D M and @ are allowed!"

    client(answer, message)
#
#   Help function that splits a string at the @, it then tests if the
#   String is split in two. If its split in two it will concenate strings
#   and send them back to the function for a last validity test.
#
def __test_if_two__(string):
    string = string.split("@")

    if len(string) != 2:
        return "A"

    string1 = string[0]
    string2 = string[1]

    if ((len(string1) == 0) | (len(string2) == 0)):
        return "A"
    return string1 + string2

choices()
