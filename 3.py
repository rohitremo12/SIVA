number=[0,1,2,5,6,8,9]
def result(a):
    count=0
    for i in range(1,999999):
        b=str(i)
        for k in b:
            if int(k) not in number:
                break
        else:
            count+=1
            if count==a:
                answer=i
                break
    return answer
a=int(input())
print(result(a))
