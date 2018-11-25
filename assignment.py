print("call the function f(input the number number of people)")
def f(no_people):
    roomtype=input("enter the room you want to stay in: ")
    if roomtype=="single":
        print("the charges for the single room are:1500"+"\n"+"iron cloths=100(per cloth)"+"\n"+"wash (per cloth)=300"+"\n"+"taxi (per km)=40")
        z=input('Do you want to book the room?').lower()
        if z=="yes":
            cloths=input("Do you want to iron:").lower()
            wash=input("Do you want to wash:").lower()
            taxi=input("do you want to ride by the taxi: ").lower()
            days=eval(input('number of days user wants to spend(in integer): '))                      
            if cloths=='yes':
                if wash=='yes' :
                    if taxi =='yes':
                        no_cloths=eval(input("no of clothes"))
                        amount_iron=100*no_cloths
                        no_wash=eval(input('no of cloths you want to wash: '))
                        amount_wash=300*no_wash
                        print(('='*20)+'\n'+'Room Charges |'+str(no_people*1500)+'per day'+'\t'+'for'+str(days)+'it will be: '+str(no_people*1500*days)+'\n'+'Iron Cloths | '+str(amount_iron)+'\n'+'Washing charges(it will take a day) | '+str(amount_wash)+'\n'+('='*20)+'\n'+'Total bill : '+str((no_people*1500*days)+amount_iron+amount_wash))
                        print('_'*20)
                        print('thanks for choosing our hotel')
                        print('NOTE : Your bill for taxi will be generated at the time of check out(rs 40 per km).')
            elif cloths=='no':
                if wash=='yes':
                    no_wash=eval(input('no of cloths you want to wash: '))
                    amount_wash=300*no_wash
                    print(('='*20)+'\n'+'Room Charges |'+str(no_people*1500)+'per day'+'\t'+'for'+str(days)+'it will be: '+str(no_people*1500*days)+'\n'+'Washing charges(it will take a day) | '+str(amount_wash)+'\n'+('='*20)+'\n'+'Total bill : '+str((no_people*1500*days)+amount_wash))
                    print('_'*20)
                    print('thanks for choosing our hotel')
                    print('NOTE : Your bill for taxi will be generated at the time of check out(rs 40 per km).')
            elif cloths =='yes':
                if wash =='no':
                    no_wash=eval(input('no of cloths you want to wash: '))
                    amount_wash=300*no_wash
                    print(('='*20)+'\n'+'Room Charges |'+str(no_people*1500)+'per day'+'\t'+'for'+str(days)+'it will be: '+str(no_people*1500*days)+'\n'+'Iron Cloths | '+str(amount_iron)+'\n'+('='*20)+'\n'+'Total bill : '+str((no_people*1500*days)+amount_iron))
                    print('_'*20)
                    print('thanks for choosing our hotel')
                    print('NOTE : Your bill for taxi will be generated at the time of check out(rs 40 per km).')                    
    else:
        print("the charges for the single room are:2500"+"\n"+"iron cloths=100(per cloth)"+"\n"+"wash (per cloth)=300"+"\n"+"taxi (per km)=40")
        z=input('Do you want to book the room?').lower()
        if z=="yes":
            cloths=input("Do you want to iron:").lower()
            wash=input("Do you want to wash:").lower()
            taxi=input("do you want to ride by the taxi: ").lower()
            days=eval(input('number of days user wants to spend(in integer): '))                      
            if cloths=='yes':
                if wash=='yes' :
                    if taxi =='yes':
                        no_cloths=eval(input("no of clothes"))
                        amount_iron=100*no_cloths
                        no_wash=eval(input('no of cloths you want to wash: '))
                        amount_wash=300*no_wash
                        print(('='*20)+'\n'+'Room Charges |'+str((no_people//2)*2500)+'per day'+'\t'+'for '+str(days)+' days it will be: '+str((no_people//2)*2500*days)+'\n'+'Iron Cloths | '+str(amount_iron)+'\n'+'Washing charges(it will take a day) | '+str(amount_wash)+'\n'+('='*20)+'\n'+'Total bill : '+str(((no_people//2)*2500*days)+amount_iron+amount_wash))
                        print('_'*20)
                        print('thanks for choosing our hotel')
                        print('NOTE : Your bill for taxi will be generated at the time of check out(rs 40 per km).')
            elif cloths=='no':
                if wash=='yes':
                    no_wash=eval(input('no of cloths you want to wash: '))
                    amount_wash=300*no_wash
                    print(('='*20)+'\n'+'Room Charges |'+str((no_people//2)*2500)+'per day'+'\t'+'for '+str(days)+' days it will be: '+str((no_people//2)*2500*days)+'\n'+'Washing charges(it will take a day) | '+str(amount_wash)+'\n'+('='*20)+'\n'+'Total bill : '+str(((no_people//2)*2500*days)+amount_wash))
                    print('_'*20)
                    print('thanks for choosing our hotel')
                    print('NOTE : Your bill for taxi will be generated at the time of check out(rs 40 per km).')
            elif cloths =='yes':
                if wash =='no':
                    no_wash=eval(input('no of cloths you want to wash: '))
                    amount_wash=300*no_wash
                    print(('='*20)+'\n'+'Room Charges |'+str((no_people//2)*2500)+'per day'+'\t'+'for '+str(days)+' days it will be: '+str((no_people//2)*2500*days)+'\n'+'Iron Cloths | '+str(amount_iron)+'\n'+('='*20)+'\n'+'Total bill : '+str(((no_people//2)*2500*days)+amount_iron))
                    print('_'*20)
                    print('thanks for choosing our hotel')
                    print('NOTE : Your bill for taxi will be generated at the time of check out(rs 40 per km).')
                        
    
        
