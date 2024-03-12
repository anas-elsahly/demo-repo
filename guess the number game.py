# This is guess the number game
def guess_the_number_game():

  # Welcome players
  print('Hi, welcome to guess the number game')

  # Ask players for name
  name = input('Please enter your name: ')

  # check name validity
  while True:
    if name.strip() and not name.replace(" ", "").isdigit():
      break
    else:
      name = input('invalid name, pease try again: ')
  print('Well, ' + name.strip() + ', I am thinking of a number between 1 and 20.')
  print('You have only six chances to guess it')

  # Choosing secret number
  import random
  secret_number = random.randint(1,20)

  # Ask them to take a guess (with only six chances)
  for guesses in range(1,7):
    if guesses > 1:
      print('Chances left: ' + str(7 - guesses))
    else:
      pass
    try:
      player_guess = int(input('Take a guess: '))
      if player_guess > secret_number:
        print('ur guess is higher')
      elif player_guess < secret_number:
        print('ur guess is lower')
      else:
        break
    except ValueError:
      print('please enter a numeric value')

  if player_guess == secret_number:
    print('CONGRATS')
  else:
    print('wrong, the number was ' + str(secret_number))
