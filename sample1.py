print "Hello World!!!!"
print "this is the start to something powerful :)"

#this is a comment

def greet(name= "Sean"):
    print("Hello,", name)

def mult_by_five(x):
    return 5 * x


print mult_by_five(15)

greet(name="John")


def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
)