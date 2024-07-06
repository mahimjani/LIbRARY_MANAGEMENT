"""
1. Name
2. Aadhar No.
3. Mobile No.
4. Age

"""
print("WELCOME TO LIBRARY MANAGER")
import string
import random


print(' 1)Sin up 2)sin in ')
while True:
    try:
        while True:
            choise = int(input("Enter your choise :"))
            if choise == 1 or choise ==2:
                break
            print("Please Enter choise either 1 or 2")
    except:
        print("enter only decimal number.")
    else:
        break

def SIGN_UP():

    def passkey_generator():
        char_list = string.ascii_uppercase + string.digits
        passkey = "".join(random.choice(char_list) for _ in range(6))
        return passkey

    
    #try:
    
        name = input("ENTER YOUR FULL NAME HERE :")
        
        while True:
            # try:
                adhar_num = int(input("ENTER YOUR ADHAR NUM :"))
                if len(str(adhar_num)) == 12:
                    break
                
            # except:
            #     print("ENTER VALID AADHAR NUMBER...")  
                

        while True:
            try:       
                mobile_num = int(input("ENTER YOUR MOBILE NUMBER :"))
                if len(str(mobile_num))==10:
                    break
                
                # check if number is already register or not  
                
                
            except:
                print("ENTER VALID MOBILE NUMBER...")
        
        


        
        
        with open("sign_up",'a') as s:
            s.write(f"{mobile_num}\n{password}\n{adhar_num}\n{age}")
            
                
    #except:
    #     print("ERROR")

        age = int(input("ENTER YOUR AGE :"))
        password = passkey_generator()
        print(f"WELCOME {name}.YOUR ACCOUNT HAS BEEN CREATED...\n YOUR USER NAME IS {mobile_num} AND HERE IS YOUR PASSWORD {password} MAKE SURE TO SAVE IT.")
    SIGN_UP()
 
# def SIGN_IN():
#     number = int(input("ENTER YOUR MOBILE NUMBER"))
#     password = str(input("ENTER YOUR PASSWORD:"))

# choice = int(input("1. New User\n2. Existing User"))
# if choice == 1:
#     SIGN_UP()
# elif choice == 2:    
# SIGN_IN()
