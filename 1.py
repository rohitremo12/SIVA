def base3(num):  
    q = num/3    
    r = num%3
    if q == 0:   
        return ""
    else:
        return base3(int(q)) + str(int(r))    
num = int(input()) 
print(base3(num))
