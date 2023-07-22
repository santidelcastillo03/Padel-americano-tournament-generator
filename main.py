from app import *


def main():
    participant_list = []
    print('-----------------------------------')
    print('Welcome to the americano padel app!')
    print('-----------------------------------2')
    while True:
        option = input('Choose an option:\n1 - Add participants\n2 - Generate americano padel matches\n3 - Add '
                       'points\n4 - Show points\n5 - Exit\n-->')
        if option == '1':
            add_participant(participant_list)
        elif option == '2':
            generate_matches(participant_list)
        elif option == '3':
            add_match_points(participant_list)
        elif option == '4':
            show_points(participant_list)
        elif option == '5':
            print('Bye!')
            break
        else:
            print('Invalid option')


main()
