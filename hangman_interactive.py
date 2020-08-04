#each fail gets a list of strings representing the hangman draw
fail1 = [("         "),("         "),("         "),("         "),("         "),("__________")]
fail2 = [("         "),("      |  "),("      |  "),("      |  "),("      |  "),("______|___")]
fail3 = [(" ______  "),("      |  "),("      |  "),("      |  "),("      |  "),("______|___")]
fail4 = [(" ______  "),("     \|  "),("      |  "),("      |  "),("      |  "),("______|___")]
fail5 = [(" ______  "),(" |   \|  "),("      |  "),("      |  "),("      |  "),("______|___")]
fail6 = [(" ______  "),(" |   \|  "),(" O    |  "),("      |  "),("      |  "),("______|___")]
fail7 = [(" ______  "),(" |   \|  "),(" O    |  "),(" |    |  "),("      |  "),("______|___")]
fail8 = [(" ______  "),(" |   \|  "),(" O    |  "),("/|\   |  "),(" '    |  "),("______|___")]
fail9 = [(" ______  "),(" |   \|  "),(" O    |  "),("/|\   |  "),("/'\   |  "),("______|___")]

fail_list = [fail1, fail2, fail3, fail4, fail5, fail6, fail7, fail8, fail9]

#variables needed
fails = 0
status = ""
m_word = ""
oneleft = 0

def draw():    #function to draw hangman based on number of fails
    for i in fail_list[fails]:
        print(i)
        
def win_lose():   #function to check for win or lose and end game accordingly
        global status
        if "." not in m_word:
            status = "win"
            raise SystemExit ("You Win!")
        elif status == "lose":
            print("The word was: {0}".format(word))
            raise SystemExit ("You Lose!")

def guess():   #function to get user guess and set according status
        global char
        char = input("Please enter a letter: ")
        global fails
        global status
        
        if len(char) > 1:
            status = "fail - 2 letters"            
            fails += 1
        elif char in m_word:
            status = "fail - already guessed" 
            fails += 1
        elif char not in word:
            status = "fail"
            fails += 1       
        else:
            if oneleft > 0:
                status = "win"
            else:
                status = "success"
        
        if fails == 8:
            status = "lose"
        elif fails == 7:
            status = "one guess left"    
                                   
def get_masked_word(): #function for the masked word
        global m_word
        global status
        global oneleft
        pos = -1
        if fails < 8:
            for i in word:
                pos += 1
                if i == char:
                    m_word = m_word[:pos] + char + m_word[pos+1:]      
            
        if m_word.count(".") == 1:
            oneleft += 1
            if oneleft == 1:
                status = "one letter left"

def comment():  #function to provide comment for user based on the guess 
    if status == "one guess left":
        print("Watch out - only one guess left!")
    elif status == "one letter left":
        print("Only one letter left!")        
    if status == "success":
        print("Nice!")
    elif status == "fail":
        print("Letter not in word - guess again!")
    elif status == "fail - 2 letters":
        print("Stop cheating - Only 1 letter at a time please!")
    elif status == "fail - already guessed":
        print("Sorry - you already guessed this letter")
    elif status == "win":
        print("N I C E ! You got it!")
    elif status == "lose":
        print("Oh noooooooooo!")  
  

#start game
word = input("Please enter a word to be guessed: ") 

input("Press enter to start the game!")

# draw space graphic
space = "."
for i in range(0,50):
    space = " " + space
    print(space)  

#draw masked word according to the entered word
for i in word:
    m_word = m_word + "."
    
while True:        
        draw()
        print("")
        print(m_word)
        win_lose() 
        guess()
        get_masked_word()
        comment()
