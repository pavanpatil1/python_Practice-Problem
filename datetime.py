import datetime
from pavan import Time
from date import Date

class Datetime(Date,Time):
    
    def __init__(self,day,date,month,year,hour,minute,second,ap):
        Date.__init__(self,day,date,month,year)
        Time.__init__(self,hour,minute,second,ap)
 
    @staticmethod
    def setDate():
        de = datetime.datetime.today()
        p = de.weekday()
        if(p == 0):
            day = "Monday"
        elif(p == 1):
            day = "Tuesday"
        elif(p == 2):
            day = "Wednesday"
        elif(p == 3):
            day = "Thusday"
        elif(p == 4):
            day = "Friday"
        elif(p == 5):
            day = "Saturday"
        else:
            day = "Sunday"


        s= de.month
        if(s == 1):
            month = "January"
        elif(s == 2):
            month = "February"
        elif(s == 3):
            month = "March"
        elif(s == 4):
            month = "April"
        elif(s == 5):
            month = "May"
        elif(s == 6):
            month = "June"
        elif(s == 7):
            month = "July"
        elif(s == 8):
            month = "August"
        elif(s == 9):     
            month = "Sepetember"
        elif(s == 10):        
            month = "Octomber"
        elif(s == 11):    
            month = "November"
        else:
            month = "December"

        return day,month 

    
    @staticmethod
    def getDate():
        de = datetime.datetime.today()
        return de.day,de.year

    
    @staticmethod
    def setTime():
        de = datetime.datetime.today()
        if(de.hour > 12):
            hour = de.hour - 12

        if(de.hour <= 12):
            k = "AM"
        else:
            k = "PM"

   
        return hour,k
    

    
    @staticmethod
    def getTime():
        de = datetime.datetime.today()
        return de.minute,de.second 

    def display(self):
        print self.day,self.date,self.month,self.year,"and",self.hour,":",self.minute,":",self.second,":",self.ap
        


def main():
    
    day,month = Datetime.setDate()
    date,year = Datetime.getDate()
    hour,ap = Datetime.setTime()
    minute,second = Datetime.getTime()
    
    n = Datetime(day,date,month,year,hour,minute,second,ap)

    n.display()

    
   

if __name__ == '__main__':
    main()



        
    
