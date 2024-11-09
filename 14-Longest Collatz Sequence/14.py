



max_count = 0 
final_anwer = 0 
for answer in range( 1000000 , 1 , -1 ) :
    temp = answer
    count_of_terms = 0 
    while answer != 1 :
        if answer % 2 == 0 :
            answer /= 2 
            count_of_terms += 1
        else :
            answer = ( answer * 3 ) + 1
            count_of_terms += 1 
    count_of_terms += 1 
    if count_of_terms > max_count :
        max_count =  count_of_terms
        final_anwer = temp
print ( "The final answer is  : {}  and the final max_count is : {}".format( final_anwer,max_count) )
    