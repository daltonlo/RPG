# Period: 1
# Date created: 9/17/21
# Date last modified: 9/22/2021
# Name: Dalton Low
# Description: Rpg Menu


# Tells the player where they can go
def movements(x, y):
    """Created a list of directions the player can go"""
    move = ["Forward", "Backward", "Left", "Right"]
    """Prints directions player can go"""
    print("You Can Go " + move[x] + " Or " + move[y])


# Creates a function to tell what the player can do
def act():
    """Creates a list of actions the player can take"""
    act = ["Run", "Hide", "Search", "Quit"]
    for act in act:
        """Prints actions the player can take"""
        print("You Can " + act)
    a = input("")
    """Determines if the player chose to run"""
    if a == "Run":
        print("You run to the next room")
        return
    """Determines if player chose to hide"""
    if a == "Hide":
        print("You hide")
        return
    """Determines if the player chose to search"""
    if a == "Search":
        print("You search and find a layout of the rooms")
        print("Four rooms in a square")
        print("Each with two doors that go to the rooms directly adjacent")
        return
    """Creates a quit function"""
    if a == "Quit":
        print("Thank you for playing")
        quit()
        """Creates invalid input prompt"""
    elif act.count(a) == 0:
        print("Please enter a valid input next time")
        return

# Prints my name and description
print("RPG menu by Dalton Low")

# Determines what room you are in
room = 1

# Loops function
while True:
    """If statement to tell which room you are in"""
    if room == 1:
        """Determines which rooms you can go to"""
        movements(0, 3)
        """Asks for the direction the player wants to go"""
        direction = input("")
        """Determines what to do if the player went forward"""
        if direction == "Forward":
            """Changes room that player is in"""
            room = 2
            """Prints actions the player can take"""
            act()
        elif direction == "Right":
            room = 4
            """Calls act function"""
            act()
            """Creates Invalid input prompt"""
        else:
            print("please enter a valid input")
        """Elif statement for if player is in room 2"""
    if room == 2:
        movements(1, 3)
        """Asks for the direction the player wants to go"""
        direction = input("")
        """Determines what to do if the player went backward"""
        if direction == "Backward":
            """Changes room that player is in"""
            room = 1
            """Prints actions the player can take"""
            act()
        if direction == "Right":
            """Changes room that player is in"""
            room = 3
            """Prints actions the player can take"""
            act()
            """Creates Invalid input prompt"""
        else:
            print("please enter a valid input")
    """Elif statement for if player is in room 3"""
    if room == 3:
        movements(1, 2)
        """Asks for the direction the player wants to go"""
        direction = input("")
        """Determines what to do if the player went backward"""
        if direction == "Backward":
            """Changes room that player is in"""
            room = 4
            """Prints actions the player can take"""
            act()
            """Determines what to do if the player went left"""
        if direction == "Left":
            """Changes room player is in"""
            room = 2
            """Prints actions the player can take"""
            act()
            """Creates Invalid input prompt"""
        else:
            print("please enter a valid input")
    """Elif statement for if player is in room 4"""
    if room == 4:
        movements(0, 2)
        """Asks for the direction the player wants to go"""
        direction = input("")
        """Determines what to do if the player went forward"""
        if direction == "Forward":
            """Changes room that player is in"""
            room = 3
            """Prints actions the player can take"""
            act()
        """Determines what to do if the player went left"""
        if direction == "Left":
            """Changes room player is in"""
            room = 1
            """Prints actions the player can take"""
            act()
            """Creates invalid input prompt"""
        else:
            print("please enter a valid input")
