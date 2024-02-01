import datetime as dt
from application.salary import calculate_salary
from application.db.people import get_employees

current_date = dt.datetime.today()

if __name__ == '__main__':
    print(get_employees('Ivan'))
    print(calculate_salary(3000, 50000))
    print(f"Сегодня: {current_date}")
