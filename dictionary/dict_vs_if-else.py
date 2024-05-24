def do_one(x):
    print("one: x*1=", x*1)
def do_two(x):
    print("two: x*2=", x*2)
def do_three(x):
    print("three: x*3=", x*3)
def do_def(x):
    print("default: x=", x)

x=2

# If Else
if x==1:
    do_one(x)
elif x==2:
    do_two(x)
elif x==3:
    do_three(x)
else:
    do_def(x)

# Dictionary approach
actions={1:do_one,2:do_two,3:do_three}

action=actions.get(x,do_def)
action(x)

# From: https://www.youtube.com/shorts/UFdEp9wrtOY