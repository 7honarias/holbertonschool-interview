#!/usr/bin/python3
"""boxes module"""


def canUnlockAll(boxes):
    """boxes key"""
    keys = {0: True}
    n_boxes = len(boxes)
    while(True):
        count = len(keys)

        for i in range(len(boxes)):
            if boxes[i] and keys.get(i, False):
                for j in boxes[i]:
                    if j < n_boxes:
                        keys[j] = True
                    boxes[i] = None

        if not(len(keys) > count):
            break

    if count == len(boxes):
        return True

    return False
