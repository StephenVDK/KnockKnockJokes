from django.shortcuts import render

def jokebot(request):
	return render(request, 'userInterface.html',{})
	
def buttonPressed(userInput):
	return userInput
	
