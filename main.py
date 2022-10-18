# UTF-8 CRLF
# Done in REPL.IT & Python 3.8.4 32-bit interpreter
# Reproduction without citation is exclusively NOT permitted
# Licensed under GNU GPLv3.0

# Copyright (c) 2022 Tyler Peppy @ OCDSB

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import time
import random
import os
from cryptograph import *
from datetime import datetime
from cryptography.fernet import Fernet
import hashlib  # Check For Cheating To Hash Scores File

# ANSI Color Codes To Insert As STR Into Text

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

# Variables Used As Global

# String Variables
name = ''
yesNoPrompt = ''

# Integer Variables
currentBetSum = 2000  # Change This Value For Larger Or Smaller Bank
die1 = 0
die2 = 0
sum1 = 0
pointScore = 0
runCount = 0
betVal = 0
winsCounter = 0
lossesCounter = 0

# Secure Keys For Score Encryption
md5 = ""
global key
key = 0


# Readback And Open Key Into ENV For ENC And DEC
global fKey
temp = readKey()
fKey = temp
fKey = Fernet(temp)

# Get Terminal Size
columns, lines = os.get_terminal_size()
size = os.get_terminal_size()

def restoreLastScore():
  global currentBetSum
  try:
    yesNoPrompt = str(
      input("\n\u001b[33mRestore Last Score? (y/n): \u001b[0m"))
  except ValueError:
    print("\n\u001b[31mEnter 'Y' Or 'N'!\u001b[0m")  # Trap Errata Input
  else:
    if (yesNoPrompt == ""):
      print("\n\u001b[31mEnter 'Y' Or 'N'!\u001b[0m")  # Check For Enter Key
      
    elif (yesNoPrompt in "yY"):  # Check For Y
      with open('TEMP.scores', 'r') as f:
        print(GREEN + "\nUsing Last Bank" + RESET)
        last_line = f.readlines()[-1]
        decrypted = fKey.decrypt(last_line)
        decrypted = int.from_bytes(decrypted, 'big')
        currentBetSum = int(decrypted)
        f.close()
        

    elif (yesNoPrompt in "nN"):  # Check For N
      print(GREEN + "\nUsing Default Bank" + RESET)
    else:
      print("\n\u001b[31mEnter 'Y' Or 'N'!\u001b[0m")


def checkHash(fileName):
  print(YELLOW + "Checking Score File MD5..." + RESET)
  md5 = hashlib.md5(open(fileName, 'rb').read()).hexdigest()
  print(md5)

def printWallet():  # Function To Print Wallet Sum With Color
  global currentBetSum  # Declare Variables As Global
  global betVal
  print(GREEN + "\nCurrent Wallet Amount ($):", currentBetSum, "" + RESET)


def bet():  # Function To Get User Bet + Error Checking
  global currentBetSum  # Declare Variables As Global (DNT Remove, Vars Won't Hold Vals)
  global betVal

  while True:
    try:  # Try To Gain User Input
      print(GREEN + "\nCurrent Bank ($): ", currentBetSum)
      betVal = int(input("\u001b[33mEnter Bet Amount ($): \u001b[0m" + RESET))
    except ValueError:  # Don't Exit Loop On Invalid Input
      print("\n\u001b[31mEnter A Number!\u001b[0m")
    if (betVal < 0):
      print(
        RED +
        "\nEmpty / Negative Bets? What Do I Look Like? A Bank? I'm Not Paying You!"
        + RESET)
    elif (betVal > currentBetSum):
      print(RED + "\nYou Can't Bet More Than You Have!" + RESET)
    elif (betVal == 0):
      print(RED + "\nNo Bet?" + RESET)
    else:  # Continue And Break Loop After Accecpted Input
      print(
        YELLOW + "\nSum of " + GREEN + "$", betVal, "" + YELLOW +
        "will be subtracted on a LOSS, or will be added to current wallet of" +
        GREEN + " $", currentBetSum, "" + RESET)
      break
  return None  # Finish Function By Returning NULL Charecter


def endGame():
  print("\nThanks For Playing", name, "!")


def rollDice(range1, range2):
  global die1
  global die2
  die1 = random.randint(1, range1)
  die2 = random.randint(1, range2)
  return None


def continueGame():  # Function To Shoot Dice And Get User Input Over And Over
  global runCount  # Global Variables
  global lastScore
  global pointScore
  global sum1
  global currentBetSum
  global betVal
  global winsCounter
  global lossesCounter
  global die1
  global die2

  print(CYAN + "\nShooter, Shooting 2 Dice..." + RESET)
  rollDice(6, 6)  # Roll 2 dice with 2x ranges 1-6
  sum1 = die1 + die2
  print(LIGHT_BLUE + "\nDice #1:", die1)
  print("Dice #2:", die2)
  print(MAGENTA + "Rolled Score:", sum1, "" + RESET)
  pointScore = sum1

  if sum1 in (7, 11):  # Check For 7 Or 11 In Initial Sum For Win!

    print(GREEN + "\nCongratulations", name,
          ", you won immediately becuase you scored: ", sum1, "" + RESET)
    winsCounter = winsCounter + 1
    currentBetSum = currentBetSum + betVal
    printWallet()

  elif sum1 in (2, 3, 12):  # Check For 2, 3 Or 12 For Crapping Score

    print(RED + "Sorry", name, ", you 'crapped' becuase you scored: ", sum1,
          "" + RESET)
    lossesCounter = lossesCounter + 1
    currentBetSum = currentBetSum - betVal
    printWallet()

  else:

    print(YELLOW +"\nYou have rolled anything other than a 2, 3, 7, 11, or 12, therefore you must roll over and over, to get your last score!")
    printWallet()
    while True:
      input(GREEN + "\nPress Enter To Roll Again...")
      os.system('clear')
      print(CYAN + "\nOnto The Next One!" + RESET)
      print(CYAN + "\nRolling 2 Dice..." + RESET)
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      print(LIGHT_BLUE + "\nDice #1:", die1)
      print(LIGHT_BLUE + "Dice #2:", die2)
      print("Required Score:", pointScore)
      sum1 = die1 + die2
      print(MAGENTA + "Rolled Score:", sum1, "" + RESET)

      if (sum1 == 7):
        print(RED + "\nYou Lose! (Scored 7)" + RESET)
        lossesCounter = lossesCounter + 1
        currentBetSum = currentBetSum - betVal
        printWallet()
        break
      elif (sum1 == pointScore):
        print(GREEN + "\nYou Win!" + RESET)
        winsCounter = winsCounter + 1
        currentBetSum = currentBetSum + betVal
        printWallet()
        break
      else:
        print(RED + "\nYou haven't gained a winning or crapping score!" +
              RESET)
        printWallet()


def intro(windowWidth):

  print("    ____                ".center(windowWidth))
  print("   /\O O\    _____      ".center(windowWidth))
  print("  /O \___\  / O  /\     ".center(windowWidth))
  print("  \O / O / /____/OO\    ".center(windowWidth))
  print("   \/___/  \O  O\  /    ".center(windowWidth))
  print("            \O__O\/     ".center(windowWidth))
  print("")
  print(" -= A Craps Game =-     ".center(windowWidth))
  print("-= By: Tyler Peppy =-   ".center(windowWidth))
  time.sleep(2)  # Use Blocking Call To Delay Logic
  os.system('clear')


def storeScore():  # Function To Store History Data In Variables
  global winsCounter
  global lossesCounter

  lines = "Attempt On:", datetime.today().strftime(
    '%Y-%m-%d %H:%M:%S'
  ), ", Resulted in", winsCounter, "Wins +", lossesCounter, "Losses"
  lines = str(lines)
  with open('History.scores','a') as file:  # Open History.scores in append mode, write to last line
    file.write(lines + "\n")
    file.close()
  with open('TEMP.scores','a') as file:  # Open History.scores in append mode, write to last line
    data = fKey.encrypt(currentBetSum.to_bytes(2, byteorder='big'))
    data = data.decode('UTF-8')
    file.write(str(data)+"\n")
    file.close()
    


intro(size.columns)  # Auto-Center Intro To Window Size
random.seed(random.random())  # Generate Less Psuedo-Random Number Generation
checkHash("TEMP.scores")

while True:
  while True:
    try:
      name = str(input(BLUE + "Hi Player, What's Your Name?: " + RESET))
    except ValueError:
      print("You Have Not Entered A Valid Name!")
    else:
      if (name == ""):
        print("You Haven't Entered A Valid Name!")
      else:
        break

  while True:
    try:
      yesNoPrompt = str(
        input(
          "\n\u001b[33mWant to play a new game [Enter n to save score!]? (y/n): \u001b[0m"
        ))
    except ValueError:
      print("\n\u001b[31mEnter 'Y' Or 'N'!\u001b[0m")  # Trap Errata Input
    else:
      if (yesNoPrompt == ""):
        print("\n\u001b[31mEnter 'Y' Or 'N'!\u001b[0m")  # Check For Enter Key
      elif (yesNoPrompt in "yY"):  # Check For Y
        print(BLUE + "\nHi " + name + ", ready to play some craps?" + RESET)
        print(BLUE + "\nHistorical Data:" + RESET)
        print(MAGENTA + "Current Wins:", winsCounter)
        print("Current Losses:", lossesCounter)
        try:
          print("W/L Ratio:", winsCounter / lossesCounter, "" + RESET)
        except ZeroDivisionError:
          print("W/L Ratio: No Data")
        restoreLastScore()
        bet()
        continueGame()
      elif (yesNoPrompt in "nN"):  # Check For N
        print(GREEN + "Thanks For Using This Program!" + RESET)
        storeScore()
        break
      else:
        print("\n\u001b[31mEnter 'Y' Or 'N'!\u001b[0m")
  break