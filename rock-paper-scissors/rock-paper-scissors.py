import random
def play_r_p_s(user_choice): # initial/not working
    computer_choice = random.choice(('r','p','s'))
    print(computer_choice)
    if computer_choice == user_choice:
        return 'Draw'
    elif computer_choice=='r' and user_choice=='p':
        return 'User Win'
    elif computer_choice=='p' and user_choice=='s':
        return 'User Win'
    elif computer_choice=='s' and user_choice=='r':
        return 'User Win'
    else:
        return 'Computer Win'

# Test print(play_r_p_s("r"))
