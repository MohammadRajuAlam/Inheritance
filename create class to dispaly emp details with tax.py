# Wap to display employee deatail with 20/ tax from salary and also find per day salary from given monthly salary
class Employee:
    company="IMB"
    located="Bangalore"

    def __init__(self,id=0,name=None,age=0,department=None,salary=0):
        self.id=id
        self.name=name
        self.age=age
        self.department=department
        self.__salary=salary # Salary is private variable

    def get_employee(self):
        print(f"Id: {self.id}\nName: {self.name}\nAge: {self.age}\nDepartment: {self.department}\nSalary{self.salary}\n")
        print(f"Rs {self.set_tax()} are Actual salary") # Here calling set_tax method
        print(f"Rs {self.per_day_salary()} are per day salry") # Here Calling per_day_salary method
        
    def set_tax(self):
        tax=__self.salary*20//100 #OR self.salary * 0.2
        return tax # Here Tax is a local variable you can't access outside class
    
    def per_day_salary(self):
        self.perday=__self.salary/30
        return self.perday
    
    @classmethod
    def get_company(cls):
        print(f"Company Name: {cls.company}\nLoacated: {cls.located}\n")
        
obj=Employee(121,"Om Prakash",27,"Financial", 50000)
obj2=Employee(241,"Suraj Kumar",29,"HR",100000)
print(obj.name)
#print(obj.__salary) # Here salary is private variable we can't access outside class # we can access _className
print(obj._Employee__salary) # Here We can access private variable or private method outside function usin _className
