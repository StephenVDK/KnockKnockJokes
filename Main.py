userString = ''
knockCounter = 0
jokeBook = [[], []]
while userString != 'exit':
    userString = input("Whatsup I'm JokeBot! ")
    if userString == 'JokeBot tell me a joke':
        if len(jokeBook[0]) == 0:
            userString = input('I don’t know any jokes yet, can you tell me a Knock knock joke?')
            jokeBook[knockCounter].append(userString + ' ')
            userString = input('Who’s there?')
            jokeBook[knockCounter].append(userString + ' ')
            userString = input(userString + ' who?')
            jokeBook[knockCounter].append(userString + ' ')
            print('lmao you so funny')
            knockCounter = knockCounter + 1
        else:
            userString = input(jokeBook[0][0])
            userString = input(jokeBook[0][1])
            userString = input(jokeBook[0][2])

    elif userString == 'knock knock':
        jokeBook[knockCounter].append(userString + ' ')
        userString = input('Who’s there?')
        jokeBook[knockCounter].append(userString + ' ')
        userString = input(userString + ' who?')
        jokeBook[knockCounter].append(userString + ' ')
        print('lmao you so funny')
        knockCounter = knockCounter + 1
