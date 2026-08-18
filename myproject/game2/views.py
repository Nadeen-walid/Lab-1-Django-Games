from django.shortcuts import render
import random


def game(request):
    choices = ["rock", "paper", "scissors"]

    if request.method == "POST":
        player_choice = request.POST["choice"]
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            result = "It's a tie! 🤝"

        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or
            (player_choice == "paper" and computer_choice == "rock")
            or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            result = "You win! 🎉"

        else:
            result = "Computer wins! 🤖"

        return render(request, "game2/game.html", {
            "player_choice": player_choice,
            "computer_choice": computer_choice,
            "result": result
        })

    return render(request, "game2/game.html")