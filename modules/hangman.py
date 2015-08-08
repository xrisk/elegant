import random, thread
from time import sleep

_in = ''
buf = []
#variable name sweg
the_end = False

def main(s, priv=False):
  global buf
 
  if 'start' in s:
    global the_end
    the_end = True
    sleep(2)
    the_end = False
    n = thread.start_new_thread(game, tuple()) 
    print n
  else:
    global _in
    _in = s
    
    
  while len(buf) == 0:
    pass
  print buf, _in
  cp = buf[:]
  buf = []
  return '\n'.join(cp)
  
  
def raw_input():
  global _in 
  _in = '$$$'
  #scary magic :6
  while _in == '$$$':
    if the_end == True:
      import sys
      sys.exit(0)
    pass
  return _in

def brint(s):
  global buf
  buf.append(s)
  
  
  
def game():
  HANGMANPICS = ['''

  +---+
  |   |
  |
  |
  |
  |
  =====''', '''

  +---+
  |   |
  |   O
  |
  |
  |
  =====''', '''

  +---+
  |   |
  |   O
  |   |
  |
  |
  =====''', '''

  +---+
  |   |
  |   O
  |  /|
  |
  |
  =====''', '''

  +---+
  |   |
  |   O
  |  /|\\
  |
  |
  =====''', '''

  +---+
  |   |
  |   O
  |  /|\\
  |  /
  |
  =====''', '''

  +---+
  |   |
  |   O
  |  /|\\
  |  / \\
  |
  =====''']
  words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

  def getRandomWord(wordList):
     # This function returns a random string from the passed list of strings.
     wordIndex = random.randint(0, len(wordList) - 1)
     return wordList[wordIndex]

  def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
     brint(HANGMANPICS[len(missedLetters)])
     brint('')
    
     if len(missedLetters) == 0:
        brint('Missed letters: None')
     else:
        brint('Missed letters:' + ' '.join(missedLetters))

     blanks = '_' * len(secretWord)

     for i in range(len(secretWord)): # replace blanks with correctly guessed letters
         if secretWord[i] in correctLetters:
             blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

     brint(' '.join(blanks))

  def getGuess(alreadyGuessed):
     while True:
         brint('Guess a letter.')
         guess = raw_input()
         guess = guess.lower()
         if len(guess) != 1:
             brint('Please enter a single letter.')
         elif guess in alreadyGuessed:
             brint('You have already guessed that letter. Choose again.')
         elif guess not in 'abcdefghijklmnopqrstuvwxyz':
             brint('Please enter a LETTER.')
         else:
             return guess


  brint('H A N G M A N')
  missedLetters = ''
  correctLetters = ''
  secretWord = getRandomWord(words)
  gameIsDone = False

  while not gameIsDone:
     displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)


     print secretWord,'ALIBABA AND THE FORTY CHORS'
     guess = getGuess(missedLetters + correctLetters)
     if guess in secretWord:
         correctLetters = correctLetters + guess


         foundAllLetters = True
         for i in range(len(secretWord)):
             if secretWord[i] not in correctLetters:
                 foundAllLetters = False
                 break
         if foundAllLetters:
             brint('Yes! The secret word is "' + secretWord + '"! You have won!')
             gameIsDone = True
     else:
         missedLetters = missedLetters + guess


         if len(missedLetters) == len(HANGMANPICS) - 1:
             displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
             brint('You have run out of guesses! After ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
             gameIsDone = True
