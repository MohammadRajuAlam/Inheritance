# Create a class display student result with Division, Total Marks, And percentages max Marks 100 and Min Marks 0
from datetime import datetime
class Student:
    board="BSEB"
    location="Patna"
    clas="10th"
    year_of_result=2024
    
    def __init__(self,name, hindi, math, sanskrit, science, ssc, english):
        self.name=name
        self.hindi=hindi
        self.math=math
        self.sanskrit=sanskrit
        self.science=science
        self.ssc=ssc
        self.english=english
        
    def total_marks(self):
        if (self.hindi>=0 and self.hindi<=100) or (self.math>=0 and self.math<=100) or (self.sanskrit>=0 and self.sanskrit<=100) or (self.science>=0 and self.science<=100) or(self.ssc>=0 and self.ssc<=100) or (self.english>=0 and self.english<=100):
            if (self.hindi>=30 and self.hindi<=45) or (self.math>=30 and self.math<=45) or (self.sanskrit>=30 and self.sanskrit<=45) or (self.science>=30 and self.science<=45) or(self.ssc>=30 and self.ssc<=45):
            
                self.sm=self.hindi+self.math+self.sanskrit+self.science+self.ssc
                
                return  self.sm #f"3rd Division\nTotal Marks: {self.sm}\nOptional\nEnglish Marks: {self.english}" # \n{datetime.now()}
            
            elif (self.hindi>45 and self.hindi<59) or (self.math>45 and self.math<59) or (self.sanskrit>45 and self.sanskrit<59) or (self.science>=45 and self.science<=59) or(self.ssc>45 and self.ssc<59):
                return self.sm #f"2nd Division\nTotal Marks: {self.sm}\nOptional\nEnglish Marks: {self.english}"
            
            elif (self.hindi>=60 and self.hindi<=100) or (self.math>=60 and self.math<=100) or (self.sanskrit>=60 and self.sanskrit<=100) or (self.science>=60 and self.science<=100) or(self.ssc>=60 and self.ssc<=100):
                return self.sm #f"1st Division\nTotal Marks: {self.sm}\nOptional\nEnglish Marks: {self.english}"
            
            elif (self.hindi>=0 and self.hindi<29) or (self.math>=0 and self.math<29) or (self.sanskrit>=0 and self.sanskrit<29) or (self.science>=0 and self.science<29) or(self.ssc>=0 and self.ssc<29):
                return self.sm#f"Fail\nTotal Marks: {self.sm}\nOptional\nEnglish Marks: {self.english}"
        else:
            return "invalid i/p given less than 0 or more than 100"
        
    def average(self):
        self.average=self.sm/5
        return f"Your {self.average} %\n{datetime.now()}"
    
    @classmethod
    def get_board(cls):
        return f"Board Name: {cls.board}\nLOcation: {cls.location}\nClass: {cls.clas}\nYear of Result: {cls.year_of_result}\n{datetime.now()}"
    
res=Student("Rakib",80,60,71,95,66,88)
res.total_marks()
