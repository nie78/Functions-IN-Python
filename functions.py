def factorial(n):# o(n)
    m=1
    if(n==0 or n==1):
        return 1;
    else:
        for i in range(1,n+1):
            m=m*i
        return m;


def find_max(list):# o(n)
    n= len(list)
    max=list[0]
    for i in range(0,n):
      if(list[i]>max):
          max=list[i]
    return max;



def linear_search(list,target):#o(n)
    n=len(list)
    for i in range (0,n):
        if(list[i]==target):
           return True;
    else:
        return False; 


def fibonacci(m):#o(2^n)
    if(m==0 or m==1):
        return 1;
    else:
        return fibonacci(m-1)+fibonacci(m-2);