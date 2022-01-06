"""
Task
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird

Input Format:

A single line containing a positive integer, n .

Constraints:

1<= n <= 100

"""

# Solution -> 06/01/2022 Thiago Sampaio.
n = 4
if n % 2 != 0:
    print('Weird')
else:
    if n < 5:
        print('Not Weird')
        quit()
    if n <= 20:
        print('Weird')
    else:
        print('Not Weird')
