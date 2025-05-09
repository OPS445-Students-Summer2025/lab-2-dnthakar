#!/usr/bin/env python3

import sys

# Default timer value is 3
if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Use the argument passed in
else:
    timer = 3  # Default to 3 if no argument is provided

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
