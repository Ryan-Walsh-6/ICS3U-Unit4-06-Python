#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: December 2020
# this program prints out all the valid RGB values


def main():
    # this program prints out all the valid RGB values
    counter1 = 0
    counter2 = 0
    counter3 = 0

    # process & output
    for counter1 in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print("RGB({0},{1},{2}".format(counter1, counter2,
                                               counter3))


if __name__ == "__main__":
    main()
