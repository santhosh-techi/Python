name = input('Enter the name: ').lower()
character_list = list(name)
name_list = ['_' for _ in name]

print(name_list)  # Printing the '_' to ensure length

print('Start of the game\n')

# Storing the number of choices
counter = len(name)
print(f'You have {counter} lives now, try to guess in the provided lives')
i=0

while counter != 0:
    letter = input('Enter a character: ').lower()

    if not letter.isalpha() or len(letter) != 1:
        print(f'Invalid input. You have {counter} lives left.')
        continue

    if letter in character_list:
        # Update the name_list with the correct guessed letters
        name_list[i] = letter
        print(name_list)
        i=i+1
        letter_index=character_list.index(letter)
        del character_list[letter_index]
        
        if '_' not in name_list:
            print(f'Congratulations! You guessed the name correctly. The name was: {name}')
            break
    else:
        counter -= 1
        print(f'Wrong guess. You have {counter} lives left, and the guess is {name_list}')
        if counter == 0:
            print(f'No lives left. The name was: {name}. Your final guess was: {name_list}')
