# Compute 3x+1
def f(x):
    return 3*x+1

if __name__ == '__main__':
    x=f(2)
    print(x)
    l = lambda x: 3*x+1
    y=l(2)
    print(y)

    # "title" function capitalizes first letter of string
    full_name=lambda fn,ln: fn.strip().title()+" "+ln.strip().title() 
    name=full_name("  jOhn","smith   ")
    print(name)
