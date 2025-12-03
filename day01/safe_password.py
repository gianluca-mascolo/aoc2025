#!/usr/bin/env python3
def main():
    dial = 50
    part1 = 0
    with open("input", "r") as reader:
        line = reader.readline()
        while line != "":  # The EOF char is an empty string
            line = line.rstrip()
            direction = line[0]
            steps = int(line[1:])
            if direction == "R":
                dial = (dial + steps) % 100
            elif direction == "L":
                dial = (dial - steps) % 100
            print(dial)
            if dial == 0:
                part1 = part1 + 1
            line = reader.readline()
    print(f"part1 = {part1}")


if __name__ == "__main__":
    main()
