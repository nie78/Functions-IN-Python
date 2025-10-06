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



while(True):
  choice = input("Choose an option:")
  print("1. Factorial")
  print("2. Find Max")
  print("3. Linear Search")
  print("4. Fibonacci")
  print("5. Login")
  print("6. Exit")
  if(choice=="1"):
      n=factorial(4)
      print(" the factorial of 4 is  ",n)
      break;
  elif(choice=="2"):
      n=find_max([1,8,20,7])
      print("The max of the list [1,8,20,7] is ",n)
      break;
  elif(choice=="3"):
      n=linear_search([2,4,6,9],3)
      print("Does the list [2,4,6,9] contain 3? ",n)
      break;
  elif(choice=="4"):
      n=fibonacci(5)
      print("The fibonacci of 5 is ",n)
      break;
  elif(choice=="5"):
      name=input("Enter your name")
      password=input("Enter your password")
      print(name, "you are logged in")
      break;
  elif(choice=="6"):
      print("your are exiting ")
      break;
