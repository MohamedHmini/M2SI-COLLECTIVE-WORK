''' this file hold functions that checks for the right input '''

def checkInput(message,mi,ma):
    value = int(input(message))
    while value >= ma or value < mi:
        value = int(input('Error!!'+message))
    return value

