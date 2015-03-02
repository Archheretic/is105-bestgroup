# -*- coding: latin-1 -*-
#
#   The main function for handling conversion from lower to upper case.
#
def bit_flip(message):
    message = message.decode("utf-8")

    modifiedMessage = ""
    for i in message:
        modifiedMessage = modifiedMessage + _lower_to_upper_case(i)

    encodedMessage = modifiedMessage.encode("utf-8")

    print ("Transforms: " + message + " to uppercase: "
           + modifiedMessage + " from client: ")

    return modifiedMessage
#
#   Help function for the _ans_1 function, this function does the
#   actuall convertion from lower to upper case.
#
def _lower_to_upper_case(char):
    lower = bin(ord(char))
    mask = bin(32)
    upper = int(lower,2) ^ int(mask,2)
    upper = '{0:b}'.format(upper)
    upper = unichr(int(upper,2))

    return upper

def _test():
    pass

if __name__ == '__main__':
    print _test()
