"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""

def date_passed(todays_date, scheduled_date):
    month_dic = {"January": 1, "February": 2, 
                 "March": 3, "April":4, "May": 5, 
                 "June": 6, "July": 7, "August": 8,
                 "September": 9, "October": 10,
                 "November": 11, "December": 12}
    today = todays_date.split()
    today_day = int(today[0][:-2])
    today_month = today[1]
    scheduled = scheduled_date.split()
    scheduled_day = int(scheduled[0][:-2])
    scheduled_month = scheduled[1]

    if month_dic[today_month] < month_dic[scheduled_month]:
        print("Scheduled date is yet to pass")
    elif month_dic[today_month] == month_dic[scheduled_month]:
        if today_day < scheduled_day:
            print("Scheduled date is yet to pass")
        elif today_day == scheduled_day:
            print("Scheduled date is today")
        else:
            print("Scheduled date is today")
    else:
        print("Scheduled date has passed")

date_passed("26th March", "25th March")
    


# Test cases
# date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
# date_passed("26th March", "26th March")  # Expected: Scheduled date is today
# date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
