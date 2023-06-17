print("Hello There , Welcome To The Python Quiz!")
print("In This Quiz You'll Have 3 Questions")
print("They'll Be Used To Check If You're Worthy To Join The Python Dev Team!")
print("So Let's Begin")
Q1 = input("What Is A Variable?: ")
if Q1 == "A Value Container In Python":
    print("Wow You Have Passed The Beginner Question!")
elif Q1 == "a value container in python":
    print("Wow You Have Passed The Beginner Question!")
else:
    print("You Have Lost On The First Question Bye!")
    quit()

Q2 = input("What Is The Github Co-Pilot?: ")
if Q2 == "A Python Dev Helping Tool":
    print("Good Job You Have Passed The Intermediate Question!") 
elif Q2 == "a python dev helping tool":
    print("Good Job You Have Passed The Intermediate Question!")
else:
    print("Well Wrong Answer Buddy You Gotta Go!")
    quit()

Q3 = input("What Is Tkinter?: ")
if Q3 == "The GUI Tool For Python":
    print("Great Job! You Have Passed Welcome To The Python Dev Team!")
    quit()
elif Q3 == "the gui tool for python":
    print("Great Job! You Have Passed Welcome To The Python Dev Team!")
    quit()
else:
    print("Sorry You Weren't Capable To Join!")
    quit()
