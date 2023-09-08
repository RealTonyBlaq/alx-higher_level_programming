#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import * as data
    lists = dir(data)
    for l in lists:
        if l[:2] != "__":
            print(l)
