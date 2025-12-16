import string 
full_alphabet = string.ascii_letters

print("Welcome Our Password Generator App")
while True:
    is_entered = input("Please Enter Password That You Want To Create: ")

    if len(is_entered.strip()) < 8:
        print("Your passsword must be at leat 8 charachters !")
        continue

    elif not any(char in "!@#$%&*" for char in is_entered):
        print("You have to use special characters (!, @, #,$,%,&,*) in your password!")
        continue

    elif not any(c in full_alphabet for c in is_entered):
        print("Your password must include letters!")
        continue

    elif not any(n in "0123456789" for n in is_entered):
        print("Your password must include at least one number!")
        continue

    elif not any(i != i.upper() for i in is_entered) or any(i != i.lower() for i in is_entered) :
        print("Your password must include both uppercase and lowercase letters!")
        continue

    else:
        print("Your password has been created succesfully")
        break

    
"""
Created By: Aytuğ Yürük

"""
    
    

    