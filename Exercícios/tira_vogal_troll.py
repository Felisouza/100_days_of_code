## Trolls are attacking your comment section!
## A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

## Your task is to write a function that takes a string and return a new string with all vowels removed.

## For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

def disemvowel(string):
    #string = string.lower()
    for i in string:
        if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
            string = string.replace(i, '')
    return print(string)


disemvowel('This website is for losers LOL!')