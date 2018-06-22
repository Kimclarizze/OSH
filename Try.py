Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.

>>> print("Hello, world!")


>>> name = input ("What's your name?")
>>> print("Hello " + name)

>>> a=input("First number?")
>>> b=input("Second number?")
>>> sum = a+b
>>> print ("Sum is " + sum)


>>> a=input("First?")
>>> b=input("Second")
>>> sum=int(a)+int(b)
>>> print(str(sum))


>>> 5==5

>>> age = input("How old are you? ")
>>> if int(age) > 18:
	print("Go!")
else:
	print("Stop!")


>>> a=input("First number?")
>>> b=input("Second number?")
>>> c=input("Operator(+,-,*,/)")
Operator(+,-,*,/)*
>>> if c=='+':
	sum = int(a) + int(b)
	print (str(sum))
elif c=='-':
	dif = int(a) - int(b)
	print (str(dif))
elif c=='*':
	prod = int(a) * int(b)
	print (str(prod))
elif c=='/':
	div = int(a) / int(b)
	print (str(div))
else:
	print("Annyeong!")

class Person:

    def __init__(self, first, last):
        self.a= first
        self.b= last

    def Name(self):
        return self.a + " " + self.b

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.num = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.num

x = Person("A", "B")
y = Employee("H", "B", "7")

print(x.Name())
print(y.GetEmployee()) 
