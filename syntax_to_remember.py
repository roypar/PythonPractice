"""Using Try, Except Blocks"""
def check_leap_year(year):
    is_leap_year = False
    if year % 4 == 0:
        is_leap_year = True

    return is_leap_year


year = 1983


class MyError(Exception):
    def __init__(self):
        self.message = "My custom error"


try:
    if not check_leap_year(year):
        raise MyError
except MyError as msg:
    print(msg.message)
else:
    print(year)
