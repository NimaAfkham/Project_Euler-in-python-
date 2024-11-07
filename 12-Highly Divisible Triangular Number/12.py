def divisor_count( number ):
    count = 1 
    jzr =  int ( number ** 0.5 ) 
    for i in range( 2 , jzr + 1 ) :
        if number % i == 0 and i * i == number :
            count += 1 
        elif number % i == 0 :
            count += 2
    return ( count + 1 )

triangle_numbers = 0
last_number = 1
while True :
    triangle_numbers +=  last_number 
    last_number += 1
    if divisor_count(triangle_numbers) > 5 :
        print( "answer : " , triangle_numbers )
        break