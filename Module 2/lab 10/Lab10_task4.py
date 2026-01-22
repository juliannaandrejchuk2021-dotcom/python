import random

def Even_num_count_list(num_list):
    count = 0
    for num in num_list:
        if num % 2 == 0:
            count += 1
    return count



def vowels_count_list(string_list):
    vowels = 'aeiouAEIOU'
    count = 0
    for string in string_list:
        for char in string:
            if char in vowels:
                count += 1
    return count


