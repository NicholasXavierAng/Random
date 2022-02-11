# Author: Ang Shao Xuan Nicholas
# Takes a guess and its corresponding result before returning a list of possible remaining words.

words = []
with open("wordle-answers-alphabetical.txt", "r") as f:
    for word in f:
        words.append(word.strip())
possible_words = []

while 1:
    while 1:
        guess = input("What is your guess: ")
        guess = guess.lower()
        print()
        
        if len(guess) != 5 or guess.isalpha() == False:
            print("Invalid guess.\nPlease ensure that the guess consists of 5 letters.")
            print("Press Ctrl + C to terminate program.\n")
            continue
        if guess not in words:
            print("Invalid word.\n")
            continue
        else:
            break

    # Enter result in format:
    #   = -> Correct letter in correct spot
    #   + -> Correct letter in wrong spot
    #   - -> Wrong letter

    print("Enter result in format:")
    print("\t= -> Correct letter in correct spot")
    print("\t+ -> Correct letter in wrong spot")
    print("\t- -> Wrong letter\n")

    correct_input = "=+-"
    while 1:
        result = input("What is the result: ")
        print()
        if len(result) != 5 or all(c in correct_input for c in result) == False:
            print("Invalid result\nPlease ensure that the result consists of 5 characters made up of only '=', '+' and '-'.")
            print("Press Ctrl + C to terminate program.\n")
            continue
        else:
            break

    for word in words:
        is_pos_word = True
        for i in range(len(word)):
            if result[i] == "=" and word[i] != guess[i]:
                is_pos_word = False
                break
            elif result[i] == "+" and (guess[i] not in word or guess[i] == word[i]):
                is_pos_word = False
                break
            elif result[i] == "-" and guess[i] in word:
                is_pos_word = False
                break
        if is_pos_word == True:
            possible_words.append(word)

    words = possible_words
    print(possible_words, "\n")
    possible_words = []
    print("Press Ctrl + C to terminate program.\n")
    if len(possible_words) == 1:
        break
