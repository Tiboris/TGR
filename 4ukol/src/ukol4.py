#!/usr/bin/env python3
import sys

import evacuation
import groups
import parking

if __name__ == "__main__":
    if str(sys.argv[1]) == "evacuation":
        sys.exit(evacuation.run(sys.stdin.read().splitlines()))
    elif str(sys.argv[1]) == "groups":
        sys.exit(groups.run(sys.stdin.read().splitlines()))
    elif str(sys.argv[1]) == "parking":
        sys.exit(parking.run(sys.stdin.read().splitlines()))
    else:
        sys.stderr.write("You choose poorly.")
        sys.exit(1)
