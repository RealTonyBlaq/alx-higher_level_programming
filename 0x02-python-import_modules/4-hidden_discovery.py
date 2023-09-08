#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lists = dir(hidden_4)
    for l in lists:
        if l[:2] != "__":
            print(l)
