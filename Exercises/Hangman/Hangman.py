import random
from words import words

def get_valid_word(words):
    word = random.choice(words) #randomly chooses an element from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word

def hangman():
    word = get_valid_word(words)
    guessed_letters = set()
    tries = 10
    
    while tries > 0:
        print("\n")
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        
        if set(word) == guessed_letters:
            print("\nCongratulations! You guessed the word correctly!")
            break
        
        guess = input("\nGuess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            tries -= 1
            print("Wrong guess!")
            print(f"Tries left: {tries}")
        
    if tries == 0:
        print("\nYou ran out of tries! The word was:", word)

if __name__ == "__main__":
    hangman()