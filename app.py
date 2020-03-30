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

if __name__=='__main__':
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(add(a,b))
    print(sub(a,b))
    print(add_fact(a,b))
