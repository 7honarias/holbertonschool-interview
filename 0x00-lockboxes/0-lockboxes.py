#!/usr/bin/python3

def canUnlockAll(boxes):
    keys = set([0])
    for i in range(len(boxes)):
        print(i)
        print(keys)
        if i in keys:
            for key in boxes[i]:
                keys.add(key)
        else:
            return False
    return True

