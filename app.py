import sys

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def add_fact(a,b):
	return fact(add(a,b))

def fact(a):
	if a < 0: 
		return "Factorial of Negative Number!"
	elif a == 0 or a==1:
		return 1
	else:
		return a * fact(a-1)

def divison(n,d):
    if d!=0:
        return n/d
    else:
        return "Divison Not Possible"

def facofsub(a,b):
    if a>b: 
        diff=a-b
    else: 
        diff=b-a
    return factorial(diff)

def factorial(c):
    if c==0:
        return 1
    return c*factorial(c-1)
    
if __name__=='__main__':
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(add(a,b))
    print(sub(a,b))
    print(facofsub(a,b))
