""" A Python program that uses recursion to count all possible ways to climb a staircase 
using 1-step or 2-step moves, combining both recursive branches until the base cases are reached."""

numberOfSteps = int(input("Enter number of steps: "))


def waysToClimb(stairs):
    if stairs == 1:
        return 1

    if stairs == 2:
        return 2

    return waysToClimb(stairs - 1) + waysToClimb(stairs - 2)


print(waysToClimb(numberOfSteps))
