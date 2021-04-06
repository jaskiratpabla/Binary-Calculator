# Binary-Calculator
Binary Calculator in Python, full documentation and testing is included.
In the early days of computing, computers were comprised of a bank of electronic switches that were either on or off. Toggling these switches would change which calculations could be performed. Thus, computers today still use a base-2 system of binary numbers with only two symbols: 0 (off) and 1 (on).

While Python programs are expressed in words that are human-readable, the Python interpreter breaks our code down to a set of machine-readable binary digits or "bits" so that the computer can understand the instructions.

A group of eight (8) bits is equal to a byte, which is considered to be a unit of memory. Each bit in a byte, starting from the right side, adds an additional exponent to a base of 2 if that bit is 1 (on).

Since the below image has all bits set to 1 (on), you would calculate the decimal value as follows:

![image](https://user-images.githubusercontent.com/67871488/113641091-e6459c00-964a-11eb-8b45-a47f24c9c126.png)

In the below image some of the bits are off (0). While the computer tends to not assign a value at all to these bits, we will be including them as 0 in our binary calculator.

For the below image, you would calculate the decimal value as follows:

![image](https://user-images.githubusercontent.com/67871488/113641116-f3628b00-964a-11eb-89dc-fc7662f34ad0.png)

In this repository, we will write a binary calculator that will convert a binary number to a decimal number.

The function binary_to_decimal(bits) consumes a list of up to eight 1s and 0s, returns the decimal value, and mutates the list to replace each 1 with the corresponding integer decimal value. If there are more than 8 digits or the list contains something other than a 1 or a 0, the function returns "Invalid Number" and does not mutate the list. In addition, we may not use the built-in sum function.
