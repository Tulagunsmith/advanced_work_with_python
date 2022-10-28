from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


today = datetime.now().date()


if __name__ == "__main__":
    get_employees(today)
    calculate_salary()