def convert_pig_latin(phrase):
    words = phrase.split(' ')
    pig_word = ''
    for word in words:
        pig_word += f'{word[1:]}{word[0]}ay '
    return pig_word
