#class student:
 #   def __init__(self,name,roll_no,branch):
 #      self.roll_no = roll_no
  #      self.branch = branch


#Student = student("Swetha",130,"CSE")
#print(Student.name)
#print(Student.roll_no)
#print(Student.branch)


#class fruit:
 #   def __init__(self,name):
  #      self.name=name
   # def names(self):
    #    print("the fruit name is: " + self.name)
#fruitname = fruit("Apple")
#fruitname.names()        


#class employee:
 #   def work(self):
  #      print("Working")
#class manager(employee):
 #   pass
#m = manager()
#m.work()        


class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
Employee1=employee('Ram',50000)    
Employee1.salary=80000
print(Employee1.salary)    

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
Employee1=employee('Ram',50000)    
Employee1.salary=80000
print(Employee1.salary)    
 

class employee:
    def __init__(self,name):
        self.name=name
        self.__salary=50000
Employee1=employee('Ram')    
Employee1.salary=80000
print(Employee1.__salary)    


class student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark

stud1=student("lily",56)
stud2=student("Bobby",76)        