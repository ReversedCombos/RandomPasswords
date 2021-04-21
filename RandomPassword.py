import random

#Global Variables
alphabet = 'abcdefghijklmnopqrstuvwxyz'
characters = '!@#$%^&*()_+'
numbers = '0123456789'
#Add password will be a carrier to final passwords
add_password = ""

def random_password(num_characters):
    #This will be the return value
    global add_password
    #Create one random password
    for i in range(num_characters):
        #Generate a number of 3
        rand_num = random.randint(0, 2)
        #For letters if 0
        if rand_num == 0:
            #Makes a boolean value with int
            rand_num_casing = random.randint(0, 1)
            #Uses boolean value to choose between Lower and Capitalized letters
            if rand_num_casing == 0:
                #Adds letters with it starting at 0 Lowercased
                add_password += alphabet[random.randint(0, 25)]
            else:
                #Adds letter with it at starting at 0 Capitalized
                add_password += alphabet[random.randint(0, 25)].capitalize()
        #For characters if 1
        elif rand_num == 1:
            add_password += characters[random.randint(0, 11)]
        #For numbers if 2
        else:
            add_password += numbers[random.randint(0,9)]
    return(add_password)

def multiple_random_passwords(num_passwords, num_characters):
    #This will be the return value
    final_passwords = []
    #Loop for how many passwords are needed
    for i in range(num_passwords):
        #The final password is added onto from the random_password Function(A whole new password)
        final_passwords.append(random_password(num_characters))
    #Returns the final value
    return(final_passwords)