thisdict =  {
  "apple": "green",
  "banana": "yellow",
  "cherry": "red"
}
print(thisdict)

thisdict["apple"] = "red"
print(thisdict)

thisdict = dict(apple="green", banana="yellow", cherry="red")
thisdict["damson"] = "purple"
print(thisdict)

a = 11
b = 21
if b > a:
  print("b is greater than a")



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




class Robot:
    count = 0
    def __init__(self, name):
        self.name = name
    def sayHello(self):
        return "Hi, I am " + self.name
def Rob_init(self, name):
    self.name = name
Robot2 = type("Robot2", 
              (), 
              {"counter":0, 
               "__init__": Rob_init,
               "sayHello": lambda self: "Hi, I am " + self.name})
x = Robot2("Marvin")
print(x.name)
print(x.sayHello())
y = Robot("Marvin")
print(y.name)
print(y.sayHello())
print(x.__dict__)
print(y.__dict__)