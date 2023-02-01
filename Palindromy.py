word = "potok"

def palindrom_check(word):
    
    """
    function checks if the word is equal to it's reverse

    """
    return word == word[::-1]
        
palindrom = palindrom_check(word)


if palindrom:
    print("yes")
else:
    print("No")

palindrom_check(word)