from tkinter import *
import random

root = Tk()
root.geometry('1200x900')
root.config(bg="Black")
Heading = Label(root, text="ROCK PAPER SCISSOR", bd=5, width=40, relief=RAISED, padx=10, pady=10, font="Revamped 30")
Heading.grid(row=0, column=0)

# Starting
label = Label(root, text="Would you like to start the game", font=("Helvetica 35"))
label.grid(row=1, column=0)

# MENU BARS
my_menu = Menu(root)
root.config(menu=my_menu)
# Options in menu
Inst = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=Inst)

# these are defined as an empty label so we can destroy it in any function
r = Label(root)
r1 = Label(root)
r2 = Label(root)
e = Label(root)
x = Label(root)
Start = Label(root)


# back to game function
# used when instruction are open and we want to go back to our main window
def btg1():
    global x
    global Start
    l1.destroy()
    btg.destroy()
    x = Label(root, text="Would you like to start the game", font=("Helvetica 35"))
    x.grid(row=1, column=0)
    Start = Button(root, text="START", fg="blue", bg="black", font=("Times 24"), width=12, command=start)
    Start.grid(row=3, column=0)


# INSTRUCTIONS OF THE GAME
def inst():
    global l1
    global btg
    r.destroy()
    r1.destroy()
    r2.destroy()
    e.destroy()
    label.destroy()
    S.destroy()
    l1 = Label(root, text="1. A very simple game which you can play with the computer"
                          "\n" "2. Enter your Name and three choices will be provided choice any of them....."
                          "\n" "3. Computer will also choose its choice and according to the choice every time winner will be choosen,score will be counted "
                          "\n" "4. After 9 turns the game will end and we will see who got a better luck in winning games "
                          "\n" "5. At, last score will be shown on the screen with the Winner Name", bg="White",
               font=("Times 15"))

    l1.grid()
    btg = Button(root, text="Back to game", command=btg1)
    btg.grid()


# Options drop down box
Inst.add_command(label="Instructions", command=inst)
Inst.add_separator()
Inst.add_command(label="QUIT", command=root.quit)


# when any selections is made by the user
# this function is called when clicked on the start button
def start():
    global r
    global r1
    global r2
    global var
    global e
    label.destroy()  # destroys the label
    S.destroy()  # destroys the button
    x.destroy()
    Start.destroy()

    var = StringVar()  # stores the value of Radio button
    var.set("gupps")
    # Formation of Radio buttons
    r = Radiobutton(root, text="ROCK", value="ROCK", variable=var, font="Lucida 24", bg="black", fg="orange",
                    command=select)
    r.grid(row=1, column=0)
    r1 = Radiobutton(root, text="PAPER", value="PAPER", variable=var, font="Lucida 24", bg="black", fg="orange",
                     command=select)
    r1.grid(row=2, column=0)
    r2 = Radiobutton(root, text="SCISSOR", value="SCISSOR", variable=var, font="Lucida 24", bg="black", fg="orange",
                     command=select)
    r2.grid(row=3, column=0)

    # Entry section
    e = Entry(root, borderwidth=3, width=45, bg="gray")
    e.insert(0, "ENTER THE NAME OF THE PLAYER")
    e.grid()


# variables for increasing the score
comp = 0
user = 0
i = 0  # this variable keeps the check of how much time game will run


def select():
    # providing them global scope
    global comp
    global user
    global i
    list = ['ROCK', 'PAPER', 'SCISSOR']
    # chooses random value from the list and assigns it to x variable
    x = random.choice(list)
    print(x)

    # conditions that checks what is score and who will win
    if x == "SCISSOR" and var.get() == "ROCK":
        user = user + 1
        Label(root, text=e.get() + " " + "WINS" + "SCORE IS" + " " + str(user), relief=RAISED, font="SHOWCARD  20",
              fg="yellow", bg="black").grid()
        i = i + 1
    elif x == "ROCK" and var.get() == "PAPER":
        user = user + 1
        Label(root, text=e.get() + " " + "WINS" + " " + "SCORE IS" + " " + str(user), relief=RAISED,
              font="SHOWCARD  20", fg="yellow", bg="black").grid()
        i = i + 1
    elif x == "PAPER" and var.get() == "SCISSOR":
        user = user + 1
        Label(root, text=e.get() + " " + "WINS" + " " + "SCORE IS" + " " + str(user), relief=RAISED, font="SHOWCARD 20",
              fg="yellow", bg="black").grid()
        i = i + 1
    elif x == "SCISSOR" and var.get() == "PAPER":
        comp = comp + 1
        Label(root, text="COMP WINS" + " " + "SCORE IS" + " " + str(comp), relief=SUNKEN, font="SHOWCARD  20",
              fg="white", bg="black").grid()
        i = i + 1
    elif x == "ROCK" and var.get() == "SCISSOR":
        comp = comp + 1
        Label(root, text="COMP WINS" + " " + "SCORE IS" + " " + str(comp), relief=SUNKEN, font="SHOWCARD 20",
              fg="white", bg="black").grid()
        i = i + 1
    elif x == "PAPER" and var.get() == "ROCK":
        comp = comp + 1
        Label(root, text="COMP WINS" + " " + "SCORE IS" + " " + str(comp), relief=SUNKEN, font="SHOWCARD  20",
              fg="white", bg="black").grid()
        i = i + 1
    elif x == "PAPER" and var.get() == "PAPER":
        Label(root, text="TIE", font="SHOWCARD 20", relief=GROOVE, fg="RED", bg="black").grid()
        i = i + 1
    elif x == "ROCK" and var.get() == "ROCK":
        Label(root, text="TIE", font="SHOWCARD  20", relief=GROOVE, fg="RED", bg="black").grid()
        i = i + 1
    elif x == "SCISSORS" and var.get() == "SCISSORS":
        Label(root, text="TIE", font="SHOWCARD  20", relief=GROOVE, fg="RED", bg="black").grid()
        i = i + 1
    # stopping condition
    if i == 9:
        Label(root, text="COMP SCORE" + "  " + str(comp), fg="White", bg="black").grid()
        Label(root, text=e.get() + " " + "SCORE" + "  " + str(user), fg="white", bg="black").grid()
        # this prints the results on the screen
        if comp > user:
            Label(root, text="COMPUTER WINS, AS" + " " + e.get() + " " + "IS NOOB", fg="RED", bg="black").grid()
        elif user < comp:
            Label(root, text=e.get() + "WINS,AS COMPUTER IS NOOB", fg="RED", bg="black").grid()
        elif comp == user:
            Label(root, text="SCORE TIED").grid()
        # GAME OVER
        Label(root, text="GAME OVER", fg="Dark Red", font="Broadway 40").grid()
        # these conditions disables all the radio buttons after the game is over
        r = Radiobutton(root, text="ROCK", value="ROCK", variable=var, state=DISABLED, font="Lucida 24", command=select)
        r.grid(row=1, column=0)
        r1 = Radiobutton(root, text="PAPER", value="PAPER", variable=var, state=DISABLED, font="Lucida 24",
                         command=select)
        r1.grid(row=2, column=0)
        r2 = Radiobutton(root, text="SCISSOR", value="SCISSOR", variable=var, state=DISABLED, font="Lucida 24",
                         command=select)
        r2.grid(row=3, column=0)
        # Quit button for quitting the game after game is finished
        quit = Button(root, text="QUIT", command=root.quit, font=("Times 12"))
        quit.grid()


# Start button
S = Button(root, text="START", fg="blue", bg="black", font=("Times 24"), width=12, command=start)
S.grid(row=3, column=0)

root.mainloop()
