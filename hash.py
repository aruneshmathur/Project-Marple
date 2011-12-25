#!/usr/bin/python

def generate_hashes(string = "", k = 1, B = 137, M = 5463458053):
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

if __name__ == "__main__":

    for r in generate_hashes("Hello there madam!", 5):
        print r
