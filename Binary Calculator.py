##
##=======================================================
## Jaskirat Pabla
## Binary Calculator
##=======================================================
##


import check


## Global Constant:
invalid_text = "Invalid Number"


def binary_to_decimal(bits):
    '''
    Returns decimal value of bits and mutates bits to replace each 1
    with it's corresponding decimal value. Returns "Invalid Number"
    if there are more than 8 digits in bits, or bits contains something
    other than ones and zeros.

    Effects: Mutates bits.
    
    binary_to_decimal: (listof Any) -> (anyof Nat invalid_text)
    
    Examples:
        B = []
        binary_to_decimal(B) => invalid_text
        and B is not mutated. It should remain [].
        
        B = [1, 0, 1, 0, 1, 0, 1, 0, 1]
        binary_to_decimal(B) => invalid_text
        and B is not mutated. It should remain [1, 0, 1, 0, 1, 0, 1, 0, 1].
        
        B = [0, 1, 0, 1]
        binary_to_decimal(B) => 5
        and B is mutated to [0, 4, 0, 1].
    '''
    length = len(bits)
    if (length < 1):
        return invalid_text
    elif (length > 8):
        return invalid_text
    
    for val in bits:
        if (val != 0):
            if (val != 1):
                return invalid_text
        elif (val != 1):
            if (val != 0):
                return invalid_text
    
    for pos in (range(length)):
        if (bits[pos] == 1):
            exponent = length - pos - 1
            bits[pos] = 2 ** exponent
    
    decimal_sum = 0
    index = 0
    while (index < length):
        decimal_sum += bits[index]
        index += 1
    return decimal_sum


## Examples:
B = []
check.expect("Ex 1 - empty list", binary_to_decimal(B), invalid_text)
check.expect("Ex 1 Mutation", B, B)

B = [1, 0, 1, 0, 1, 0, 1, 0, 1]
check.expect("Ex 2 - list of length greater than 9", binary_to_decimal(B),
             invalid_text)
check.expect("Ex 2 Mutation", B, B)

B = [0, 1, 0, 1]
check.expect("Ex 3 - Typical", binary_to_decimal(B), 5)
check.expect("Ex 3 Mutation", B, [0, 4, 0, 1])


## Tests:
B = [0]
check.expect("T1 - list of just 0", binary_to_decimal(B), 0)
check.expect("T1 Mutation", B, B)

B = [1]
check.expect("T2 - list of just 1", binary_to_decimal(B), 1)
check.expect("T2 Mutation", B, B)

B = [0, 0, 0, 0, 0, 0, 0, 0]
check.expect("T3 - list of 8 zeros", binary_to_decimal(B), 0)
check.expect("T3 Mutation", B, B)

B = [1, 1, 1, 1, 1, 1, 1, 1]
check.expect("T4 - list of 8 ones", binary_to_decimal(B), 255)
check.expect("T4 Mutation", B, [128, 64, 32, 16, 8, 4, 2, 1])

B = [1, 0, "one", "loper"]
check.expect("T5 - list including something other than 1 or 0",
             binary_to_decimal(B), invalid_text)
check.expect("T5 Mutation", B, B)

B = [7]
check.expect("T6 - Another list including something other than 1 or 0",
             binary_to_decimal(B), invalid_text)
check.expect("T6 Mutation", B, B)

B = [0, 1, 0, True, False, "yellow", [1, 0, 1], 1]
check.expect("T7 - Another list including something other than 1 or 0",
             binary_to_decimal(B), invalid_text)
check.expect("T7 Mutation", B, B)

B = [0, 1, 0, [1, 0, 1], 1, 0]
check.expect("T8 - Another list including something other than 1 or 0",
             binary_to_decimal(B), invalid_text)
check.expect("T8 Mutation", B, B)

B = [1, 0, 1, 0, 1, 0, 1, 0]
check.expect("T9 - Typical", binary_to_decimal(B), 170)
check.expect("T9 Mutation", B, [128, 0, 32, 0, 8, 0, 2, 0])

B = [0, 1, 0, 1, 0, 1, 0, 1]
check.expect("T10 - Another typical", binary_to_decimal(B), 85)
check.expect("T10 Mutation", B, [0, 64, 0, 16, 0, 4, 0, 1])

B = [0, 1]
check.expect("T11 - Another typical", binary_to_decimal(B), 1)
check.expect("T11 Mutation", B, B)

B = [1, 0]
check.expect("T12 - Another typical", binary_to_decimal(B), 2)
check.expect("T12 Mutation", B, [2, 0])
