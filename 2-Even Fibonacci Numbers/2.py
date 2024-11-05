f1 = 0
f2 = 1
f3 = 1

sum_of_even_valued_numbers = 0
print ( f1 , f2  , f3 , sep="\n" )
while ( f3 + f2 < 4000000 )  :
    f1 = f2 
    f2 = f3 
    f3 = f1 + f2 
    print ( f3 )
    if f3 % 2 == 0 :
        sum_of_even_valued_numbers += f3
        
print ( "The sum is : " , sum_of_even_valued_numbers )