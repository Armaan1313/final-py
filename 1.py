a={}
print("menu\n 1. Add a record.\n 2. Search a record.  \n 3. update a record . \n 4. sort the record alphabetically. \n 5. delete a record .\n 6. Quit")
x=int(input("what your choice : "))
while(x!=6):
    if x==1:
             p=input("enter name")
             q=int(input("enter your phone number"))
             a.update({p:q})
             print("record added")
        
    elif x==2:
            p=input("enter name to search")
            p=int(input("enter your phone number"))
            print("record added")
        
    elif x==3:
            p=input("enter name to search")
            p=int(input("enter your phone number"))
            print("record updated")
            
    elif x==4:
           
            la=list(a.keys())
            la.sort()
            sala={i:a[i] for i in la}
            print(sala)



 
    elif x==5:
            p=input("enter name to search")
            print("record deleted")
            
    elif x==6:
            print("exit from the whole program")
    x=int(input("what your choice : "))

       
    print("menu\n 1. Add a record.\n 2. Search a record.  \n 3. update a record . \n 4. sort the record alphabetically. \n 5. delete a record .\n 6. Quit")
    
 
