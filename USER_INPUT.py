"""
1. Name
2. Aadhar No.
3. Mobile No.
4. Age

"""
print("WELCOME TO LIBRARY MANAGER")




def SIGN_UP():

    '''generating password for user...'''
    import string
    import random
    def passkey_generator():
        char_list = string.ascii_uppercase + string.digits
        passkey = "".join(random.choice(char_list) for _ in range(6))
        return passkey

    
    try:
    
        name = input("ENTER YOUR FULL NAME HERE :")
        
        while True:
            try:
                adhar_num = int(input("ENTER YOUR ADHAR NUMBER :"))
                if adhar_num == None :
                    print("ENTER VALID ADHAR NUMBER HERE...")
                    print("")
                elif len(str(adhar_num)) == 12:
                    break
                else:
                    print("SOME ERROR OCCURED DUE TO INVALID INPUT...")
                    print("")
                
            except ValueError:
                print("ADHAR NUMBER CANNOT CONSIST STRING ANYWAY...")
                print("")
            except:
                print("SOME ERROR OCCURED DUE TO INVALID INPUT...")
                print("")
        
        while True:
            try:       
                mobile_num = int(input("ENTER YOUR MOBILE NUMBER :"))
                if len(str(mobile_num))==10:
                    break
                
                # check if number is already register or not  
                
                
            except:
                print("ENTER VALID MOBILE NUMBER...")
        
        


        
        
        # with open("sign_up",'a') as s:
        #     s.write(f"{mobile_num}\n{password}\n{adhar_num}\n{age}")
            
                
    except:
        print("ERROR")

        age = int(input("ENTER YOUR AGE :"))
        password = passkey_generator()
        # print(f"WELCOME {name}.YOUR ACCOUNT HAS BEEN CREATED...\n YOUR USER NAME IS {mobile_num} AND HERE IS YOUR PASSWORD {password} MAKE SURE TO SAVE IT.")
SIGN_UP()
 
def SIGN_IN():
    number = int(input("ENTER YOUR MOBILE NUMBER"))
    password = str(input("ENTER YOUR PASSWORD:"))





# '''asking for login or signup'''
# print('1) Sin-up \n2) sin-in ')
# while True:
#     try:
#         choice = int(input("ENTER YOUR CHOICE :"))
#         if choice == 1:
#             # SIGN_UP()
#             break
#         elif choice == 2:
#             # SIGN_IN()
#             break
#         else:
#             print("ENTERD CHOICE IS NOT AVAILABLE...")
#             print("")

#     except ValueError:
#         print("ENTER YOUR CHOICE IN INTERGER...")
#         print("")

#     except:
#         print("EROOR OCCURED DUE TO INVALID INPUT...")
#         print("")
