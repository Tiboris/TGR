#!/usr/python3
import sys

import chemistry
import fusion
import information


if __name__ == "__main__":
    if str(sys.argv[1]) == "information":
        sys.exit(information.run(sys.stdin.read().splitlines()))
    elif str(sys.argv[1]) == "fusion":
        sys.exit(fusion.run(sys.stdin.read().splitlines()))
    elif str(sys.argv[1]) == "chemistry":
        sys.exit(chemistry.run(sys.stdin.read().splitlines()))
    else:
        sys.stderr.write("You choose poorly.")
        sys.exit(1)
