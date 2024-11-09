import math
#move to right as 1
#move to down as 0
def is_path ( bin_number , size ) :
    temp = str(bin_number)
    a = temp[2:len(temp)]
    a = a.zfill(size * 2)
    if a.count("1") == a.count("0") and ( a.count("1") + a.count("0") == size * 2 ) :
        print("One of the pathes : " , a)
        return True
    else :
        return False
    
size = int( input("Enter your n for n*n : ") )
start = 0
final = ( 2 ** ( size * 2 ) ) - 1
cursor = 0 
path_count = 0 
while cursor != ( final + 1 ) :
    if is_path( bin(cursor) , size ) :
        path_count += 1 
        cursor += 1 
    else :
        cursor += 1
print("final answer : " , path_count)
print("cheat answer : " , math.factorial(size * 2 ) / ( math.factorial(size) * math.factorial(size))) 