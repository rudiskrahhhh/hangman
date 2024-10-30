import random

def display_hangman(tries):
    stages = [  # KA IZSKATISIES PATS DZEKS
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

# VARDI/IESPEJAS

def get_word():
    words = ['zvaigzne', 'pilots', 'formula', 'matematika', 'basketbols', 'televizors', 'skolotajs']
    return random.choice(words).lower()

# SPELES PROGRAMMA 

def play_hangman():
    word = get_word()
    word_completion = "_" * len(word)  
    guessed = False
    guessed_letters = []  
    guessed_words = []  
    tries = 6  
    
    print("spelejam :D")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("ludzu mini burtu vai vardu: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"tu jau esi minejis {guess}.")
            elif guess not in word:
                print(f"{guess} nav varda")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"apsveicu! {guess} ir varda")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)  
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"tu jau esi minejis {guess}.")
            elif guess != word:
                print(f"{guess} nav pareizi")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("ta nu gan nevar")
        
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    if guessed:
        print(f"apsveicu! uzmineji vardu '{word}'!")
    else:
        print(f"diemzel tev neizdevas... vards bija '{word}'. lai veicas nakamreiz!")

if __name__ == "__main__":
    play_hangman()