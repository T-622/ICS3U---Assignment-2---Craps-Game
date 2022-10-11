import math
import time
import random
import os

# Colors

MAGENTA = "\u001b[35m"
BLACK = "\033[0;30m"
YELLOW = "\u001b[33m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
RESET = "\u001b[0m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"

name = ''
yesNoPrompt = ''
currentBetSum = 2000
die1 = 0
die2 = 0
sum1 = 0
pointScore = 0
runCount = 0
betVal = 0
winsCounter = 0
lossesCounter = 0

def printWallet():
  global currentBetSum
  global betVal
  print(GREEN+"\nCurrent Wallet Amount ($):",currentBetSum,""+RESET)

def bet():
  global currentBetSum
  global betVal
  
  while True: #TODO - Check For Negatives Or Larger Than Current Wallet
    try:                                                     
      betVal = int(input(GREEN+"\n\u001b[33mEnter Bet Amount ($): \u001b[0m"+RESET))
    except ValueError:
      print("\n\u001b[31mEnter A Number!\u001b[0m")
    else:
      print(YELLOW+"\nSum of "+GREEN+"$",betVal,""+YELLOW+"will be subtracted on a LOSS, or will be added to current wallet of"+GREEN+" $",currentBetSum,""+RESET)
      break
  return None

def endGame():
  print("\nThanks For Playing",name,"!")

def continueGame():
  global runCount
  global lastScore
  global pointScore
  global sum1 
  global currentBetSum
  global betVal
  global winsCounter
  global lossesCounter

  runCount = runCount + 1
  print(CYAN+"\nShooter, Shooting 2 Dice..."+RESET)
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  sum1 = die1+die2
  print(LIGHT_BLUE+"\nDice #1:",die1)
  print("Dice #2:",die2)
  print(MAGENTA+"Rolled Score:",sum1,""+RESET)
  pointScore = sum1
  
  if sum1 in (7,11):   
    print(GREEN+"\nCongratulations",name,", you won immediately becuase you scored: ",sum1,""+RESET)
    winsCounter = winsCounter + 1
    currentBetSum = currentBetSum + betVal
    printWallet()
    
  elif sum1 in (2,3,12):
    print(RED+"Sorry",name,", you 'crapped' becuase you scored: ",sum1,""+RESET)  
    lossesCounter = lossesCounter + 1
    currentBetSum = currentBetSum - betVal
    printWallet()
  else: 
    print(YELLOW+"\nYou have rolled anything other than a 2, 3, 7, 11, or 12, therefore you must roll over and over, to get your last score!")
    printWallet()
    
    while True:
      input(GREEN+"\nPress Enter To Roll Again...")
      print(CYAN+"\nRolling 2 Dice..."+RESET)
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      print(LIGHT_BLUE+"\nDice #1:", die1)
      print(LIGHT_BLUE+"Dice #2:", die2)
      print("Required Score:",pointScore)
      sum1 = die1 + die2
      print(MAGENTA+"Rolled Score:",sum1,""+RESET)
      
      if (sum1 == 7):
        print(RED+"\nYou Lose!"+RESET)
        lossesCounter = lossesCounter + 1
        currentBetSum = currentBetSum - betVal
        printWallet()
        break
      elif (sum1 == pointScore):
        print(GREEN+"\nYou Win!"+RESET)
        winsCounter = winsCounter + 1
        currentBetSum = currentBetSum + betVal
        printWallet()
        break
      else:
        print(RED+"\nYou haven't gained a winning or crapping score!"+RESET)
        printWallet()
def intro():
  print("  /\' .\    _____    ")
  print(" /: \___\  / .  /\   ")
  print(" \' / . / /____/..\  ")
  print("  \/___/  \'  '\  /  ")
  print("           \'__'\/   ")
  print("    A Craps Game     ")
  print("   By: Tyler Peppy   ")
  time.sleep(2)  # Use Blocking Call To Delay Logic
  os.system('clear')
  

intro()
while True:
  
  while True:
    try:
      name = str(input("Hi Player, What's Your Name?: "))
    except ValueError:
      print("You Have Not Entered A Valid Name!")
    else:
      if (name == ""):
        print("You Haven't Entered A Valid Name!")
      else:
        break
    
  
  while True:
    try:
      yesNoPrompt = str(input("\n\u001b[33mWant to play a new game? (y/n): \u001b[0m"))
    except ValueError:
      print("\n\u001b[31mEnter 'Y' Or 'N'!\u001b[0m")
    else:
      if (yesNoPrompt == ""):                                       
        print("\n\u001b[31mEnter 'Y' Or 'N'!\u001b[0m")
      elif (yesNoPrompt in "yY"):   
        print("Hi",name,"ready to play some craps?")
        print(MAGENTA+"\nCurrent Wins:",winsCounter)
        print("Current Losses:",lossesCounter)
        try:
          print("W/L Ratio:",winsCounter / lossesCounter,""+RESET)
        except ZeroDivisionError:
         print("W/L Ratio: No Data")
        bet()
        continueGame()
      elif(yesNoPrompt in "nN"):                                    
        print("Thanks For Using This Program!")
        break
      else:
        print("\n\u001b[31mEnter 'Y' Or 'N'!\u001b[0m")