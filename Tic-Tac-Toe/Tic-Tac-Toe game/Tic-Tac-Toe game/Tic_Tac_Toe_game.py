from tkinter import *
import random

def nextTurn(row, col):
    global player

    if buttons[row][col]['text'] == "" and winner() is False:      #['text'] accesses the 'text' attribute of a button widget
        if player == symbols[0]:
            buttons[row][col]['text'] = player

            if winner() is False:
                player = symbols[1]
                #l1.config(text=(symbols[1]+"'s turn"))
                l1.config(text=f"Player with symbol {symbols[1]} 's turn")

            elif winner() is True:
                #l1.config(text=(symbols[0]+" wins"))
                l1.config(text=f"Player with symbol {symbols[0]} wins")
                
            elif winner() == "Tie":
                l1.config(text="It's a tie")

        else:
            buttons[row][col]['text'] = player

            if winner() is False:
                player = symbols[0]
                #l1.config(text=(symbols[0]+"'s turn"))
                l1.config(text=f"Player with symbol {symbols[0]} 's turn")

            elif winner() is True:
                #l1.config(text=(symbols[1]+" wins"))
                l1.config(text=f"Player with symbol {symbols[1]} wins")

            elif winner() == "Tie":
                l1.config(text="It's a tie")

def winner():

    #Horizontal win condition
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] !="":
            buttons[i][0].config(bg="red")
            buttons[i][1].config(bg="red")
            buttons[i][2].config(bg="red")
            return True

    #Vertical win condition
    for j in range(3):
        if buttons[0][j]['text'] == buttons[1][j]['text'] == buttons[2][j]['text'] !="":
            buttons[0][j].config(bg="green")
            buttons[1][j].config(bg="green")
            buttons[2][j].config(bg="green")
            return True
    
    #Diagonal win conditions
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] !="":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] !="":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif openSpace() is False:
        for r in range(3):
            for c in range(3):
                buttons[r][c].config(bg="grey")
        return "Tie"

    else:
        return False

def openSpace():
    spaces = 9
    
    for r in range(3):
        for c in range(3):
            if buttons[r][c]['text'] !="":
                spaces -=1

    if spaces == 0:
        return False
    else:
        return True

def newGame():

    global player
    player = random.choice(symbols)
    l1.config(text=player + "'s turn")

    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="", bg="#F0F0F0")


w = Tk()
w.title("Tick-Tac-Toe")
#w.geometry("500x500")
w.config(bg="#3882d1")
symbols = ["X","O"]
player = random.choice(symbols)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]
          ]
l1 = Label(text=f"Player with symbol {player} 's turn", font=("Arial",40), bg="#d9d025")
l1.pack(side="top", pady=20)

rb = Button(text="Restart", font=("Arial",20), bg="#d9d025", command=newGame)
rb.pack(side="top", pady=2)

game_frame = Frame(w)
game_frame.pack()

for r in range(3):
    for c in range(3):
        buttons[r][c] = Button(game_frame,
                               text = "",
                               font = ("Arial",40),
                               width = 5,
                               height = 2,
                               command = lambda row = r, col = c: nextTurn(row, col)
                               )
        buttons[r][c].grid(row=r, column=c)
                        
w.mainloop()