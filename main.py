# imports
# imports random module
import random

# this function checks to see if the input is a number


def get_min_max():
    """
     get_min_max, choose a min/max range for the game
    """
    user_min_num = choose_a_number("Please provide a low number: ")
    user_max_num = choose_a_number("Please Provide a high number: ")
    if user_max_num <= user_min_num:
        print("Invalid choice, max value is less than min.  Try again")
        return get_min_max()

    return user_min_num, user_max_num


def choose_a_number(msg):
    """
    Keep trying till a valid number is entered
    """
    while True:
        user = input(msg)
        try:
            result =  int(user)
            return result
        except:
            print("Invalid selection.  Please enter a numeric value")

def is_num_less(user, value):
    """
    this function checks to see if the second number is lower then the first number
    """
    while user <= value:
        return choose_a_number("Choose a higher number: ")


def play_again():
    """
    checks to see if the user wants to restart the game or quit
    """
    choice = input(
        "Do you want to play again? (y/n)?: "
    ).lower()
    return choice[0:1]


def main():

  ans = 'y'
  while ans == 'y':
      # gets the user inputs
      user_min_num, user_max_num = get_min_max()
      # generates a random number
      random_number = random.randint(user_min_num, user_max_num)
      # the user guesses the random number that was generated
      guess = choose_a_number("Guess the number that was generated: ")
      # checks to see if the guessed number matches the random number that was generated
      while guess != random_number:
          # if the number is to high then it will inform the user
          if guess < random_number:
              guess = choose_a_number("That choice is too low: ")
          # if the number is to low then it will inform the user
          else:
              guess = choose_a_number("That was choice was too high: ")
      # announces that the user has won the number guessing game
      print(f"Congratulations your choice of {guess} was correct!")
      # restarts the game
      ans = play_again()


if __name__ == '__main__':
        main()
