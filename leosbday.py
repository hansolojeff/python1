from sys import exit

def leo_bday():
    print("We are going to find out Leo's age today")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        his_age = int(choice)
    else:
        dead("Man, you are not even close.")

    if his_age == 9:
        print("Nice, Leo is 9 today and you win!")
        exit(0)
    else:
        dead("Nope!")


def leo_room1():
    print("Leo was born on a certain month of the year")                    
    print("This day was very special to me")
    print("It was the 8th day of what month")
    print("Do you know the month?")
    right_month = False 

    while True:
        choice = input("> ")

        if choice == "january":
            dead("The door locks you out and slams in your face off.")
        elif choice == "august" and not right_month:
            print("The door opens and you move on")
            print("You can wish him a happy birthday")
            bear_moved = True 
        elif choice == "december" and right_month:
            dead("The bear gets pissed off amd chews your leg off.")
        elif choice == "april" and right_month:
            leo_bday()
        else:
            print("I have no ieda what that means.") 
def leo_room2():
    print("You have no idea what the day or month is .")
    print("Leo, stares at you and waits for an answer.") 
    print("Do you quess for your life or know the age  type quess or knowleft?.")

    choice = input ("> ")

    if "know" in choice:
        start()

    elif "quess" in choice: 
        dead("You wish!")
    else:
       leo_room2() 

def dead(why):
        print("there's no time for that!") 
        exit(0)  

def start():
        print("Leo's birthday is today.")             
        print("There is a door to Leo's room to your right and left.")
        print("Which one do you take?.")

        choice = input( "> " )

        if choice == "left":
            leo_room1()
        elif choice == "right":
            leo_room2()
        else:
            dead("You will never know the answer")

start()    