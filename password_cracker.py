#!/usr/bin/env python

import hashlib

def crack_sha1_hash(hash, use_salts=False):
    passwords = 'top-10000-passwords.txt'
    salts = 'known-salts.txt'

    with open(passwords, 'r') as pf:
        for pwd in (pwd.strip() for pwd in pf):
            if use_salts:
                with open(salts, 'r') as sf:
                    for salt in (salt.strip() for salt in sf):
                        salted = salt + pwd
                        if  (hash == hashlib.sha1(salted.encode()).hexdigest()):
                            return pwd
                        salted = pwd + salt
                        if  (hash == hashlib.sha1(salted.encode()).hexdigest()):
                            return pwd
            else:
                if (hash == hashlib.sha1(pwd.encode()).hexdigest()):
                    return pwd

    return 'PASSWORD NOT IN DATABASE'
