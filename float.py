#!/usr/bin/env python
from fractions import Fraction

class fpo():
    def __init__(self, rawData):
        self.data = {}
        if len(rawData.split(" ")) == 3:
            binary = rawData.split(" ")
            self.data['sign'] = binary[0]
            self.data['exp'] = binary[1]
            self.data['frac'] = binary[2]

    def __binary_to_decimal(self, binaryString):
        number = 0
        counter = 0
        for item in binaryString[::-1]:
            if int(item) == 1:
                number += 2**counter
            counter += 1
        return number

    def __binaryfrac_to_decimal(self, binaryString):
        number = 0.0
        counter = 1
        for item in binaryString:
            if int(item) == 1:
                number += 1.0/(2**counter)
            counter += 1
        return number

    def print_decimal(self):
        """
        Converts a IEEE 754 representation of a floating point number to a human readable decimal number
        """
        normalized = 0
        frac = self.__binaryfrac_to_decimal(self.data['frac'])
        E = self.__binary_to_decimal(self.data['exp'])
        bias = 2**(len(self.data['exp'])-1)-1
        e = E - bias
        if e >= 0:
            normalized = 1
        mantissa = frac+normalized

        decimal_number = 2**e * mantissa
        if self.data['sign'] == '1':
            decimal_number *= -1
        if not '0' in self.data['exp'] and not '1' in self.data['frac']:
            print("inf")
        elif not '0' in self.data['exp'] and '1' in self.data['frac']:
            print("NaN")

        else:
            print("Decimal:    %s\nFraction:    %s" % (decimal_number, Fraction(decimal_number)))



if __name__ == "__main__":
    myInput = raw_input()
    myObj = fpo(myInput)
    myObj.print_decimal()
