def factorial_num(n):
    if n<=1:
        return 1
    return n*factorial_num(n-1)
n=int(input("Enter a number: "))
print(f"Factorial of {n} is : {factorial_num(n)}")