from participant import Participant
import random


def show_participants(participant_list):
    for index, participant in enumerate(participant_list):
        print(f'{index + 1} - {participant.name}')


def add_participant(participant_list):
    while True:
        add = input('Enter the name of the participant:\n\n-->').title()
        participant_list.append(Participant(add, 0))
        option = input('Do you want to add another participant? (y/n)').lower()
        if option == 'y':
            continue
        elif option == 'n':
            break
        else:
            print('Invalid option')
            break
    print('The participants are:')
    show_participants(participant_list)


def generate_matches(participant_list):
    if len(participant_list) < 4:
        print('There are not enough participants to generate a match')
    else:
        res = []
        n = len(participant_list)
        for i in range(n):
            for j in range(i + 1, n):
                res.append((participant_list[i], participant_list[j]))
        random.shuffle(res)
        print('The matches are:')
        for index,match in enumerate(res):
            print(f'-------------{index+1}-------------\n{match[0].name} vs {match[1].name}')


def show_points(participant_list):
    participant_list.sort(key=lambda x: x.points, reverse=True)
    for index, participant in enumerate(participant_list):
        print(f'-----------{index + 1}-----------\n{participant.name} --> {participant.points}')


def add_match_points(participant_list):
    while True:
        if len(participant_list) == 0:
            print('There are no participants')
            break
        else:
            show_points(participant_list)
        while True:
            try:
                select_player = int(input("Select the player's number:"))
                if select_player in range(1, len(participant_list) + 1):
                    break
                else:
                    print('Invalid option')
            except ValueError:
                print('Invalid option')
        while True:
            try:
                points = int(input('Enter the points: '))
                break
            except ValueError:
                print('Invalid option')
        participant_list[select_player - 1].points += points
        print('Points added successfully')
        option = input('Do you want to add points to another player? (y/n)').lower()
        if option == 'y':
            continue
        elif option == 'n':
            break
        else:
            print('Invalid option')
