import random

def choose_word():
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
    return random.choice(wordslist).lower()

def display_word(word, letters_guessed):
    return ' '.join(letter if letter in letters_guessed else '*' for letter in word)

def hangman():
    word = choose_word()
    letters_guessed = set()
    wrong_guesses = 0
    max_attempts = 6
    body_parts = ['head', 'body', 'left arm', 'right arm', 'left leg', 'right leg']

    print("LET'S PLAY HANGMAN!!")
    print(display_word(word, letters_guessed))
    
    while wrong_guesses < max_attempts:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue
        
        if guess in letters_guessed:
            print("You already guessed that one.")
            continue
        
        letters_guessed.add(guess)
        
        if guess in word:
            print("Correct!")
        else:
            print(f"Incorrect! You lost a body part: {body_parts[wrong_guesses]}")
            wrong_guesses += 1
        
        print(display_word(word, letters_guessed))
        
        if '*' not in display_word(word, letters_guessed):
            print("Congratulations! You guessed the word!")
            return
    
    print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
