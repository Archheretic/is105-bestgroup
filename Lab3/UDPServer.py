# -*- coding: latin-1 -*-

#
#   Imports the module socket and imports our custom made is105roman,
#   which handles roman numerals.
#
from socket import *
import is105roman
import LowerToUpper
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
            modifiedMessage = LowerToUpper.bit_flip(message)
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

server()
