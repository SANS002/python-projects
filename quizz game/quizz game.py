print("WELCOME TO QUIZZ!")

playing = input("do you want play this game ..?")

print(playing)

x=0

if playing.lower() !="yes":
    quit()

print("OK! Let's play :")
answer = input("What does CPU stand for ?")
if answer.lower() =="central processing unit":
    print("correct!")
    x=x+1
else:
    print("Incorrect!")

answer = input("What does GPU stand for ?")
if answer.lower() =="graphics processing unit":
    print("correct!")
    x=x+1
else:
    print("Incorrect!")  

answer = input( "What does RAM stand for ?")
if answer.lower() =="random access memory":
    print("correct!")
    x=x+1
else:
    print("Incorrect!")

answer = input("What does ROM stand for ?")
if answer.lower() =="read only memory":
    print("correct!")
    x=x+1
else:
    print("Icorrect!")

answer = input("Is python is programming language ?")
if answer.lower() =="yes":
    print("correct!")
    x=x+1
else:
    print("Incorrect!")

print("your points out of 5 is :",x)
