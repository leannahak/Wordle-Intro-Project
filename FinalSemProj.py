#I hereby certify that this program is solely the result of my own work and is
#in compliance with Academic Integrity policy of the course syllabus. 
import Draw
import random

#In the canvas function we are writing out the heading Wordle and setting the
#font to a fixed width font and making all leters bolded
def canvas():
   Draw.setFontFamily('Courier New') 
   Draw.setFontSize(50)
   Draw.setFontBold(True)
   Draw.string("Wordle",185,20)
   
#we are opeining and inserting a wordlist that contains 5,000 five letter words
#we are making this list of words into an actual list 
def getWordList():
   fin=open("fivewordlist.txt")
   #creating an empty list to add the words into
   wordList=[] 
   #here we are reading through each line of the txt file
   for line in fin: 
      #we are stripping the words to get rid of the \n
      wordList+=[line.strip()] 
      #common etiquette to close the file after usage
   fin.close() 
   return wordList  

#in getGuess we are verifying that the user has finsihed typing the whole guess
#and that the guess is an actual word. 
def  getGuess(wordList,tryNum): 
   alphabet="abcdefghijklmnopqrstuvwxyz"
   guess=""
   while len(guess)<5 or guess not in wordList:
      #Once the user clicks a key on the keyboard
      if Draw.hasNextKeyTyped():
         #get the key 
         newKey=Draw.nextKeyTyped()
         #if the user hits the backspace button then the guess is what has been typed so far
         #up until but not including the last letter 
         if newKey=="BackSpace" and len(guess)>0: 
            guess=guess[:-1]
            redrawGuess(guess,tryNum) 
         #as long as the key is a letter in the alphabet then we concatante it to
         # the guess string. we then invoke redrawGuess which will put the guess
         #on the actual canvas screen
         if newKey in alphabet and len(guess)<5:
            guess+=newKey
            redrawGuess(guess,tryNum)
   return guess

#This is where we take the guess string and actually display it on the string
#ytop is where each of the boxes of the guess rows will be located
#for each letter of the guess string we are drawing a small black square and then
#drawing the letter inside that box
def redrawGuess(guess,tryNum): 
   #how tall we
   ytop=tryNum*75  
   x =100 
   Draw.setColor(Draw.WHITE)
   Draw.filledRect(70,ytop+70, 450,40) 
   #for each letter draw a box and the actual letter
   for i in range(len(guess)): 
      Draw.setColor(Draw.BLACK)
      Draw.rect(x*i+70,ytop+70,40,40)
      Draw.setColor(Draw.BLACK)
      Draw.setFontSize(30)
      Draw.string(guess[i],x*i+80,ytop+70) 
   Draw.show()
   
 #in letterFind  we take the guessCharacter and goal word. For each positon of 
 #the goal word, if the guessChar is the same letter we want this position
 #if it is not the same that return a -1
def letterFind(guessChar,goal):
   for i in range(len(goal)):
      if guessChar==goal[i]:
         return i
   return -1

#In colorGuess here we are seeing if the letter is in the correct or wrong postion
#or if the letter is in the goal word at all
def colorGuess(goal,guess,tryNum): 
   x=100
   #starting off with no greens/anything guessed
   numGreens=0 
   #make the goal word into a list so we can loop through it
   goal=list(goal) 
   ytop=tryNum*75 
   #cover the squares and letters with a white box so
   #we can redraw them in the corresponding colors
   #make box the color of the background color
   Draw.setColor(Draw.WHITE) 
   Draw.filledRect(70,ytop+70, 450,40) 
   #for each position in the guess string,if the letter is the same redraw it in green
   for i in range(len(guess)):
      if guess[i]==goal[i]:
         Draw.setColor(Draw.GREEN)
         Draw.string(guess[i],x*i+80,ytop+70) 
         # we set it to None to remember that character has been used up 
         goal[i]=None 
         #we add one to numGreens because we must keep track of how many
         #we got right         
         numGreens+=1 
         #if it is not the same as the goal letter in the same postion 
         #invoke letter find and if we find that letter at all in the goal
         #then initialize foundPos to that position      
      else: 
         foundPos=letterFind(guess[i],goal)
         #meaning the letter is in the gaol word but at a diifferent postion
         if not(foundPos==-1): 
            Draw.setColor(Draw.ORANGE)
            goal[foundPos]=None
         #if letterFind returns a -1 it means that letter is not in the goal word
         #so we should redraw it in a gray color
         else: 
            Draw.setColor(Draw.GRAY)
         Draw.string(guess[i],x*i+80,ytop+70) 
   Draw.show()
   #return the number of greens here because if it equals 5 that means 
   #that the user won the game
   return numGreens 

#here we are drawing the instructions to explain the game and instruct how 
#to start playing the game
def instructions(): 
   Draw.clear() #start by clearing the canvas
   Draw.setFontSize(40)
   Draw.setFontBold(True)
   Draw.setColor(Draw.BLUE)
   Draw.string("How To Play:",170,10) 
   Draw.setFontSize(20)
   Draw.setColor(Draw.RED)
   Draw.string("You have 6 tries to guess the correct 5-Letter word",60,100) 
   Draw.setFontSize(20)
   Draw.setColor(Draw.BLACK)
   Draw.string("Gray letter= not in word",60,140) 
   Draw.string("Orange letter=in word but in different position",60,180) 
   Draw.string("Green letter= in word and in correct position",60,220)
   Draw.setFontSize(32)
   Draw.string("Enjoy the game!",170,260) 
   Draw.setColor(Draw.BLACK)
   Draw.string("Click anywhere to begin",115,450) 
   #if the user clicks the mouse then we will clar the canvas if the 
   #instructions and start to invoke the functions for the game 
   while True:
      if Draw.mousePressed()==True:
         Draw.clear()
         return  
             
def playGame(): 
   #initialize tryNum to zero because they have not tried to guess yet
   tryNum=0
   #set the canvas size
   Draw.setCanvasSize(600,650) 
   instructions()
   canvas() 
   wordList=getWordList()
   goal=random.choice(wordList)
   #the user only gets 6 tries
   for tryNum in range(6):
      guess=getGuess(wordList,tryNum)
      numGreens=colorGuess(goal,guess,tryNum)
      #if the number of greens is equal to 5 that means the user won, so display
      #a winning message 
      if numGreens==5:
         Draw.setFontSize(85)
         Draw.setFontBold(True)
         Draw.setColor(Draw.PINK)
         Draw.string("YOU WIN!",100,250)   
         Draw.show()
   #otherwise once we fall out of the loop of the 6 tries display a losing message
   if numGreens!=5:
      Draw.setFontSize(85)
      Draw.setFontBold(True)
      Draw.setColor(Draw.BLUE)
      Draw.string("YOU LOSE!",60,250) 
      Draw.show()
playGame()