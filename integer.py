#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program determines positive/negative/zero numbers


def main():
    # this function runs the integer identity

    # input
    print("Positive, negative or zero?")
    integer = int(input("Enter an integer: "))

    # process and output
    if integer >= 0:
        print("{} is a positive number!".format(integer))
    elif integer <= 0:
        print("{} is a negative number!".format(integer))
    elif integer == 0:
        print("{} is nothing but a zero!".format(integer))


if __name__ == "__main__":
    main()
