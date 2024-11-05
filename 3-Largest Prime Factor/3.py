our_prime_numbers = []
def is_prime( number ) :
    is_prime = True
    for i in range ( 2 , int(number ** 0.5) + 1  ) :
        if number % i == 0 :
            is_prime = False
    return is_prime        
        
for i in range( 2 , 9999 ) :
    if (is_prime(i)) :
        our_prime_numbers.append(i)        

the_givven_number = 600851475143
biggest_prime_factor = 2
for i in our_prime_numbers :
    if ( the_givven_number % i == 0 ) :
        biggest_prime_factor = i
print ( "Apparently the biggest prime factor is : " , biggest_prime_factor )