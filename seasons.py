from datetime import date, datetime
import sys
import re
import operator
import inflect


def main():
    # ask for input
    user = convert(validate(input("Date of Birth: ")))
    print(user)

def validate(my_date):
    # YYYY-MM-DD 1990-01-08
    matches = re.search(r"^(\d{4})-(1[0-2]|0[0-9])-(0[0-9]|1[0-9]|2[0-9]|3[0-1])$", my_date)
    if matches:
        my_year = (matches.group(1))
        my_month = (matches.group(2))
        my_day = (matches.group(3))
        m_date = my_date
        return m_date
    else:
        print("Invalid date")
        sys.exit(1)


def convert(m_date):
    # constructs a date object from str
    birthday = (date.fromisoformat(m_date))
    # today's date
    now = date.today()
    operator.__sub__(birthday, now)
    n_days = (now - birthday)

    in_minutes = round(n_days.total_seconds() / 60)

    # numbers into words without and
    p = inflect.engine()
    words = p.number_to_words(in_minutes, andword = "")
    return((words + " minutes").capitalize())


if __name__ =="__main__":
    main()
