# From CSDojo
# A naive recursive solution
def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result

# A memoized solution
def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_2(n, memo)

# A bottom-up solution
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

while True:
    try:
        result=0
        n=int(input("Input number: "))
        print("1 -(Naive) 2 -(Memoized) 3 -(Bottom Up)")
        version=int(input("Which algorithm?(1-3): "))
    except:
        print("Invalid input")
    if version==1:
        result=fib(n)
    elif version==2:
        result=fib_memo(n)
    elif version==3:
        result=fib_bottom_up(n)
    elif version>=4:
        print("Out of range!")
    print(result)
