import random
import requests
import math
import sys
import colorama
from colorama import init
init()

url = 'https://hp-api.onrender.com/api/characters'
response = requests.get(url)
character = response.json()

url = 'https://hp-api.onrender.com/api/spells'
response = requests.get(url)
spells = response.json()

user_team = []
spell_count = 0
comp_team = []
user_special_powers = []
comp_special_powers = []
user_health = 100
comp_health = 100

# This assigns spells to variables so below I can get them to affect the health in different amounts
five_damage = ['Accio','Alohomora', 'Avis', 'Evanesco', 'Impedimenta', 'Petrificus Totalus', 'Rictusempra', 'Wingardium Leviosa']
ten_damage = ['Ascendio', 'Confundo', 'Expelliarmus', 'Incendio', 'Locomotor Mortis', 'Tarantallegra']
fifteen_damage = ['Aparecium', 'Finite Incantatem', 'Levicorpus', 'Stupefy']
twenty_damage = ['Bombardo', 'Immobulus', 'Reducto']
twentyFive_damage = ['Conjunctivitis Curse', 'Fiendfyre Curse']
thirty_damage = ['Crucio', 'Imperio', 'Sectumsempra']
oneHundred_damage = ['Avada Kedavra']
five_healing = ['Episkey']
ten_healing = ['Apparate']
fifteen_healing = ['Ferula']
twenty_healing = ['Aguamenti', 'Reparifors']
twentyFive_healing = ['Protego', 'Renneverate']
thirty_healing = ['Anapneo', 'Brackium Emendo', 'Expecto patronum']

def welcome_message():
    print("\nWelcome to the Harry Potter Battle Game! Follow the instructions and beat your opponent to win. \nYou and the computer start with 100 health and the first one to get to 0 loses. \nFirst, you need to know the special powers of each house. \nGryffindor: +10% damage -5% healing. \nSlytherin: +8% damage -4% healing. \nRavenclaw: -5% damage +10% healing. \nHufflepuff: -4% damage +8% healing. \nGood luck! \n ")
    print("---------------")

def team_chooser():
    print("Type \033[1;4mteam\033[0m if you would like to pick your team, or \033[1;4mrandom\033[0m if you want a random one: ")
    team_choice = input().title()
    if team_choice == 'Team':
        your_characters()
    elif team_choice == 'Random':
        random_character()
        while len(user_team) < 3:
            random_character()
            if chosen_character['house'] != "":
                user_team.append(f"{chosen_character['name']}, {chosen_character['house']}")
    else:
        print("Please type only \033[1;4mteam\033[0m or \033[1;4mrandom\033[0m.")
        team_chooser()

def your_characters(): # This gets 3 characters for the user's team or picks a random team for them
    while len(user_team) < 3:
        print(f"Team member {len(user_team)+1}: choose a Harry Potter character: ")
        character_name = input().title()
        global chars
        chars = []
        for i in character:
            if character_name in i['name']:
                global charName
                global charHouse
                charName = i['name']
                charHouse = i['house']
                chars.append(i['name'])
        check_chars()

def check_chars(): # This checks them in the API as there are characters with similar names
    if len(chars) == 1 and charHouse != "":
        print(f"{charName}, {charHouse}")
        user_team.append(f"{charName}, {charHouse}")
    elif len(chars) > 1:
        print(chars)
        print("Please pick from the options given.")
        your_characters()
    else:
        print("Please check the spelling. Your character must be in a house.")
        your_characters()

def random_character(): # This gets a random character for the computer
    global chosen_character
    chosen_character = []
    character_number = random.randint(1, 102)
    chosen_character = character[character_number]

def random_team(): # This gets 3 characters and checks that they have a house
    while len(comp_team) < 3:
        random_character()
        if chosen_character['house'] != "":
            comp_team.append(f"{chosen_character['name']}, {chosen_character['house']}")
    print(f"The computer's team is: {' - '.join(comp_team)}.\n")
    print("---------------")

def special_powers(team): # This works out the additional/minus damage and healing for each team based on houses they're in
    Dam = 0
    Heal = 0
    for i in team:
        if 'Gryffindor' in i:
            Dam += 10
            Heal -= 5
        if 'Slytherin' in i:
            Dam += 8
            Heal -= 4
        if 'Ravenclaw' in i:
            Dam -= 5
            Heal += 10
        if 'Hufflepuff' in i:
            Dam -= 4
            Heal += 8
    if team == user_team:
        user_special_powers.append(Dam)
        user_special_powers.append(Heal)
        print(f"\033[1mYour special powers are:\033[0m {user_special_powers[0]}% damage and {user_special_powers[1]}% healing.")
    else:
        comp_special_powers.append(Dam)
        comp_special_powers.append(Heal)
        print(f"\033[1mThe computer's special powers are:\033[0m {comp_special_powers[0]}% damage and {comp_special_powers[1]}% healing.")

def random_damage_spell(): # Gets a random damage spell based on the id numbers I've selected
    global damage_num
    global spell_count
    damage_num = ''
    damage_spells = ['Accio','Alohomora', 'Avis', 'Evanesco', 'Impedimenta', 'Petrificus Totalus', 'Rictusempra', 'Wingardium Leviosa', 'Ascendio', 'Confundo', 'Expelliarmus', 'Incendio', 'Locomotor Mortis', 'Tarantallegra', 'Aparecium', 'Finite Incantatem', 'Levicorpus', 'Stupefy', 'Bombardo', 'Immobulus', 'Reducto', 'Conjunctivitis Curse', 'Fiendfyre Curse', 'Crucio', 'Imperio', 'Sectumsempra', 'Avada Kedavra']
    random_damage = random.choice(damage_spells)
    for i in spells:
        if random_damage == i['name']:
            print(f"\033[91mDamage\033[0m: {i['name']}, {i['description']}")
            damage_num += random_damage
    if (spell_count % 2) == 0:
        damage_value('user')
    else:
        damage_value('comp')
    spell_count += 1

def random_healing_spell(): # Gets a random healing spell based on the id numbers I've selected
    global healing_num
    global spell_count
    healing_num = ''
    healing_spells = ['Episkey', 'Apparate', 'Ferula', 'Aguamenti', 'Reparifors', 'Protego', 'Renneverate', 'Anapneo', 'Brackium Emendo', 'Expecto patronum']
    random_healing = random.choice(healing_spells)
    for i in spells:
        if random_healing == i['name']:
            print(f"\033[92mHealing\033[0m: {i['name']}, {i['description']}")
            healing_num += random_healing
    if (spell_count % 2) == 0:
        heal_value('user')
    else:
        heal_value('comp')
    spell_count += 1

def spell_choice(): # Gets user to pick either a damage or a healing spell
    print("Do you want to use a \033[92mhealing\033[0m spell or a \033[91mdamage\033[0m spell?: ")
    user_spell = input().capitalize()
    if user_spell == 'Damage':
        random_damage_spell()
    elif user_spell == 'Healing':
        random_healing_spell()
    else:
        print("Try typing either \033[91mdamage\033[0m or \033[92mhealing\033[0m.\n")
        spell_choice()

def spell_comp(): # Picks a random spell for the computer, either damage or healing
    spell_number = random.randint(1,2)
    if spell_number == 1:
        random_damage_spell()
    else:
        random_healing_spell()

def damage_value(team): # Works out how much damage to do
    global user_health
    global comp_health
    global damage_amount
    damage_amount = 0
    if damage_num in five_damage:
        damage_amount = 5
    elif damage_num in ten_damage:
        damage_amount = 10
    elif damage_num in fifteen_damage:
        damage_amount = 15
    elif damage_num in twenty_damage:
        damage_amount = 20
    elif damage_num in twentyFive_damage:
        damage_amount = 25
    elif damage_num in thirty_damage:
        damage_amount = 30
    elif damage_num in oneHundred_damage:
        damage_amount = 1000
    total = (damage_amount / 100) * (100 + user_special_powers[0])
    if team == 'comp':
        user_health -= total
        if user_health > 0:
            print("Now your health is {}".format(math.trunc(user_health)))
        else:
            user_health == 0
            print("Bad luck, you lose.")
    else:
        comp_health -= total
        if comp_health > 0:
            print("Now the computer's health is {}".format(math.trunc(comp_health)))
        else:
            comp_health == 0
            print("Well done, you win!")

def heal_value(team): # Works out how much healing to do
    global user_health
    global comp_health
    global healing_amount
    healing_amount = 0
    if healing_num in five_healing:
        healing_amount = 5
    elif healing_num in ten_healing:
        healing_amount = 10
    elif healing_num in fifteen_healing:
        healing_amount = 15
    elif healing_num in twenty_healing:
        healing_amount = 20
    elif healing_num in twentyFive_healing:
        healing_amount = 25
    elif healing_num in thirty_healing:
        healing_amount = 30
    total = (healing_amount / 100) * (100 + user_special_powers[1])
    if team == 'comp':
        comp_health += total
        if comp_health < 100:
            print("Now the computer's health is {}".format(math.trunc(comp_health)))
        else:
            comp_health = 100
            print("The computer's health is full.")
    else:
        user_health += total
        if user_health < 100:
            math.trunc(user_health)
            print("Now your health is {}".format(math.trunc(user_health)))
        else:
            user_health = 100
            print("Your health is full.")

def game_round(): # runs through what a round is
    round_counter = 1
    while user_health > 0 and comp_health > 0:
        print("---------------")
        print(f"\n\033[1mRound {round_counter} - your turn:\033[0m")
        spell_choice()
        round_counter += 1
        if not comp_health <= 0:
            print("\nThe computer's turn:")
            spell_comp()

def play_again():
    global user_team
    global spell_count
    global comp_team
    global user_special_powers
    global comp_special_powers
    global user_health
    global comp_health
    again = str(input("\nDo you want to play again (type yes or no): "))
    if again == "yes":
        user_team = []
        spell_count = 0
        comp_team = []
        user_special_powers = []
        comp_special_powers = []
        user_health = 100
        comp_health = 100
        play_game()
    elif again == "no":
        sys.exit(0)
    else:
        play_again()

def play_game(): # The whole game
    welcome_message()
    team_chooser()
    print(f"Your team is: {' - '.join(user_team)}.")
    random_team()
    special_powers(user_team)
    special_powers(comp_team)
    game_round()
    play_again()

play_game()