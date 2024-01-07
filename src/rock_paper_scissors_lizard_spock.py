from enum import IntEnum
from collections import Counter

class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Rock: GameAction.Paper,
    GameAction.Paper: GameAction.Scissors,
    GameAction.Scissors: GameAction.Rock
}

def assess_game(user_action, computer_action):

    game_result = None

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        game_result = GameResult.Tie

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
            game_result = GameResult.Victory
        else:
            print("Paper covers rock. You lost!")
            game_result = GameResult.Defeat

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
            game_result = GameResult.Victory
        else:
            print("Scissors cuts paper. You lost!")
            game_result = GameResult.Defeat

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Scissors cuts paper. You won!")
            game_result = GameResult.Victory

    return game_result


def get_computer_action(user_actions_list):
    
    if len(user_actions_list) == 1:
        computer_action = GameAction(1)
    else:
        new_user_action = Counter(user_actions_list)
        preferencia = ['Rock', 'Paper', 'Scissors']
        max_value = max(new_user_action.values())
        empate = list(new_user_action.values()).count(max_value)

        if empate > 1:
            action_final = min(new_user_action, key=lambda x: preferencia.index(GameAction(x).name))
            computer_action = Victories[action_final]
        else:
            action_final = max(new_user_action, key=lambda x: new_user_action[x])
            computer_action = Victories[action_final]
            print(f"Computer picked {computer_action.name}.")
            
    return computer_action


def get_user_action():
    
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action

def main():
    user_actions_list = []
    print("Indicates the number of games: ")
    n_games = int(input())
    temp_n_games = n_games
    wins = 0

    while n_games > 0:
        try:
            user_action = get_user_action()
            user_actions_list.append(user_action)
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action(user_actions_list)
        
        if assess_game(user_action, computer_action) == GameResult.Victory:
            wins +=1

        n_games -=1

        print(f"You won {wins} games out of {temp_n_games} games")

if __name__ == "__main__":
    main()