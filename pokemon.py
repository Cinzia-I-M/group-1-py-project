import random
import requests


def pokemon_chooser():
    poke_id = random.randint(1, 152)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(poke_id)
    response = requests.get(url)
    pokemon = response.json()
    pokemon_info = {"Name": pokemon["name"], "ID": poke_id, "Height": pokemon["height"], "Weight": pokemon["weight"]}
    return pokemon_info


def dictionary_print(info):
    for key, value in info.items():
        print(f"{key}: {value}")


game_round = 0
user = 0
comp = 0

pokemon_user = pokemon_chooser()
user_name = input("What is your name? ")
print(f"Hi {user_name}! Let's battle!")

while game_round < 3:
    pokemon_comp = pokemon_chooser()
    print(f"Your Pokemon is: ")
    dictionary_print(pokemon_user)
    print(f"Your opponent's Pokemon is: {pokemon_comp['Name']}")
    chosen_stat = input("Which stat do you want to choose? (1.ID, 2.Height, 3.Weight) ")
    if chosen_stat == "1" or chosen_stat.casefold() == "id":
        game_round += 1
        print("---------------")
        print(f"You have chosen: 'ID'")
        print(f"Your Pokemon's ID is: {pokemon_user['ID']}")
        print(f"The ID of your opponent's Pokemon, '{pokemon_comp['Name']}', is: {pokemon_comp['ID']}")
        if pokemon_user['ID'] > pokemon_comp['ID']:
            user += 1
            print(f"{pokemon_comp['Name']} fainted!")
            print("You win!")
            print("---------------")
        elif pokemon_user['ID'] < pokemon_comp['ID']:
            comp += 1
            print(f"{pokemon_user['Name']} fainted!")
            print("You lose!")
            print("---------------")
            pokemon_user = pokemon_chooser()
        else:
            print("It's a draw!")
            print("---------------")
    elif chosen_stat == "2" or chosen_stat.casefold() == "height":
        game_round += 1
        print("---------------")
        print(f"You have chosen: 'Height'")
        print(f"Your Pokemon's height is: {pokemon_user['Height']}")
        print(f"The height of your opponent's Pokemon, '{pokemon_comp['Name']}', is: {pokemon_comp['Height']}")
        if pokemon_user['Height'] > pokemon_comp['Height']:
            user += 1
            print(f"{pokemon_comp['Name']} fainted!")
            print("You win!")
            print("---------------")
        elif pokemon_user['Height'] < pokemon_comp['Height']:
            comp += 1
            print(f"{pokemon_user['Name']} fainted!")
            print("You lose!")
            print("---------------")
            pokemon_user = pokemon_chooser()
        else:
            print("It's a draw!")
            print("---------------")
    elif chosen_stat == "3" or chosen_stat.casefold() == "weight":
        game_round += 1
        print("---------------")
        print(f"You have chosen: 'Weight'")
        print(f"Your Pokemon's weight is: {pokemon_user['Weight']}")
        print(f"The weight of your opponent's Pokemon, '{pokemon_comp['Name']}', is: {pokemon_comp['Weight']}")
        if pokemon_user['Weight'] > pokemon_comp['Weight']:
            user += 1
            print(f"{pokemon_comp['Name']} fainted!")
            print("You win!")
            print("---------------")
        elif pokemon_user['Weight'] < pokemon_comp['Weight']:
            comp += 1
            print(f"{pokemon_user['Name']} fainted!")
            print("You lose!")
            print("---------------")
            pokemon_user = pokemon_chooser()
        else:
            print("It's a draw!")
            print("---------------")
    else:
        print("Please choose from the options listed.")
        print("---------------")

if user > comp:
    print(f"You win! Congratulations, {user_name}!")
    print(f"Your score: {user}")
    print(f"Computer's score: {comp}")
elif user < comp:
    print(f"You lose. Better luck next time, {user_name}!")
    print(f"Your score: {user}")
    print(f"Computer's score: {comp}")