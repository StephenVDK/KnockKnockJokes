userString = ''
joke = ''
knockCounter = 0
jokeBook = []
while userString != 'exit':
    userString = input("Whatsup I'm JokeBot! ")
    if userString == 'JokeBot Tell me a joke':
        userString = input('I don’t know any jokes yet, can you tell me a Knock knock joke?')
        joke = userString
        userString = input('Who is there?')
        joke = joke + ' ' + userString
        userString = input(userString + ' who?')
        joke = joke + ' ' + userString
        print('lmao you so funny')
        jokeBook.append(joke)
