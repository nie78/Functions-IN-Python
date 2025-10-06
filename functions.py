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