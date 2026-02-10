
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "AEIOUaeiou":
            if letter. isupper():
            translation = translation + "g"
        else:
            translation = translation + "G"
    return translation


print(translate(input("enter a phrase")))
    
