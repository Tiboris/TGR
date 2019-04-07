#!/usr/bin/env python3
import sys

import car
import race
import server

if __name__ == "__main__":
    if str(sys.argv[1]) == "car":
        sys.exit(car.run(sys.stdin.read().splitlines()))
    elif str(sys.argv[1]) == "race":
        sys.exit(race.run(sys.stdin.read().splitlines()))
    elif str(sys.argv[1]) == "server":
        sys.exit(server.run(sys.stdin.read().splitlines()))
    else:
        sys.stderr.write("You choose poorly.")
        sys.exit(1)
