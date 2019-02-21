#!/usr/python3
import sys

import information
import fusion
import chemistry


if __name__ == '__main__':
    if (str(sys.argv[1]) == "information"):
        sys.exit(information.run(str(sys.stdin.readlines())))
    elif (str(sys.argv[1]) == "fusion"):
        sys.exit(fusion.run(str(sys.stdin.readlines())))
    elif (str(sys.argv[1]) == "chemistry"):
        sys.exit(chemistry.run(str(sys.stdin.readlines())))
    else:
        sys.stderr.write("You choose poorly.")
        sys.exit(1)
