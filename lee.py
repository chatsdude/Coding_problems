digits=[9,9,9,9,9,9,9,9]
if all(v==9 for v in digits):
    digits[0]=1
    for i in range(1,len(digits)):
        digits[i]=0
    digits.append(0)
res=digits
print(res)
    #digits[i]+=1
    #return digits
#print(is_nine(arr,len(arr)))
#print(res)