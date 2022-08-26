app.background = 'skyBlue'

Label('Type to guess!', 200, 15, size=20, fill='black', bold=True)

Line(105,105, 105,145, fill='sienna')
Line(30,300, 30, 110, lineWidth = 12, fill='sienna')
Line(24,110, 110, 110, lineWidth = 12, fill='sienna')
Line(30,145, 75, 110, fill='sienna')
Line(24,110, 110, 110, lineWidth = 12, fill='sienna')


# first row
Rect(0, 280, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(40, 280, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(80, 280, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(120, 280, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(160, 280, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(200, 280, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(240, 280, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(280, 280, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(320, 280, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(360, 280, 40, 40 , fill = 'lightGrey', border = 'black')


# second row
Rect(0, 320, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(40, 320, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(80, 320, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(120, 320, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(160, 320, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(200, 320, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(240, 320, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(280, 320, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(320, 320, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(360, 320, 40, 40 , fill = 'lightGrey', border = 'black')


#third row

Rect(80, 360, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(120, 360, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(160, 360, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(200, 360, 40, 40 , fill = 'lightGrey', border = 'black')
Rect(240, 360, 40, 40 , fill = 'lightGrey', border = 'black')



# letters
Label('a', 18, 300, font= 'monospace', size=35)
Label('b', 58, 300, font= 'monospace', size=35)
Label('c', 98, 300, font= 'monospace', size=35)
Label('d', 138, 300, font= 'monospace', size=35)
Label('e', 178, 300, font= 'monospace', size=35)
Label('f', 218, 300, font= 'monospace', size=35)
Label('g', 258, 300, font= 'monospace', size=35)
Label('h', 298, 300, font= 'monospace', size=35)
Label('i', 338, 300, font= 'monospace', size=35)
Label('j', 378, 300, font= 'monospace', size=35)
Label('k', 18, 340, font= 'monospace', size=35)
Label('l', 58, 340, font= 'monospace', size=35)
Label('m', 98, 340, font= 'monospace', size=35)
Label('n', 138, 340, font= 'monospace', size=35)
Label('o', 178, 340, font= 'monospace', size=35)
Label('q', 218, 340, font= 'monospace', size=35)
Label('r', 258, 340, font= 'monospace', size=35)
Label('s', 298, 340, font= 'monospace', size=35)
Label('t', 338, 340, font= 'monospace', size=35)
Label('u', 378, 340, font= 'monospace', size=35)

Label('v', 98, 380, font= 'monospace', size=35)
Label('w', 138, 380, font= 'monospace', size=35)
Label('x', 178, 380, font= 'monospace', size=35)
Label('y', 218, 380, font= 'monospace', size=35)
Label('z', 258, 380, font= 'monospace', size=35)


#word bank
Words = ["birds", "shoes", "shirt", "stink", 'board', 'final', 'heads', 'roads', 'feast', 'group', 'paper', 'right', 'skies', 'level', 'phone']

Word = Words[randrange(0, 15)]

Letters = []

guessedLetters = ["_"]

firstLetter = Label("_", 100, 60, bold = True, size = 25)
secondLetter = Label("_", 150, 60, bold = True, size = 25)
thirdLetter = Label("_", 200, 60, bold = True, size = 25)
fourthLetter = Label("_", 250, 60, bold = True, size = 25)
fifthLetter = Label("_", 300, 60, bold = True, size = 25)


Head = Circle(105, 160, 15, fill='skyBlue', border='black', borderWidth=2.5)
Body = Line(105, 175, 105, 230, lineWidth=2.5)
RightArm = Line(105, 190, 87, 205, lineWidth=2.5)
LeftArm = Line(105, 190, 123, 205, lineWidth=2.5)
LeftLeg = Line(105, 229, 87, 255, lineWidth=2.5)
RightLeg = Line(105, 229, 123, 255, lineWidth=2.5)

Guy = Group (
   Head, Body, RightArm, LeftArm, LeftLeg, RightLeg
)

wrongGuesses = Label(0, 200, 200, opacity = 0)

guessedWord = ["", "", "", "", ""]

#see if user guessed the right word
for x in Word:
    Letters.append(x)

def onKeyPress(key):
    for x in guessedLetters:
        if (x == key):
            print("You already guessed this letter!")
            break
        else:
            if (Letters[0] == key):
                firstLetter.value = key
                guessedWord[0] = key
            if (Letters[1] == key):
                secondLetter.value = key
                guessedWord[1] = key
            if (Letters[2] == key):
                thirdLetter.value = key
                guessedWord[2] = key
            if (Letters[3] == key):
                fourthLetter.value = key
                guessedWord[3] = key
            if (Letters[4] == key):
                fifthLetter.value = key
                guessedWord[4] = key
                pass
            if (guessedWord == Letters):
                Rect(53, 80, 295, 175, fill = 'white', border = 'Black')
                Label('YOU GOT IT!', 200, 175, bold = True, size = 30, border = 'white')
                pass
            if key in Letters:
                pass
            else:
                # Incorrect Guess
                wrongGuesses.value += 1
                if (wrongGuesses.value == 6):
                    Guy.remove(Head)
                    #Guy.remove(Body)
                elif (wrongGuesses.value == 5):
                    Guy.remove(Body)
                elif (wrongGuesses.value == 4):
                    Guy.remove(RightArm)
                elif (wrongGuesses.value == 3):
                    Guy.remove(LeftArm)
                elif (wrongGuesses.value == 2):
                    Guy.remove(LeftLeg)
                elif (wrongGuesses.value == 1):
                    Guy.remove(RightLeg)
                    
                    
                else:
                    #Game Over
                    Rect(53, 80, 295, 175, fill = 'white', border = 'Black')
                    Label('GAME OVER', 200, 120, bold = True, size = 30, border = 'white')
                    Label('The answer was: ' + Word, 150, 160, size = 15, fill = 'red')
                    #Label(key , 250, 160, size = 15)
                    app.paused
                break
                
                
                
    guessedLetters.append(key)
    pass

def onStep():
    # print(guessedLetters)
    pass

Rect(180, 40, 40, 40, fill='white', border='black', opacity=40)
Rect(130, 40, 40, 40, fill='white', border='black', opacity=40)
Rect(230, 40, 40, 40, fill='white', border='black', opacity=40)
Rect(80, 40, 40, 40, fill='white', border='black', opacity=40)
Rect(280, 40, 40, 40, fill='white', border='black', opacity=40)
