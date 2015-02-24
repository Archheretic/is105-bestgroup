# -*- coding: latin-1 -*-
import sys
import re
#print sys.path
#
#   The function takes a decimal and turns it into a roman number.
#   First it checks if the parameter is a positive number (valid)
#   Then the function check if the parameter has a value of 1000 or more,
#   if it is then in subtracts 1000 from the parameter and adds the roman
#   numeral M to the roman string variable. This continues throught all the
#   roman numerals, until the parameter value is 0. The function then returns
#   the roman string variable.
#
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

    return _subtractive_form(roman)
#
#   This function is for converting a roman number to a decimal number.
#   The function uses checks that the roman number (string) is valid.
#   Then turns the roman number into its unsubtractive form XL -> XXXX.
#   The function then takes one roman number at time and turns them into
#   decimals. Then returns the full decimal number.
#
def roman_to_decimal(string):
    decimal = 0
    try:
        fixSubtractives = _unsubtractive_form(string)
        for c in fixSubtractives:
            decimal += _roman_numerals_value(c)
        return decimal
    except KeyError:
        print "Not a valid input, only roman numerals allowed"

#
#   This function is for adding together two roman numbers.
#   First it converts the string to its unsubtractive form i.e IX -> VIIII.
#   Then it concatenates the strings, sorts the string in the correct order,
#   subtract the string VIIII -> IX and returns the answer.
#
def roman_add(string1, string2):
    numerals1 = str(_unsubtractive_form(string1))
    numerals2 = str(_unsubtractive_form(string2))
    unsortedAnswer = numerals1 + numerals2
    finalAnswer = _subtractive_form(unsortedAnswer)
    return finalAnswer
#
#   This function subtracts the roman number "y" from the roman number "x".
#   First it converts the string to its unsubtractive form i.e IX -> VIIII.
#   Then it removes similar characters on both sides, until one of them doesn't
#   contain any of those characters, then it moves on to the next character.
#   When all similiar characters is removed, it downgrades the remains to the
#   lowest value (I) and those the samme all over again, until y is an empty
#   string. The remains of x is then turned into its subtractive form(IIII ->IV)
#   then returns this answer.
#
def roman_sub(x, y):
    if (roman_to_decimal(x)-roman_to_decimal(y)) < 0:
        print "Illegal values, roman numbers can only be positive!"
        return "Illegal values, roman numbers can only bCDDCe positive!"

    left1 = str(_unsubtractive_form(x))
    right1 = str(_unsubtractive_form(y))
    left2 = left1
    right2 = right1

    romanNumerals = ["I","V","X","L","C","D","M"]
    for e in romanNumerals:
        i = 0
        while i < left1.count(e) and i < right1.count(e):
            left2 = left2.replace(e,'',1)
            right2 = right2.replace(e,'',1)
            i = i + 1

    left1 = _downgrade_numerals(left2)
    right1 = _downgrade_numerals(right2)
    left2 = left1
    right2 = right1

    i = 0
    while i < left1.count("I") and i < right1.count("I"):
        left2 = left2.replace("I",'',1)
        right2 = right2.replace("I",'',1)
        i = i + 1

    answer = _subtractive_form(left2)

    if len(answer) == 0:
        answer = ("The romans don't have any numerals for zero, they have only "
                 + "words.")

    return answer

#
#   This function is for multiplying two roman numbers.
#   First it unsubtract both parameters (IX-> XVIIII), then downgrades them
#   all the way down to the numeral I. The way the function do the actual
#   math is described on this webpage:
#   http://rbutterworth.nfshost.com//tables/romanmult
#
def roman_mult(x, y):
    x2 = x
    y2 = y
    x = _unsubtractive_form(x)
    y = _unsubtractive_form(y)
    x = _downgrade_numerals(x)
    y = _downgrade_numerals(y)

    answer = ""
    while True:
        if len(x) == 0:
            break
        if len(x) % 2 != 0:
            answer = answer + y
        x = _split_string(x)
        y = _double_string(y)

    answer = _subtractive_form(answer)


    if decimal_to_roman((roman_to_decimal(x2)*roman_to_decimal(y2))) != answer:
        print ("Insert the numerals in correct order, don't make fantasy "
              + "numbers like IVI")
        return
    return answer
#
#   Help function with a dictionary that translates the value of roman
#   numeral into the decimal system.
#
def _roman_numerals_value(numeral):
    romanNumerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                     "M": 1000}
    return romanNumerals[numeral]
#
#   Help function that takes in two parameters, the first parameter is a
#   String, the other parameter is a dictionary. The function replaces the
#   characters in the string with the respective value in the dictionary
#
def _uni_sort(string, howToSort):
    for i, j in howToSort.iteritems():
        string = string.replace(i, j)
    return string
#
#   Help function that convers all roman numerals into their respective I value.
#   It uses a regular expression to confirm that the string only contains the
#   roman character I.
#
def _downgrade_numerals(numeral):
    table = {"M": "DD", "D": "CCCCC", "C": "LL", "L": "XXXXX", "X": "VV",
             "V": "IIIII"}
    while True:
        if re.match(r"^[I]*$", numeral):
            return numeral
        else:
            numeral = _uni_sort(numeral, table)
#
#   Help function that splits a string, and returns the first part of the string
#   If len(string) == odd number, it will count as an integer division and the
#   remains will be lost.
#
def _split_string(string):
    half = len(string)/2
    return string[:half]
#
#   Help function that adds a string to the same string.
#
def _double_string(string):
    string = string + string
    return string
#
#   Help function to sort a roman number after the numerals value.
#
def _sort_order(x):
    valueOrder = "MDCLXVI"
    sortingList = sorted(x, key=valueOrder.index)
    sort = ""
    for i in sortingList:
        sort += i
    return sort
#
#   Help function that turns a roman number into its unsubtractive
#   form (CL -> LXXXX).
#
def _unsubtractive_form(x):
    table = {"IV": "IIII", "IX": "VIIII", "XL": "XXXX", "XC": "LXXXX",
             "CD": "CCCC", "CM": "DCCCC"}
    sort = _uni_sort(x, table)
    test = ""
    while test != sort:
        test = sort
        sort = _uni_sort(sort, table)
    return sort
#
#   Help function that turns a roman number into its subtractive
#   form (XXXXX -> L ).
#
def _subtractive_form(x):
    table = {"IIIII": "V", "VV": "X", "XXXXX": "L", "LL": "C", "CCCCC": "D",
             "DD": "M"}
    table2 = {"IIII": "IV", "VIV": "IX", "VIIII": "IX", "XXXX": "XL",
              "LXXXX": "XC", "CCCC": "CD", "DCCCC": "CM"}

    sort = _sort_order(x)
    test = ""
    while test != sort:
        test = sort
        sort = _uni_sort(sort, table)

    test = ""
    while test !=sort:
        test = sort
        sort = _uni_sort(sort, table2)
    return sort
#
#   A function that asserts that all the main functions are working correctly.
#
def _test():
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
#
#   The if statement below will make the module only print out the tests as
#   Long as this module is the main module (not imported).
#
if __name__ == '__main__':
    print _test()
