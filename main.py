from datetime import datetime

import emoji

from application.db.people import calculate_salary
from application.salary import get_employees

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(datetime.today().date())
    print(emoji.emojize('Python is :thumbs_up:'))