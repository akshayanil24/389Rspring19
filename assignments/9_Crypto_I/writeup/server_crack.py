#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    hashes = open("hashes.txt").read().splitlines()
    passwords = open("passwords.txt").read().splitlines()
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    for i in range(3):
        data = s.recv(1024)
        prompt = data.splitlines()[2]
        for c in characters:
            for p in passwords:
                #time.sleep(1)
                hash = hashlib.sha256(c+p).hexdigest()
                if hash == prompt:
                    #print(p + ":" + hash)
                    s.send(c+p+'\n')
    # parse data
    # crack 3 times
    print(s.recv(1024))
if __name__ == "__main__":
    server_crack()
