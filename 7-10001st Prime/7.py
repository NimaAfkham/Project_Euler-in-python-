def is_prime( number ) :
    for i in range( 2, int( number ** 0.5 ) + 1 ) :
        if number % i == 0 :
            return False
    return True

prime_numbers = [  ]
number = 2

while ( len( prime_numbers ) != 10002 ) :
    if is_prime( number ) :
        prime_numbers.append( number )
        number += 1
    else :  
        number += 1

print( prime_numbers[ 10000 ] )