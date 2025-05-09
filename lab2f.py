#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Error: Please provide a starting number for the countdown.")
    sys.exit(1)

try:
    count = int(sys.argv[1])
    if count <= 0:
        raise ValueError
except ValueError:
    print("Error: Please provide a positive integer.")
    sys.exit(1)

while count > 0:
    print(count)
    count -= 1
print("blast off!")
