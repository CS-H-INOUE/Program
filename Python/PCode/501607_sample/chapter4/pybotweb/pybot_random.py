import random

def choice_command(command):
    data = command.split()
    choiced = random.choice(data[1:])
    response = f'「{choiced}」ガ選バレマシタ'
    return response

def dice_command():
    num = random.randrange(1, 7)
    response = f'「{num}」ガ出マシタ'
    return response
