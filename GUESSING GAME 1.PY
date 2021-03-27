i=1
guess=5
print("what is your name")
my_name=input("enter the name")
print("Hello",my_name,"I am thinking of a number between 1 to 10")
print("This game chance is five times")
while i<=guess:
    number=int(input("enter the guess number"))
    i=i+1
    if number==guess:
        print("guessing is correct")
        print("congratulations,your guessing is absoultly correct")
        break
    else:
        print("guessing is wrong")