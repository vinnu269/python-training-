"""def primefact(n):
    fact=[]
    while n%2==0:
        fact.append(2)
        n//=2
    i=3
    while i*i<n:
        while n%i==0:
            fact.append(i)
            n//=i
        i+=2
    if n>2:
        fact.append(n)
    return fact
n=int(input())
print(primefact(n))"""


"""def palindrome(n):
    
    result=str(n)
        
    if result==result[::-1]:
         return True
    else:
        return False
n=int(input())
print(palindrome(n))"""





def perfectsquare(n):
    if n<0:
        return False
    i=0
    while i*i<=n:
        if i*i==n:
            return perfectsquare
        i+=1
    return not perfectsquare
n=int(input())
print(perfectsquare(n))
   













  
    


