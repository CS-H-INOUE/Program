from pybot_eto import eto_command
from pybot_random import choice_command, dice_command
from pybot_datetime import today_command, now_command, weekday_command
from pybot_sum import sum_command

def len_command(command):
    cmd, text = command.split()
    length = len(text)
    response = f'文字列ノ長サハ {length} 文字デス'
    return response

def wareki_command(command):
    wareki, year_str = command.split()
    if year_str.isdigit():
        year = int(year_str)
        if year >= 2019:
            reiwa = year - 2018
            response = f'西暦{year}年ハ、令和{reiwa}年デス'
        elif year >= 1989:
            heisei = year - 1988
            response = f'西暦{year}年ハ、平成{heisei}年デス'
        else:
            response = f'西暦{year}年ハ、平成ヨリ前デス'
    else:
        response = '数値ヲ指定シテクダサイ'
    return response

command_file = open('pybot.txt', encoding='utf-8')
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines()

bot_dict = {}
for line in lines:
    word_list = line.split(',')
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response

def pybot(command, image=None):
    response = ''
    try:
        for message in bot_dict:
            if message in command:
                response = bot_dict[message]
                break

        if '和暦' in command:
            response = wareki_command(command)
        if '長さ' in command:
            response = len_command(command)
        if '干支' in command:
            response = eto_command(command)
        if '選ぶ' in command:
            response = choice_command(command)
        if 'さいころ' in command:
            response = dice_command()
        if '今日' in command:
            response = today_command()
        if '現在' in command:
            response = now_command()
        if '曜日' in command:
            response = weekday_command(command)
        if '合計' in command:
            response = sum_command(command)

        if not response:
            response = '何ヲ言ッテルカ、ワカラナイ'
        return response

    except Exception as e:
        print('予期セヌ エラーガ 発生シマシタ')
        print(f'* 種類: {type(e)}')
        print(f'* 内容: {e}')
