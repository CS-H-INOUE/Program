from datetime import date, datetime

def today_command():
    today = date.today()
    response = f'今日ノ日付ハ {today} デス'
    return response

def now_command():
    now = datetime.now()
    response = f'現在日時ハ {now} デス'
    return response

def weekday_command(command):
    try:
        data = command.split()
        year = int(data[1])
        month = int(data[2])
        day = int(data[3])
        one_day = date(year, month, day)

        weekday_str = '月火水木金土日'
        weekday = weekday_str[one_day.weekday()]

        response = f'{one_day} ハ {weekday}曜日デス'
    except IndexError:
        response = '3ツノ値(年月日)ヲ指定シテクダサイ'
    except ValueError:
        response = '正シイ日付ヲ指定シテクダサイ'
    return response
