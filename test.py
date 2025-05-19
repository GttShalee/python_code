# str = ["eat", "tea"]
# set = []

# for i in range(len(str)-1):
#     for j in range(len(str) - i):
        # print(str[j])

# def getPermutation(n: int, k: int) -> str:
#         nums = [str(i) for i in range(1, n + 1)]  # 数字集合
#         print(nums)

# getPermutation(3, 3)

def get_decimal(self, numerator: int, denominator: int, sign: str) -> str:
        integer_part = numerator // denominator
        decimal_part = ""
        reminder = numerator % denominator

        reminder_map = {}
        index = 0

        while reminder != 0:
                if reminder in reminder_map:
                        decimal_part = decimal_part[:reminder_map[reminder]] + "(" + decimal_part[reminder_map[reminder]:] + ")"
                        break
                reminder_map[reminder] = index
                reminder *= 10
                decimal_digit = reminder // denominator
                decimal_part += str(decimal_digit)
                reminder %= denominator
                index += 1

# Example usage
result = get_decimal(1, 3, "-")
print(result)

