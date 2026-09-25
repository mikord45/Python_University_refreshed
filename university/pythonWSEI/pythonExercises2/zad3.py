import calendar
import datetime

def last_day_of_month(year, month):
    last_day = calendar.monthrange(year, month)[1]
    last_day_helper = datetime.date(year, month, last_day)

    while last_day_helper.weekday() in [calendar.SATURDAY, calendar.SUNDAY]:
        last_day -= 1
        last_day_helper = datetime.date(year, month, last_day)

    return last_day_helper.strftime("%d.%m.%Y")

def main():
    year = int(input("Podaj rok: "))

    for month in range(1, 13):
        month_name = datetime.date(year, month, 1).strftime("%B")
        payment_date = last_day_of_month(year, month)

        print(f"{month_name}: {payment_date}")

if __name__ == "__main__":
    main()