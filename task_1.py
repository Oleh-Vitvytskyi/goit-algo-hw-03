from datetime import datetime

def get_days_from_today(user_date):
    try:
        input_date =  datetime.strptime(user_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError ("Неправельний формат дати.")
    
    date_now = datetime.now().date()

    difference = date_now - input_date

    return difference.days

user_date = input("Введіть дату в форматі 'РРРР-ММ-ДД': ")

try:
    difference_in_day = get_days_from_today(user_date)
    print(difference_in_day)
except ValueError as e:
    print(e)