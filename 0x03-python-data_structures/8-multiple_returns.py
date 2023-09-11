#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sen = None
    else:
        sen = sentence[0]
    return (len(sentence), sen)
