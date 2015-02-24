# -*- coding: latin-1 -*-

#
#   Imports the module socket and imports our custom made is105roman,
#   which handles roman numerals.
#
from socket import *
import is105roman
#
#   This is the server module
#   serverSocket : AF_INET tells that the adressfamily is IPv4
#   serverSocket : SOCK_DGRAM tells that we are using the UDP socket.
#   serverSocket.bind("This first parameter is the IP of the server so it can
#   either listen to the localhost or the ip on the network. The second
#   parameter is the port which is declared in serverPort variable.
#   While 1 : 1 is true, 0 is false. So this is always true.
#   modifiedMessage = message.upper() : takes the message string and makes it in
#   uppercase letters.
#   serverSocket.sendto(the modified uppercase string, clientAddress is the
#   ip and port it gets from the client that sends the message to the server)
#
def server():

    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(("", serverPort))
    print "The server is ready to receive"
    while 1:
        message, clientAddress = serverSocket.recvfrom(2048)

        string = message.split("#")

        answer = string[0]
        message = string[1]

        if answer == "1":
            modifiedMessage = _ans_1(message)
            print clientAddress
            serverSocket.sendto(modifiedMessage.encode("utf-8"), clientAddress)

        if answer == "2":
            message = int(message)
            modifiedMessage = is105roman.decimal_to_roman(message)
            serverSocket.sendto(modifiedMessage, clientAddress)

        if answer == "3":
            modifiedMessage = str(is105roman.roman_to_decimal(message))
            serverSocket.sendto(modifiedMessage, clientAddress)

        if answer == "4":
            string = message.split("@")

            y = string[0]
            x = string[1]
            modifiedMessage = str(is105roman.roman_add(y, x))
            serverSocket.sendto(modifiedMessage, clientAddress)

        if answer == "5":
            string = message.split("@")

            y = string[0]
            x = string[1]
            modifiedMessage = str(is105roman.roman_sub(y, x))
            serverSocket.sendto(modifiedMessage, clientAddress)

        if answer == "6":
            string = message.split("@")

            y = string[0]
            x = string[1]
            modifiedMessage = str(is105roman.roman_mult(y, x))
            serverSocket.sendto(modifiedMessage, clientAddress)
#
#   The main function for handling conversion from lower to upper case.
#
def _ans_1(message):
    message = message.decode("utf-8")

    modifiedMessage = ""
    for i in message:
        modifiedMessage = modifiedMessage + _lower_to_upper_case(i)

    encodedMessage = modifiedMessage.encode("utf-8")

    print ("Transforms: " + message + " to uppercase: "
           + modifiedMessage + " from client: ")

    return modifiedMessage
#
#   Help function for the __ans_1__ function, this function does the
#   actuall convertion from lower to upper case.
#
def _lower_to_upper_case(char):
    lower = bin(ord(char))
    mask = bin(32)
    upper = int(lower,2) ^ int(mask,2)
    upper = '{0:b}'.format(upper)
    upper = unichr(int(upper,2))

    return upper

server()
