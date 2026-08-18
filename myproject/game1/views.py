from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import random


def game(request):
    if request.method == "POST":
        guess = int(request.POST["guess"])
        number = request.session["number"]

        if guess == number:
            message = "Correct! 🎉"
        elif guess < number:
            message = "Too low! Try again."
        else:
            message = "Too high! Try again."

        return render(request, "game1/game.html", {
            "message": message
        })

    number = random.randint(1, 10)
    request.session["number"] = number

    return render(request, "game1/game.html")
