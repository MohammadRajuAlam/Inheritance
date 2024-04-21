# Single inheritance
class Mobile:
    location="Bangalore"
    pincode=560029
    
    def __init__(self,m_name,model,color,s_size,ram,os, price):
        self.mobile_name=m_name
        self.model=model
        self.color=color
        self.screen_size=s_size
        self.ram=ram
        self.os=os
        self.price=price
        
    def get_mobile_detail(self):
        print(f'Mobile Name: {self.mobile_name}\nModel No: {self.model}\nColor: {self.color}\nScreen Size: {self.screen_size}\nRam Size: {self.ram}\nOperating System: {self.os}\nPrice :{self.price}')
        
    @classmethod
    def get_location(cls):
        print(f"Current Location: {cls.location}\nPin Code: {cls.pincode}")
        
class Recharge(Mobile):
    def __init__(self,m_name,model,color,s_size,ram,os, price):
        #super().__init__("Redme","Redme note 8", "blue","2.5 inches",'128 GB',"IOS System",12000)
        super().__init__(m_name,model,color,s_size,ram,os, price)
        
    def get_recharge(self):
        print("Recharge pack is:\nRs 155, 179, 210, 310, 509, 777\nYou can Select any package\n")
        self.recharge=int(input("Enter Rs for Recharge\n"))
        
        if self.recharge==155:
            print(f"Rs {self.recharge} Recharge Done\nunlimited Voice call\n2 GB Data/Pack\n300 SMS\nValidity 28 Days")
            
        elif self.recharge==179:
            print(f"Rs {self.recharge} Recharge Done\nunlimited Voice call\n1 GB Data/Day\n100 SMS/Day\nValidity 28 Days")
            
        elif self.recharge==210:
            print(f"Rs {self.recharge} Recharge Done\nunlimited Voice call\n1.5 GB Data/Day\n100 SMS/Day\nValidity 28 Days")
        
        elif self.recharge==310:
            print(f"Rs {self.recharge} Recharge Done\nunlimited Voice calling\n2 GB Data/Day\n200 SMS/Day\nValidity 56 Days")
            
        elif self.recharge==509:
            print(f"Rs {self.recharge} Recharge Done\nunlimited Voice calling\n2 GB Data/Day\n200 SMS/Day\nValidity 75 Days")
        elif self.recharge==777:
            print(f"Rs {self.recharge} Recharge Done\nunlimited Voice calling\n2.5 GB Data/Day\n300 SMS/Day\nValidity 90 Days")
        else:
            print(f"Sorry\nRs {self.recharge} recharge is not available")

rech=Recharge("Redme","Redme note 8", "blue","2.5 inches",'128 GB',"IOS System",12000)
#rech.get_mobile_detail()
#rech.get_location()
rech.get_recharge()