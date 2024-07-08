"""
1. Name
2. Aadhar No.
3. Mobile No.
4. Age

"""
print("WELCOME TO LIBRARY MANAGER")



'''SAVING USER DATA TO TXT FILE NAMED 'SIGN_UP.TXT'...'''
def save_userdata(mobile_num,password,adhar_num,age):
    with open("sign_up.txt","a") as f:
        f.write(f"{mobile_num}\n{password}\n{adhar_num}\n{age}")


def get_userdata():
    with open("sign_up.txt","r") as f:
        data=f.readline()
        for i in data:
            pass

def SIGN_UP():

    '''generating password for user...'''
    import string
    import random
    def passkey_generator():
        char_list = string.ascii_uppercase + string.digits
        passkey = "".join(random.choice(char_list) for _ in range(6))
        return passkey

    


    '''COMMONN ERROR HANDLING FOR ALL INPUT CODE...'''
    try:
    
        name = input("ENTER YOUR FULL NAME HERE :")
        


        '''ERROR HANDLING FOR ADHAR NUMBER....'''
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




        '''ERROR HANDLING FOR MOBILE NUMBER...'''
        while True:
            try:       
                mobile_num = int(input("ENTER YOUR MOBILE NUMBER :"))
                if len(str(mobile_num))==10:
                    break
                
                else:
                    print("MOBILE NUMBER YOU ENTERED IS NOT FAIR..")
                    print("")
                # check if number is already register or not  
                
                
            except:
                print("ENTER VALID MOBILE NUMBER...")
                print("")
        
    except:
        print("ERROR")




        '''ERROR HANDLING FOR AGE....'''
        while True:
            try:
                age = int(input("ENTER YOUR AGE :"))
                if age == None:
                    print("ENTER VALID AGE...")
                    print("")
                elif age == int:
                    break
                else:
                    print("AGE CANNNOT BE EMPTY OR STRING...")
                    print("")
            except ValueError:
                print("AGE CANNNOT BE EMPTY OR STRING...")
                print("")
            except:
                print("ERROR OCCURED DUE TO INVALID INPUT...")
                print("")
    password = passkey_generator()
    print("YOUR PASSWORD IS : ",password)
    save_userdata(mobile_num,password,adhar_num,age)
        # print(f"WELCOME {name}.YOUR ACCOUNT HAS BEEN CREATED...\n YOUR USER NAME IS {mobile_num} AND HERE IS YOUR PASSWORD {password} MAKE SURE TO SAVE IT.")
SIGN_UP()



 
 
 
def SIGN_IN():
    number = int(input("ENTER YOUR MOBILE NUMBER"))
    password = str(input("ENTER YOUR PASSWORD:"))

    f = 




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
