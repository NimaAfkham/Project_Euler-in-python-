f1 = 0
f2 = 0
for i in range(1,101):
    f1 += ( i ** 2 )
sum = 0 
for j in range(1,101):
    sum += j
    f2 = sum ** 2 

print("F1 : " , f1 )
print("F2 : " , f2 )
final_Resalt = f2 - f1 
print("Hence : " , final_Resalt )