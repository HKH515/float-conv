#!/usr/bin/env python
import sys
from fractions import Fraction

class fpo():
    def __init__(self, rawData):
        self.data = {}
        if len(rawData.split(" ")) == 3:
            binary = rawData.split(" ")
            self.data['sign'] = binary[0]
            self.data['exp'] = binary[1]
            self.data['frac'] = binary[2]
        elif len(rawData.split("/")) == 2:
            fractional = rawData.split("/")
            self.data['upper'] = fractional[0]
            self.data['lower'] = fractional[1]
        elif len(rawData.split(" ")) == 0 & len(rawData.split("/")) == 0:
            self.data['decimal'] = rawData

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

    def __decimal_to_binaryfrac(self, decimal):
        binary = 0
        counter = 1

    def __decimal_to_binary(self, decimal):
        pass
        leftSide = decimal.round()
        rightSide = decimal - leftSide;

    def print_binary(self):
        """
        Converts a human readable decimal number or fraction to an IEEE 754 representation of a floating point number
        """
        pass

    def print_decimal(self):
        """
        Converts an IEEE 754 representation of a floating point number to a human readable decimal number or fraction
        """
        normalized = None
        frac = self.__binaryfrac_to_decimal(self.data['frac'])
        E = self.__binary_to_decimal(self.data['exp'])
        bias = 2**(len(self.data['exp'])-1)-1
        if E == 0:
            e = 1 - bias
            normalized = 0
        else:
            e = E - bias
            normalized = 1
        mantissa = frac+normalized

        decimal_number = 2**e * mantissa
        if self.data['sign'] == '1':
            decimal_number *= -1
        if not '0' in self.data['exp'] and not '1' in self.data['frac']:
            if self.data['sign'] == '1':
                print("-inf")
            else:
                print("inf")
        elif not '0' in self.data['exp'] and '1' in self.data['frac']:
            print("NaN")

        else:
            print("Decimal:    %s\nFraction:    %s" % (decimal_number, Fraction(decimal_number)))



if __name__ == "__main__":
    if len(sys.argv) == 4:
        myInput = "%s %s %s" % (sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 2:
        myInput = sys.argv[2]
    else:
        myInput = raw_input()
    myObj = fpo(myInput)
    myObj.print_decimal()
