def factorial(n):# o(n)
    m=1
    if(n==0 or n==1):
        return 1;
    else:
        for i in range(1,n+1):
            m=m*i
        return m;


