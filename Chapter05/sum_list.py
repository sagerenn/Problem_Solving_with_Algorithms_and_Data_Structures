#!/usr/bin/env python3
# coding=utf-8

import sys
import os
sys.path.append(os.path.abspath('./Chapter04'))
# # add the work path to sys path, this will cause the other module import from the work path instead of the same folder
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from stack import Stack

def iter_sum(num_list):
    num_sum = 0
    # for i in num_list:
    #     num_list += i

    count = 0
    while count != len(num_list):
        num_sum += num_list[count]
        count += 1
    return num_sum


def recur_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + recur_sum(num_list[1:])

# maybe O(n) and use more space
def factorial_num(num):
    if num <= 1:
        return 1
    else:
        return num * factorial_num(num-1)

# 769 = 7 * 10^2 + 6 * 10^1 + 9 * 10^0
# to string, is retrieve the every postion number which is less than the base 10 and change to string by using comparable table
# we don't know the length, but we can start from divide by 10 until the last or most significant part to be less than base 10
def base_string(num, base):
    convert_string = '0123456789ABCDEF'
    if num < base:
        return convert_string[num]
    else:
        return base_string(num // base, base) + convert_string[num % base]

def revers_string(test_string):
    if not test_string:
        return test_string
    else:
        return revers_string(test_string[1:]) + test_string[0]

def check_palindrome(test_string):
    ch_string = 'abcdefghijklmnopqrstuvwxyz'
    # remove the chars on the both sides to shorter the process
    # when zero or one letter remain, it's palindrome. That is the base condition.
    if len(test_string) <= 1:
        return True
    else:
        # the topmost step to solve the problem, remove the first pair of chars and compare them
        head = 0
        end = len(test_string) - 1
        while head != len(test_string) and test_string[head].lower() not in ch_string:
            head += 1
        while end != -1 and test_string[end].lower() not in ch_string:
            end -= 1
        if end - head <= 1:
            return True
        # check the remain string
        if test_string[head].lower() == test_string[end].lower():
            return check_palindrome(test_string[head+1:end])
        else:
            # The recursive steps will be stop when some conditions meet
            return False


def stack_base_string(num, base):
    s = Stack()
    convert_string = '01234567890ABCDEF'
    while num > 0:
        s.push( convert_string[num % base] )
        num = num // base
    result = ''
    while not s.is_empty():
        result += s.pop()
    return result

print(iter_sum([1,3,5,7,9]))
print(recur_sum([1,3,5,7,9]))
print(factorial_num(5))
print(repr(base_string(34564,16)))
print(repr(stack_base_string(34564,10)))
print(repr(revers_string('eegeh')))
print(check_palindrome('Go hang a salami; I’m a lasagna hog.'))
print(check_palindrome('Go han a salami; I’m a lasagna hog.'))
print(check_palindrome('Reviled did I live, said I, as evil I did deliver'))
print(check_palindrome('Reviled did I live, sad I, as evil I did deliver'))

