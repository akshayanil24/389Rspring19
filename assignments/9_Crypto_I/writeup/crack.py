#!/usr/bin/env python3

import hashlib
import string

def crack():
    hashes = open("hashes.txt").read().splitlines()
    passwords = open("passwords.txt").read().splitlines()
    characters = string.ascii_lowercase

    for c in characters:
        for p in passwords:
            hash = hashlib.sha256(c+p).hexdigest()

            if hash in hashes:
                print(p + ":" + hash)
            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()
