special=[i for i in range(1,21)]
normal=[]
urgent=[]
super_urgent=[]
class Patient:

    def __init__(self,name="",status=0,specialization=0):
        self.name=name
        self.status=status
        self.specialization=specialization

    def set_info(self):
        self.name              =    input("enter your name           : ")
        self.status            =int(input("enter your status         : "))
        check                  =int(input("enter your specialization : "))
        while check<1 or check>20:
             print("sory enter the correct answer from |1 - 20 | ")
             check             =int(input("enter your specialization : "))

        self.specialization=check
        if special[check-1]==0:
            print("sory it is completed")
        else:
            special[check-1]-=1
            if  self.status == 0:
                normal.append(Patient(self.name,self.status,self.specialization))
            elif self.status==1:
                urgent.append(Patient(self.name,self.status,self.specialization))
            elif self.status==2:
                super_urgent.append(Patient(self.name,self.status,self.specialization))

    def get_info(self):
        print("name   = ",self.name)
        if self.status==0:
            print("status = normal")
        elif self.status ==1:
            print("status = urgent")
        else:
            print("status = super_urgent")
        print("specialization = ",self.specialization)
        print("\n\n")

    @staticmethod
    def remove_aleaving(name_,status_):
        if status_=='0' :
            for i in normal:
                if i.name==name_:
                    normal.remove(i)
                    print("yes")
                    break 
        elif status_=='1':
            for i in urgent:
                if i.name==name_:
                    urgent.remove(i)
                    break
        
        elif status_=='2':
            for i in super_urgent:
                if i.name==name_:
                    super_urgent.remove(i)
                    break
