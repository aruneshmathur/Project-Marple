#!/usr/bin/python
M = 5463458053

def stripchars(s, chars):
    return s.translate(None, chars)


def generate_hashes(string, k = 10, B = 137):
    hash_list = []

    length = len(string)
    count = length - k + 1

    if count <= 0:
        return None 

    t = 0
    j = 1

    # Calculate ((B ^ k) - 1) once
    for i in range(0, k - 1):
        j = (j * B) % M
    
    for i in range(0, k):
        t = ((t * B) + ord(string[i])) % M

    hash_list.append(t)

    for i in range(1, count):
        t = (hash_list[i-1] - (ord(string[i-1]) * j)) % M
        t = (t * B) % M
        t = (t + ord(string[i+k-1])) % M
        hash_list.append(t)

    return hash_list


def winnow(hash_list=[], w = 15):

    winnow_list = []
    hash_list_length = len(hash_list)

    param = hash_list_length

    if not param < w:
        param = w

    global_min = M + 1  
        
    for i in range(param - 1, -1, -1):
        if hash_list[i] < global_min:
            global_min = hash_list[i]
            index = i

    winnow_list.append(global_min)

    if hash_list_length < w:
        return winnow_list

    for i in range(1, hash_list_length - w + 1):
        if i - index > 0:
            global_min = M + 1

            for j in range(w + i - 1, i - 1, -1):

    
if __name__ == "__main__":

    winnow(generate_hashes("Hello there madam!"), 4), 
