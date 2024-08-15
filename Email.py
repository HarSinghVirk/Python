# Project helps to determine if correct Email is entered or not
email = input("Enter Your Email : ") #a@g.com
k,j,d = 0,0,0
if len(email)>=6: #1
    if email[0].isalpha(): #2
        if("@"in email) and (email.count("@") == 1): #3
            if (email [-4] == ".") ^ (email[-3] == "."): #4
                for i in email:
                    if i == i.isspace(): #5
                        k = 1
                    elif i.isalpha():   
                        if i == i.upper(): # w-- W==W #5
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i =="@":
                        continue
                    else: #5
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    print(" wrong Email 5")        
            else:
                print(" wrong Email 4 ") 
        else:
            print(" wrong Email 3 ")
    else:
        print(" wrong Email 2 ")  
else:
    print(" wrong Email 1 ")                  