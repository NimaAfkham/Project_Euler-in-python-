def f3(num: int) -> int:
    mapping = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 0: 0}
    return mapping.get(num, 0)

def f2(num: int) -> int:
    mapping = {2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}
    return mapping.get(num, 0)

def kk(num: int) -> int:
    mapping = {10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}
    return mapping.get(num, 0)

def ppp(number: int) -> int:
    final_result = 0
    if number >= 100:
        final_result += f3(number // 100) + 7  # "hundred"
        if number % 100:
            final_result += 3  # "and"
    number %= 100
    if 10 <= number <= 19:
        final_result += kk(number)
    else:
        final_result += f2(number // 10)
        final_result += f3(number % 10)
    return final_result

total_sum = sum(ppp(i) for i in range(1, 1000)) + 11  # "one thousand"
print(f"The final result is {total_sum}")
