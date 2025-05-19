class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        if denominator == 0:
            return "undefined"
        flag = numerator * denominator
        if flag < 0:
            sign = "-"
        else:
            sign = ""
        numerator = abs(numerator)
        denominator = abs(denominator)

        if numerator % denominator == 0:
            return sign + str(numerator // denominator)
        else:
            return self.get_decimal(numerator, denominator, sign)
        
    def get_decimal(self, numerator: int, denominator: int, sign: str) -> str:
        '''
        This function calculates the decimal representation of a fraction.
        It handles both non-repeating and repeating decimals.
        '''
        integer_part = numerator // denominator
        decimal_part = ""
        remainder = numerator % denominator
        remainder_map = {}
        index = 0

        while remainder != 0:
            if remainder in remainder_map:
                # If the remainder has been seen before, we have a repeating decimal
                decimal_part = decimal_part[:remainder_map[remainder]] + "(" + decimal_part[remainder_map[remainder]:] + ")"
                break
            # Store the index of this remainder
            remainder_map[remainder] = index
            # Calculate the next digit in the decimal part
            remainder *= 10
            decimal_digit = remainder // denominator
            decimal_part += str(decimal_digit)
            # Update the remainder
            remainder %= denominator
            index += 1

        return sign + str(integer_part) + "." + decimal_part
    

# Example usage
if __name__ == "__main__":
    sol = Solution()
    numerator = 1
    denominator = 3
    result = sol.fractionToDecimal(numerator, denominator)
    print(f"Fraction: {numerator}/{denominator} -> Decimal: {result}")