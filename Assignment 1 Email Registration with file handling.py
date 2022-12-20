#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def email_reg():
    user_name = input("To register, Please enter the username or Email ID:")
    for i in range(0,len(user_name)):
        if (user_name[i].isdigit() or (user_name[i]=='@' and user_name[i+1]=='.') or(user_name[i]=='!'or user_name[i]=='#'or user_name[i]=='&'or user_name[i]=='%')):
            print("invalid, Please enter valid username or Email ID")
            email_reg()
    pass_word = input("Please enter the password:")
    digit=0
    spl_char=0
    u_case=0
    l_case=0
    for i in range(0,len(pass_word)):
        if (pass_word[i].isdigit()):
            digit+=1
        if (pass_word[i]=='!' or pass_word[i]=='@' or pass_word[i]=='#' or pass_word[i]=='&'):
            spl_char+=1
        if (pass_word[i].isupper()):
            u_case+=1
        if (pass_word[i].islower()):
            l_case+=1                      
    if((len(pass_word)>5 and len(pass_word)<16) and digit>=1 and spl_char>=1 and u_case>=1 and l_case>=1):
        print("Registration is successful")
        file = open("Credentials.txt","a")
        credentials = user_name+','+pass_word
        file.write(credentials)
        file.write('\n')
        file.close()
    else:
        print("invalid passwork, please register again")
        email_reg()
con=0        
a = int(input("Welcome. \nPlease enter 1 to Register, 2 to login:"))

if a==1:
    email_reg()
    
if a==2:
    b = input("Please enter 1 to login and 2 to exit() ")
    username = input("Please enter the username or Email ID:") 
    password = input("Please enter the password:")
    
    file = open("Credentials.txt","r")
    
    for i in file:
        A,B = i.split(",")
        B = B.strip()
        if(username==A and password==B):
            print("login successfull")
            con=1
            exit()
        if(username==A and password!=B):
            print("password is mismatching.")
            c = int(input("enter 1 to retrive your password,2 to register"))
            if c== 1:
                print("your password:",B)
                con=1
                break
            if c==2:
                email_reg()
    if(con==0):
        print("credential not found, please register")  


# In[ ]:




