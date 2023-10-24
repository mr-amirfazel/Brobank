
resthe = " )(((((())))))( "

def match(reshte):
    stack = []
    counter = 0
    for char in reshte:
        if char == '(':
            counter +=1
        elif char == ')':
            counter -=1

    if counter == 0:
        print('matches')
    else:
        print('doesnt match')

