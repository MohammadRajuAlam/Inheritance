# Here We are creating MultiLevel inheritance
class Grandpa:
    country="India"
    code="+91"
    
    def __init__(self,name,age,car):
        self.name=name
        self.age=age
        self.car=car
    def get_grandpa(self):
        print("This is Grandpa properties")
        print(f"Your Name is: {self.name}\nAge: {self.age}\nNo of Car: {self.car}\n")
        
    @classmethod
    def get_country(cls):
        print("This is grandpa country")
        print(f"Country Name: {cls.country}\nCountry Code: {cls.code}\n") #Raju
        
    @staticmethod
    def add_grandpa():
        village="Dih"
        city="Hisua"
        print(f"This is grandpa Address\nVillage Name: {village}\nCity: {city}\n")
        
class Father(Grandpa):
    country="Bangaladesh"
    code="+81"
    
    def __init__(self,name,age,car,land,shop):
        super().__init__(name,age,car)
        self.land=land
        self.shop=shop
        
    def get_father(self):
        print(f"This is father's properties\nLand: {self.land}\nNo of Shop: {self.shop}")
        
    @classmethod
    def get_f_country(cls):
        Grandpa.get_country()
        print(f"Father's Country: {cls.country}\nCode: {cls.code}\n")
        
    @staticmethod
    def get_f_static(watch,tv):
        watch=watch
        tv=tv
        print(f"This is static of Father\nWatch: {watch}\nTV: {tv}\n")

class Son(Father):
    scountry="US"
    scode="+1"
    def __init__(self,name,age,car,land,shop, school,clas,roll,__pswd):
        super().__init__(name,age,car,land,shop)
        self.school=school
        self.clas=clas
        self.roll=roll
        self.__pswd=__pswd        
    def get_son(self):
        print(f"This is Son properties\nSchool Name: {self.school}\nClass: {self.clas}\nRoll No: {self.roll}\n")
        
    def get_pswd(self):
        return self.__pswd
    
    def __set_acc(self):
        self.acc=12345687
        self.__code=4578
        print(f"This child Acc No: {self.acc}\nCode: {self.__code}\n")
        
    def get_bank(self):
        return self.__set_acc()   
    @classmethod
    def get_s_country(cls):
        print(f"Son Country: {cls.scountry}\nSon Country Code: {cls.scode}\n")
        return Father.get_f_country()
    
class Grandson(Son):
    address="Electronic City Bangalore"
    state="Karnataka"
    def __init__(self, name, age, car, land, shop, school, clas, roll, __pswd, designation,salary,phone,email):
        super().__init__(name, age, car, land, shop, school, clas, roll, __pswd)
        self.designation=designation
        self.salary=salary
        self.phone=phone
        self.email=email
        
    def get_gson(self):
        print(f"This is Grandson properties:\nDesignation: {self.designation}\nSalary: {self.salary}\nPhone No: {self.phone}\nEmail: {self.email}\n")

    @classmethod
    def get_gs_add(cls):
        print(f"This is Grandson class varible:\nAddress: {cls.address}\nState: {cls.state}\n")
               
# Here We are creating Father object
#f=Father("Md Rajjak",88,0,"13 Dismil",1) # These are parameter: name,age,car,land,shop
# f.get_father() # Here We are accessing Father Properties
# f.get_grandpa() # Here We are using Grandpa properties
# Grandpa.get_country() # Here We are using Grandpa (class variable) properties using Class Name
# f.get_f_country() # Here We are using Father (class variable) properties using object Name 
# Father.get_f_country() # Here We are using Father (class variable) properties using object Name #
# f.add_grandpa() # Here We are accessing Grandpa (static varibles) properties using object
# Father.add_grandpa() # Here We are accessing Grandpa (static varibles) properties using class Name
# f.get_f_static("Sonata","Onida") # Here We are accessing Father (static varibles) properties using object Name
# Father.get_f_static("Sonata","Onida") # Here We are accessing Father (static varibles) properties using object Name

# Here We Creating Son Object

s=Son("Jakir",95,1,"13 Dismil",1,"Jeevan Deep","10th",77,"rsts745PI") # These are parameter: name,age,car,land,shop, school,clas,roll,__pswd
# Here We are accessing Grandpa properties using Son object and also Son class name
#s.get_grandpa() # Here We are accessing grandpa (instance varibles) properties using object
#s.get_country() # Here We are accessing grandpa (class varibles) properties using object
#Son.get_country() # Here We are accessing grandpa (class varibles) properties using using Son class Name
#s.add_grandpa() #  Here We are accessing grandpa (static varibles) properties using object
#Son.add_grandpa() # Here We are accessing grandpa (static varibles) properties using Class Name

# Here We are accessing Father properties using Son object and also Son class name
#s.get_father() # Here We are accessing Father (instance varibles) properties using Son object
#s.get_f_country()# Here We are accessing father (class varibles) properties using son object
#Son.get_f_country() # Here We are accessing father (class varibles) properties using son class
#s.get_f_static("Sonam","LG") # Here We are accessing father (static varibles) properties using son object
#Son.get_f_static("Sonam","LG")# Here We are accessing father (static varibles) properties using son class

# Here We are accessing Son properties using Son object and also Son class name
#s.get_son()
#print(s.__pswd) # Here We are trying to access private variable of Outside class, We can't access. 
#print(s._Son__pswd)  # Here We can access private variable outside class using _Son with variable name here Son is class Name
#s.__set_acc() # Here We are trying to access private function of Outside class, We can't access.
#s._Son__set_acc() # Here We can access private function of outside class using _Son with private function name here Son is class Name
#s.get_bank() # Here We are accessing private variable using returning (calling) instance method with Son object
#s.get_s_country() # Here We are accessing static methof of Son class using Son object
#Son.get_s_country() # Here We are accessing static method of Son class using Son class

# Here We Creating GrandSon Object 
gs=Grandson("Jakir",95,1,"13 Dismil",1,"Jeevan Deep","10th",77,"rsts745PI","Software Engineer", "8 LPA", 8892478965,"md12@gmail.com")  # These are parameter: name, age, car, land, shop, school, clas, roll, __pswd, designation,salary,phone,email
#gs.get_gson()
#gs.get_gs_add()
#Grandson.get_gs_add()
#gs.get_grandpa()
#gs.get_father()
gs.get_son()