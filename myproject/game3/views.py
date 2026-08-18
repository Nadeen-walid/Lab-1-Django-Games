from django.shortcuts import render


def game(request):

    if request.method == "POST":

        board = request.POST.getlist("board")

        if len(board) != 9:
            board = [""] * 9

        position = int(request.POST["position"])
        player = request.POST["player"]

        if board[position] == "":
            board[position] = player

        winner = check_winner(board)

        if winner:
            message = f"Player {winner} wins! 🎉"
        elif "" not in board:
            message = "It's a draw! 🤝"
        else:
            message = "Keep playing!"

        next_player = "O" if player == "X" else "X"

        return render(request, "game3/game.html", {
            "board": board,
            "message": message,
            "next_player": next_player
        })

    board = [""] * 9

    return render(request, "game3/game.html", {
        "board": board,
        "next_player": "X"
    })


def check_winner(board):

    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for combination in winning_combinations:

        a, b, c = combination

        if board[a] and board[a] == board[b] == board[c]:
            return board[a]

    return None