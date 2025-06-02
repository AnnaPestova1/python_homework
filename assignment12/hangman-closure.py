def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        # result_after_guesses = [word secret_word.replace(not_guessed_letter, '_') if letter not in secret_word else letter]
        result_after_guesses=""
        for char in secret_word:
            if char in guesses:
                result_after_guesses+=char
            else:
                result_after_guesses += "_"
        # return True if result_after_guesses == secret_word else False    
        # added interactivity with user   
        if result_after_guesses == secret_word:
            print(result_after_guesses)
            print(f"Congrats, the secret word is {secret_word}")
            return True
        else:
             print(result_after_guesses)
             print("Continue guessing")
             return False

    return hangman_closure


def play_game():
    game = make_hangman("python")
    game(input('make a guess '))
    while game(input('make a guess ')) != True:
        continue
play_game()