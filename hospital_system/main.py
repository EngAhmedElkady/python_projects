import patient
out="""
1) add new patient
2) print all patients
3) get next patient
4) remove a leaving atient
5) end program
"""
print(out)
choice =int(input("enter your choice : "))
while choice>0 and choice <5:
    if choice==1 :
       x=patient.Patient()
       x.set_info()
    elif choice==2:
        for i in patient.super_urgent:
            i.get_info()
        for k in patient.urgent:
            k.get_info()
        for l in patient.normal:
            l.get_info()
    elif choice==3:
        if len(patient.super_urgent)>0:
            patient.super_urgent[0].get_info()
            oo=patient.super_urgent.remove(patient.super_urgent[0])
        elif len(patient.urgent)>0:
            patient.urgent[0].get_info()
            oo=patient.urgent.remove(patient.urgent[0])
        elif len(patient.normal)>0:
            patient.normal[0].get_info()
            oo=patient.normal.remove(patient.normal[0])
    
    elif choice==4:
        name=  input("enter your name   : ")
        status=input("enter your status : ")
        patient.Patient.remove_aleaving(name,status)
        


    print(out)
    choice =int(input("enter your choice : "))

