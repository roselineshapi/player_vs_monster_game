from random import randint

game_running = True
game_results = [] #empty list
def calculate_monster_attack(attack_min, attack_max):# function that generate a random number for the monster to attack with
    return randint(attack_min, attack_max)

def game_ends(winner_name): #function prints the name of the winner
    print(f"{ winner_name} won the game")

while game_running == True: #loop that makes the game continue to run until the player decides to quit
    counter = 0
    new_round = True
    player={"name":"Roseline","attack": 13 ,"heal": 16, "health":100}
    monster={"name":"Dragon","attack_min": 10 ,"attack_max":20,"health":100}

    print("___"*7)
    print("Enter player name")
    player["name"] = input()

    print(player["name"] + " has "+ str(player["health"]) + " health")
    print(monster["name"] + " has "+ str(monster["health"]) + " health")

    while new_round == True: #loop for new round

        counter = counter + 1
        player_won = False
        monster_won = False

        #selection menu
        print("Please select action")
        print("1) Attack")
        print("2) Heal")
        print("3) Exit")
        print("4) Show Results")

        player_choice = input()

        if player_choice == "1":
            monster["health"] = monster["health"] - player["attack"]
            if monster["health"] <=0:
                player_won = True

            else:

                player["health"] = player["health"] - calculate_monster_attack(monster["attack_min"], monster["attack_max"])
                if player["health"] <= 0:
                    monster_won = True

        elif player_choice == "2":
            player["health"]= player["health"] + player["heal"]

            player["health"] = player["health"] - calculate_monster_attack()
            if player["health"] <= 0:
                monster_won = True

            print("Heal player")

        elif player_choice =="3":
            game_running = False
            new_round = False

        elif player_choice == "4":
            for item in game_results:
                print(item)


        else:
            print("Invalid Input")

        if player_won == False and monster_won == False:
            print(player["name"] + " has "+ str(player["health"]) + " left")
            print(monster["name"] + " has "+ str(monster["health"]) + " left")

        elif player_won:
            game_ends(player["name"])
            round_result = {"name": player["name"], "health": player["health"], "rounds":counter}
            game_results.append(round_result)
            new_round = False

        elif monster_won:
            game_ends(monster["name"])
            round_result = {"name": player["name"], "health": player["health"], "rounds":counter}
            game_results.append(round_result)

            new_round = False
