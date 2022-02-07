print("-------------Hands on 2---------------")
import datetime
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
now = datetime.date.today()
dayOfWeek = now.weekday()
today = weekDays[dayOfWeek]
daysToWeekend = 6 - dayOfWeek
print(f'There are {daysToWeekend-1} days until the weekend')
quotePrinted = "false"
for left in weekDays[dayOfWeek:6]:
    if today == "Sunday" and quotePrinted == "false":
        print(left, " Sunday is my funday!")
        quotePrinted = "true"
    elif (today == "Monday" or today == "Tuesday" or today == "Wednesday") and quotePrinted == "false":
        print(left, " Sign...Back to the daily grind")
        quotePrinted = "true"
    elif today == "Thursday" and quotePrinted == "false":
        print(left, " Almost there...")
        quotePrinted = "true"
    elif quotePrinted == "false":
        print(left, " Woo hoo, the weekend")
        quotePrinted = "true"
    else:
        print(left)