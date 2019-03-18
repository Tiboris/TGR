#!/usr/python3
import sys

import power
import reset
import weakness
import avltree

if __name__ == '__main__':
    if (str(sys.argv[1]) == "power"):
        sys.exit(power.run(sys.stdin.read().splitlines()))
    elif (str(sys.argv[1]) == "reset"):
        sys.exit(reset.run(sys.stdin.read().splitlines()))
    elif (str(sys.argv[1]) == "weakness"):
        sys.exit(weakness.run(sys.stdin.read().splitlines()))
    elif (str(sys.argv[1]) == "avltree"):
        sys.exit(avltree.run(sys.stdin.read().splitlines()))
    else:
        sys.stderr.write("You choose poorly.")
        sys.exit(1)
