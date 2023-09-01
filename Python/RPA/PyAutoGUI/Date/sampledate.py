from datetime import datetime, timedelta
import random

def get_previous_month_range(date):
    """前月の開始日と終了日を計算する関数"""
    first_day_of_previous_month = date.replace(day=1) - timedelta(days=date.day)
    last_day_of_previous_month = date.replace(day=1) - timedelta(days=1)
    return (first_day_of_previous_month.year, first_day_of_previous_month.month, 1,
            last_day_of_previous_month.year, last_day_of_previous_month.month, last_day_of_previous_month.day)

def get_previous_year_previous_month_range(date):
    """前年の前月の開始日と終了日を計算する関数"""
    first_day_of_previous_year_previous_month = date.replace(year=date.year-1, day=1) - timedelta(days=date.day)
    last_day_of_previous_year_previous_month = date.replace(year=date.year-1, day=1) - timedelta(days=1)
    return (first_day_of_previous_year_previous_month.year, first_day_of_previous_year_previous_month.month, 1,
            last_day_of_previous_year_previous_month.year, last_day_of_previous_year_previous_month.month, last_day_of_previous_year_previous_month.day)

def get_recent_month_range(date, start_month):
    """直近の指定した月の開始日と終了日を計算する関数"""
    if date.month >= start_month:
        start_date = date.replace(month=start_month, day=1)
    else:
        start_date = date.replace(year=date.year-1, month=start_month, day=1)
    last_day_of_current_month = start_date.replace(day=1) + timedelta(days=32) - timedelta(days=1)
    last_day_of_current_month = last_day_of_current_month.replace(day=1) - timedelta(days=1)
    return (start_date.year, start_date.month, 1, last_day_of_current_month.year, last_day_of_current_month.month, last_day_of_current_month.day)

def get_recent_year_previous_month_range(date, start_month):
    """前年以前の直近の指定した月の開始日と終了日を計算する関数"""
    start_date = date.replace(year=date.year-1, month=start_month, day=1)
    last_day_of_current_month = start_date.replace(day=1) + timedelta(days=32) - timedelta(days=1)
    last_day_of_current_month = last_day_of_current_month.replace(day=1) - timedelta(days=1)
    return (start_date.year, start_date.month, 1, last_day_of_current_month.year, last_day_of_current_month.month, last_day_of_current_month.day)

def calculate_ranges(date):
    """各条件の期間を計算する関数"""
    start1, start_month1, start_day1, end1, end_month1, end_day1 = get_previous_month_range(date)
    start2, start_month2, start_day2, end2, end_month2, end_day2 = get_previous_year_previous_month_range(date)
    start3, start_month3, start_day3, _, _, _ = get_recent_month_range(date, 8)
    end3 = end1  # 条件1の終了日を使用
    start4, start_month4, start_day4, _, _, _ = get_recent_year_previous_month_range(date, 8)
    end4 = date.replace(year=date.year-1, day=1) - timedelta(days=1)
    return (start1, start_month1, start_day1, end1, end_month1, end_day1,
            start2, start_month2, start_day2, end2, end_month2, end_day2,
            start3, start_month3, start_day3, end1, 8, end_day1,
            start4, start_month4, start_day4, end4.year, 8, end4.day)

for _ in range(50):
    random_date = datetime(random.randint(2020, 2023), random.randint(1, 12), random.randint(1, 28))
    print("Random Date:", random_date.strftime("%Y/%m/%d"))
    
    ranges = calculate_ranges(random_date)

    print("条件1:", ranges[0], "/", ranges[1], "/", ranges[2], "-", ranges[3], "/", ranges[4], "/", ranges[5])
    print("条件2:", ranges[6], "/", ranges[7], "/", ranges[8], "-", ranges[9], "/", ranges[10], "/", ranges[11])
    print("条件3:", ranges[12], "/", 8, "/", 1, "-", ranges[15], "/", ranges[4], "/", ranges[5])
    print("条件4:", ranges[12]-1, "/", 8, "/", 1, "-", ranges[21], "/", ranges[10], "/", ranges[11])

