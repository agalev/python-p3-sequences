#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    result_list = list()
    counter = 0
    for n in range(length):
        result_list.append(counter)
        if counter == 0:
            counter = 1
        else:
            counter=result_list[n]+result_list[n-1]
        
    print(result_list)