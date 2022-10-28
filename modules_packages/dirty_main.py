from application.salary import *
from application.db.people import *
from datetime import datetime

today = datetime.now().date()


if __name__ == "__main__":
    get_employees(today)
    calculate_salary()