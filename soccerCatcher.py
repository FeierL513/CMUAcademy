    #Background
Rect(0, 0, 400, 400, fill = gradient('green', 'forestGreen', 'seaGreen', start = 'top-left'))
Rect(40, 40, 320, 320, fill = gradient('green', 'forestGreen', 'seaGreen', start = 'top-left'), border = 'white')
    
    #center
Circle(200, 200, 40, fill = gradient('green', 'forestGreen', 'seaGreen', start = 'left'), border = 'white')
Line(40, 200, 360, 200, fill = 'white')
    
    #top
Rect(120, 40, 160, 80, fill = gradient('green', 'forestGreen', 'seaGreen', start = 'top'), border = 'white')
Rect(160, 40, 80, 40, fill = gradient('green', 'forestGreen', 'seaGreen', start = 'top-right'), border = 'white')
    
    #bottom
Rect(120, 280, 160, 80, fill = gradient('green', 'forestGreen', 'seaGreen', start = 'bottom'), border = 'white')
Rect(160, 320, 80, 40, fill = gradient('green', 'forestGreen', 'seaGreen', start = 'top-left') , border = 'white')
    
    #ball
ball = Circle(200, 200, 20)
    
    #soundeffects
music = Sound('https://drive.google.com/file/d/1WFMiGHe0uPaHg-DVmzji2eyGof195KY0/view?usp=sharing')
    
    #cleat
shoe = Rect(143, 350, 100, 60, fill = gradient('black','white', start = 'top'))
    
        
    #ScoreCounter
ScoreCounter = Label (0, 360, 25, size = 35, bold = True)
ScoreHeader = Label (' score: ', 260, 25, size = 40, fill = 'white', border = 'black', bold = True)
    

    #overlay
overlay = Rect (0,0, 400, 400, fill = 'black', opacity = 0)
    
    
ball.speedY = 0
ball.speedX = 3
ball.rotateSpeed = 2
ball.movement = 5

    #start-button


startButton = Group(
    Rect(0, 0, 400, 400, fill = 'darkGreen'),
    Star(52, 40, 50, 5, fill = gradient('white', 'yellow', start = 'top-left'), rotateAngle = 15),
    Star(258, 258, 30, 5, fill= gradient('white', 'yellow', start = 'top-left'), rotateAngle = 30),
    Star(54, 370, 50, 5, fill = gradient('white', 'yellow', start = 'top-left'), rotateAngle = 20),
    Star(390, 340, 40, 5, fill = gradient('white', 'yellow', start = 'top-left'), rotateAngle = -15),
    Star(390, 45, 25, 5, fill = gradient('white', 'yellow', start = 'top-left'), rotateAngle = 20),
    Image('https://www.misskatecuttables.com/uploads/shopping_cart/9126/large_soccer-title.png', -10, -40, rotateAngle = -15),
    Oval(200, 330, 220, 80, border = 'white'),
    Label("START", 200, 330, fill='white', font='arial', size = 30, bold = True),
    )
    
stars = Group( Star(40, 40, 3, 4, fill = 'white'), 
                Star(360, 320, 3, 4, fill = 'white'), 
                Star(40, 360, 3, 4, fill = 'white'), 
                Star(120, 40, 3, 4, fill = 'white'),
                Star(58, 288, 3, 4, fill = 'white'),
                Star(113, 259, 3, 4, fill = 'white'),
                Star(23, 106, 3, 4, fill = 'white'),
                Star(194, 9, 3, 4, fill = 'white'),
                Star(337, 389, 3, 4, fill = 'white'),
                Star(350, 380, 3, 4, fill = 'white'),
            )
app.pause = True
    
def onMousePress(mouseX,mouseY):
    if (startButton.hits(mouseX,mouseY)):
        app.pause = False
        startButton.opacity = 0
    
def onMouseMove(mouseX,mouseY):
    if (app.pause == False):
        shoe.centerX = mouseX

def onStep():
    for star in stars:
      star.radius = randrange (5, 10)
      
     
    if (app.pause == False):
        #testing label
        
        ball.centerY += ball.speedY
        ball.centerX += ball.speedX
        ball.rotateAngle += ball.rotateSpeed
        
        #gravity
        ball.speedY += 1 
            # sound
        if (ball.bottom <= 300):
            music.play(loop=True)
             #bouncing
        if (ball.hitsShape(shoe)):
                
            ball.speedY = -20
            ScoreCounter.value += 1
        if (ScoreCounter.value >= 3):
            ball.movement = 7
        if (ScoreCounter.value >= 5):
            shoe.width = 75
            shoe.height = 45
            shoe.centerY = 380
            ball.movement = 10
            ball.rotateSpeed += 2
        if (ScoreCounter.value >= 10):
            ball.movement = 14
            ball.rotateSpeed += 2
        if (ScoreCounter.value >= 15):
            shoe.width = 55
            shoe.height = 35
            shoe.centerY = 395
            ball.movement = 19
            ball.rotateSpeed += 2
        if (ScoreCounter.value >= 20):
            ball.movement = 26
            ball.rotateSpeed += 2
        if (ScoreCounter.value >= 30):
            ball.movement = 36
            ball.rotateSpeed += 2
            
        if (ball.centerX >= 350):
            ball.speedX = -ball.movement
        if (ball.centerX <= 50):
            ball.speedX = ball.movement
            #game over
        if (ball.centerY >= 400):
            Label ('GAME OVER', 200, 130, size = 50, fill =gradient( 'red', 'black', start = 'top'), font = 'orbitron', border = 'red')
            overlay.opacity = 40
            Label ('Score: % s' % (ScoreCounter.value), 200, 180, size = 40, bold = True, font = 'orbitron', border = 'black', fill = gradient ('white', 'gray', start = 'bottom'))
            app.stop()
                
      
               
             
    
    
    
    #cleat image
    #Image('http://www.clker.com/cliparts/S/R/r/K/v/4/soccer-shoe-md.png', 90, 200)
    
