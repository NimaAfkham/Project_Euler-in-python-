def is_palindromic( number ) :
    if ( str(number)[::-1] == str(number)[::+1] ) :
        return True
    else :
        return False 
    
largest_palindromic_number = 0
for i in range ( 100 , 1000 ) :
    for j in range ( 100 , 1000 ) :
        number = i * j 
        if is_palindromic( number ) :
            if ( number > largest_palindromic_number ) :
                largest_palindromic_number = number
            
            
                    
print ( "the largest thing that i've found " , largest_palindromic_number )