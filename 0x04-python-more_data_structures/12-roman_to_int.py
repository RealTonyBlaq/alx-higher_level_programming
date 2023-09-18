#!/usr/bin/python3
def roman_to_int(roman_string):

    """
    Function:
    ---------
    roman_to_int - Converts roman numerals to integer

    Parameters:
    -----------
    roman_string - A string of roman numerals

    Return: The converted number
    """
    if roman_string is None:
        return 0
    if not str(roman_string):
        return 0
    intgr = 0
    lenn = len(roman_string)
    dic = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    for i in range(0, lenn):
        if i > 0:
            if (dic[roman_string[i - 1]] < dic[roman_string[i]]):
                k = dic[roman_string[i]] - dic[roman_string[i - 1]]
                intgr += k - dic[roman_string[i - 1]]
            else:
                intgr += dic[roman_string[i]]
        else:
            intgr += dic[roman_string[i]]

    return intgr
