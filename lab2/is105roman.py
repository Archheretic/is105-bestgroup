# -*- coding: latin-1 -*-
import sys
import re
#print sys.path
def roman_numerals_value(numeral):
    romanNumerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                     "M": 1000}
    return romanNumerals[numeral]

def uni_sort(string, howToSort):
    for i, j in howToSort.iteritems():
        string = string.replace(i, j)
    return string

def downgrade_numerals(numeral):
    table = {"M": "DD", "D": "CCCCC", "C": "LL", "L": "XXXXX", "X": "VV",
             "V": "IIIII"}
    while True:
        if re.match(r"^[I]*$", numeral):
            return numeral
        else:
            numeral = uni_sort(numeral, table)


def split_string(string):
    half = len(string)/2
    return string[:half]


def double_string(string):
    string = string + string
    return string



def sort_order(x):
    valueOrder = "MDCLXVI"
    sortingList = sorted(x, key=valueOrder.index)
    sort = ""
    for i in sortingList:
        sort += i
    return sort

def unsubtractive_form(x):
    table = {"IV": "IIII", "IX": "VIIII", "XL": "XXXX", "XC": "LXXXX",
             "CD": "CCCC", "CM": "DCCCC"}
    sort = uni_sort(x, table)
    test = ""
    while test != sort:
        test = sort
        sort = uni_sort(sort, table)

    return sort

def subtractive_form(x):
    table = {"IIIII": "V", "VV": "X", "XXXXX": "L", "LL": "C", "CCCCC": "D",
             "DD": "M"}
    table2 = {"IIII": "IV", "VIIII": "IX", "XXXX": "XL", "LXXXX": "XC",
              "CCCC": "CD", "DCCCC": "CM"}


    sort = sort_order(x)
    test = ""
    while test != sort:
        test = sort
        sort = uni_sort(sort, table)

    test = ""
    while test !=sort:
        test = sort
        sort = uni_sort(sort, table2)
    return sort

def decimal_to_roman(int1):
    if int1 <=0:
        print "Insert a valid integer."
        return

    roman = ""
    if int1 >= 1000:
        while int1 >= 1000:
            roman += "M"
            int1 -= 1000

    if int1 >= 500:
        while int1 >= 1000:
            roman += "D"
            int1 -= 500

    if int1 >= 100:
        while int1 >= 100:
            roman += "C"
            int1 -= 100

    if int1 >= 50:
        while int1 >= 50:
            roman += "L"
            int1 -= 50

    if int1 >= 10:
        while int1 >= 10:
            roman += "X"
            int1 -= 10

    if int1 >= 5:
        while int1 >= 5:
            roman += "V"
            int1 -= 5

    if int1 > 0:
        while int1 <= 5 and int1 > 0:
            roman += "I"
            int1 -= 1

    return subtractive_form(roman)

def roman_to_decimal(string):
    decimal = 0
    try:
        fixSubtractives = unsubtractive_form(string)
        for c in fixSubtractives:
            decimal += roman_numerals_value(c)
        return decimal
    except KeyError:
        print "Not a valid input, only roman numerals allowed"

#
#   This function is for adding together two strings.
#   first it converts the string to its unsubtractive form i.e IX -> VIIII.
#   Then it concatenates the strings, sorts the string in the correct order,
#   subtract the string VIIII -> IX and returns the answer.
#
def roman_add(string1, string2):
    numerals1 = str(unsubtractive_form(string1))
    numerals2 = str(unsubtractive_form(string2))
    unsortedAnswer = numerals1 + numerals2
    finalAnswer = subtractive_form(unsortedAnswer)
    return finalAnswer

def roman_sub(x, y):
    left1 = str(unsubtractive_form(x))
    right1 = str(unsubtractive_form(y))
    left2 = left1
    right2 = right1

    romanNumerals = ["I","V","X","L","C","D","M"]
    for e in romanNumerals:
        i = 0
        while i < left1.count(e) and i < right1.count(e):
            left2 = left2.replace(e,'',1)
            right2 = right2.replace(e,'',1)
            i = i + 1

    left1 = downgrade_numerals(left2)
    right1 = downgrade_numerals(right2)
    left2 = left1
    right2 = right1

    i = 0
    while i < left1.count("I") and i < right1.count("I"):
        left2 = left2.replace("I",'',1)
        right2 = right2.replace("I",'',1)
        i = i + 1

    answer = subtractive_form(left2)
    return answer

def roman_mult(x, y):
    x = unsubtractive_form(x)
    y = unsubtractive_form(y)
    x = downgrade_numerals(x)
    y = downgrade_numerals(y)

    answer = ""
    while True:
        if len(x) == 0:
            break
        if len(x) % 2 != 0:
            answer = answer + y
        x = split_string(x)
        y = double_string(y)

    answer = subtractive_form(answer)
    return answer

def test():
    assert decimal_to_roman(2444) == "MMCDXLIV"
    assert decimal_to_roman(1337) == "MCCCXXXVII"
    assert roman_to_decimal("MMCDXLIV") == 2444
    assert roman_to_decimal("MCCCXXXVII") == 1337
    assert roman_add("MCCCXXXVII", "MMCDXLIV") == "MMMDCCLXXXI"
    assert roman_sub("MMMDCCLXXXI", "MCCCXXXVII") == "MMCDXLIV"
    assert roman_sub("MMMDCCLXXXI", "MMCDXLIV") == "MCCCXXXVII"
    assert roman_mult("DCIV", "XLIV") == "MMMMMMMMMMMMMMMMMMMMMMMMMMDLXXVI"
    assert roman_mult("CIV", "CD") == "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMDC"

    return "Testene er fullført uten feil."

print test()
