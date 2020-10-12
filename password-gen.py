#!/usr/bin/env python3
import random
import string

while True:
    try:
        length = int(input("How long do you want your password to be?: "))
        secure = random.SystemRandom()
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''
        for i in range(length):
            password += str(secure.choice(alphabet))
        print(password)
    except ValueError:
        print('Please enter a number.')
    except KeyboardInterrupt:
        print("\nQuiting..")
        exit()
