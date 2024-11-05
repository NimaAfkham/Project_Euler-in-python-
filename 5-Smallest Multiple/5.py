multiple_list = [ 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 ]
idea = [ 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 ]
test = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
a = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19
print ( " a is : " , a )
x = 9835339
the_answer = 0 
number = a
while ( True ) :
    print(number)
    
    status = True
    for j in idea :
        if number % j != 0 :
            status = False
            break
    if ( status ):
        the_answer = number
        break
    number += 1 
    
print( "the final answer is : " , the_answer )