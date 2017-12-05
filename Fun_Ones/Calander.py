months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
weeks = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
start_week_day = [5, 0, 1, 2, 3, 5, 6, 0, 1, 3, 4, 5, 6, 1, 2, 3, 4, 6, 0, 1, 2, 4, 5, 6, 0, 2, 3, 4]

year = int(input("enter an year : "))
week_day = start_week_day[year % len(start_week_day)]

for i in range(12):
    if i in (0, 2, 4, 6, 7, 9, 11):
        for day in range(1, 32):
            if(week_day % 7 == 0): print()
            print(str(day) + " / " + str(months[i] + " / " + str(year) + " - " + str(weeks[week_day%7])))
            week_day += 1
    elif i in (3, 5, 8, 10):
        for day in range(1, 31):
            if(week_day % 7 == 0): print()
            print(str(day) + " / " + str(months[i] + " / " + str(year) + " - " + str(weeks[week_day%7])))
            week_day += 1
    elif (year % 4 == 0):
        for day in range(1, 30):
            if(week_day % 7 == 0): print()
            print(str(day) + " / " + str(months[i] + " / " + str(year) + " - " + str(weeks[week_day%7])))
            week_day += 1
    else:
        for day in range(1, 29):
            if(week_day % 7 == 0): print()
            print(str(day) + " / " + str(months[i] + " / " + str(year) + " - " + str(weeks[week_day%7])))
            week_day += 1

input("\n\n----------\nHit enter to close\n")