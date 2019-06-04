def search4vowels(phrase:str) -> set:
    """ Display any vowels found in a supplied word """
    vowels = set('aeiou')
    #word = input('Enter a word to search for vowels:')
    found = vowels.intersection(set(phrase))
    #for vowel in found:
        #print(vowel)

    return (found)


def search4letters(phrase:str, letters:str) -> set:
    """Display the letters we are interested in found in supplied string """
    return set(letters).intersection(set(phrase))


result = search4vowels('Guardians of the galaxy')
print(result)

result = search4letters('How have you been lately', 'wvaeiouty')
print(result)