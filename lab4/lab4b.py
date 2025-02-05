#!/usr/bin/env python3

def join_lists(l1, l2):
    return list(set(l1) | set(l2))

def match_lists(l1, l2):
    return list(set(l1) & set(l2))

def diff_lists(l1, l2):
    return list(set(l1) ^ set(l2))

if __name__ == '__main__':
    list1 = list(range(1, 10))
    list2 = list(range(5, 15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))