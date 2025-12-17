import random

# Liste der 44 Länder Europas
europa_laender = [
    "Albanien", "Andorra", "Belarus", "Belgien", "Bosnien und Herzegowina",
    "Bulgarien", "Dänemark", "Deutschland", "Estland", "Finnland",
    "Frankreich", "Griechenland", "Irland", "Island", "Italien",
    "Kroatien", "Lettland", "Liechtenstein", "Litauen", "Luxemburg",
    "Malta", "Moldau", "Monaco", "Montenegro", "Niederlande",
    "Nordmazedonien", "Norwegen", "Österreich", "Polen", "Portugal",
    "Rumänien", "Russland", "San Marino", "Schweden", "Schweiz",
    "Serbien", "Slowakei", "Slowenien", "Spanien", "Tschechien",
    "Ukraine", "Ungarn", "Vatikanstadt", "Vereinigtes Königreich"
]

word_bank = europa_laender

word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 8

gibbet = '__________\n |/       \n |        \n |        \n |        \n |        \n |        \n_|___     '
phase1 = '__________\n |/    |  \n |        \n |        \n |        \n |        \n |        \n_|___     '
phase2 = '__________\n |/    |  \n |     O  \n |        \n |        \n |        \n |        \n_|___     '
phase3 = '__________\n |/    |  \n |     O  \n |     |  \n |        \n |        \n |        \n_|___     '
phase4 = '__________\n |/    |  \n |     O  \n |    \|  \n |        \n |        \n |        \n_|___     '
phase5 = '__________\n |/    |  \n |     O  \n |    \|/ \n |        \n |        \n |        \n_|___     '
phase6 = '__________\n |/    |  \n |     O  \n |    \|/ \n |     |  \n |        \n |        \n_|___     '
phase7 = '__________\n |/    |  \n |     O  \n |    \|/ \n |     |  \n |    /   \n |        \n_|___     '
phase8 = '__________\n |/    |  \n |     O  \n |    \|/ \n |     |  \n |    / \ \n |        \n_|___     '

phase = gibbet

# Welcome-Loop - asking the user if he want's to play. Closes the game if not.
print('Welcome to this little game of Hangman.')
print('You\'ve got 8 attempts to guess the correct word. Otherwise a stickfigure will go to the gallows.')
answer = input('Do you want to play? (Y/N) ').lower()

while answer != 'y':
  if answer == 'n':
    print('Bye bye!')
    quit()
  else:
    print('Invalid answer. Try again.')
    answer = input('Do you want to play? (Y/N) ').lower()

print('Let\'s start!')

# Game-Loop - randomly chooses a word from the word_bank and let's you guess
while attempts > 0:
  print('\nCurrent word: ' + ''.join(guessedWord) + '(' + str(len(word)) +')')

  guess = input('Guess a letter: ').lower()
  while guess == '':
    guess = input('Enter a letter: ').lower()

  if guess in word.lower():
    for i in range(len(word)):
      if word[i].lower() == guess:
        guessedWord[i] = guess
    print('Great guess!')
  else:
    attempts -= 1
    print('Wrong guess!')
    if attempts == 8:
      print(phase)
    elif attempts == 7:
      phase = phase1
      print(phase)
    elif attempts == 6:
      phase = phase2
      print(phase)
    elif attempts == 5:
      phase = phase3
      print(phase)
    elif attempts == 4:
      phase = phase4
      print(phase)
    elif attempts == 3:
      phase = phase5
      print(phase)
    elif attempts == 2:
      phase = phase6
      print(phase)
    elif attempts == 1:
      phase = phase7
      print(phase)
    elif attempts == 0:
      phase = phase8
      print(phase)
    print('Attempts left: ' + str(attempts))

  if '_' not in guessedWord:
      print('\nCongratulations!! You guessed the word: ' + word)
      break

if attempts == 0 and '_' in guessedWord:
  print('\nYou\'ve run out of attempts! The word was: ' + word)