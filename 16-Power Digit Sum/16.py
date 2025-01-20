
def sum( num : int ) -> int :
    final = 0 
    while num != 0 :
        final += num % 10
        num //= 10 
    return final

print(sum ( 2 ** 1000 ))