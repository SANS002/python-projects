
def view():
    with open ('password.txt','r') as f:
        #read lines in the file
        for line in f.readlines():
            #rstrip used for remove the charecters in this line it's remove the white spaces from the right (\n creats the new line)
            data = line.rstrip()
            user,psword = data.split("|")#split the account name,pwd and it creat a list for accessing
            print("user_name:",user,"| password",psword)
   
def add():
    name = input ('Enter Your Account Name : ')
    pwd = input("Enter the the password : ")
    #with used for closing file automatically
    with open ('password.txt','a') as f:
        f.write(name+ '|'+pwd+"\n")


while True :
    mode = input("would you like to add a new password or view existing one (view,add) or Quit(q)? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else :
        print("invalid option !")
        continue
