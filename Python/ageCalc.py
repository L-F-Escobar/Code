from datetime import datetime
from dateutil.relativedelta import relativedelta

year = 0
month = 0
day = 0

str_now = str(datetime.now())
curr_year = str_now[:4]

# Year check
while True:
    try:
        year = int(input('\nEnter year of birth (xxxx): '))
    except ValueError:
        print("\nSorry, I didn\'t understand that. Please enter your year of birth.")
        continue
    except:
        print('\nUnknown error. Please enter a year of birth (xxxx)')
        continue

    if len(str(year)) != 4 or int(year) < 1700 or int(year) > int(curr_year):
        print('\nValid year format is xxxx. Max year allowed is %s, minimum allowed is 1700.' %curr_year)
    else:
        break


# Month check
while True:
    try:
        month = int(input('\n\nEnter month of birth (1-12): '))
    except ValueError:
        print("\nSorry, I didn\'t understand that. Please enter a month between 1-12.")
        continue
    except:
        print('\nUnknown error. Please enter a month between 1-12.')
        continue

    if month <= 12 and month >= 1:
        break
    else:
        print("\nPlease enter a month between 1-12.")


# Day check
while True:
    try:
        # if month == 1, 3, 5, 7, 8, 10, 12: # MONTHS WITH 31 days
        # if month == 4, 6, 9, 11: # MONTHS WITH 30 days
        # if month == 2: # MONTHS WITH 28 days    

        day = int(input('\n\nEnter day of birth (xx): '))
    except ValueError:
        print("\nSorry, I didn\'t understand that. Please enter day of birth.")
        continue
    except:
        print('\nUnknown error. Please enter day of birth.')
        continue

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day > 31 or day < 1:
            print('\nValid days for month selected are 1-31.')
        else:
            break

    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30 or day < 1:
            print('\nValid days for month selected are 1-30.')
        else:
            break

    else: #month = 2
        if day > 29 or day < 1:
            print('\nValid days for month selected are 1-29.')
        else:
            break



# delta = datetime.now() - datetime(year, month, day)

years_since = relativedelta(datetime.now(), datetime(year, month, day)).years
months_since = relativedelta(datetime.now(), datetime(year, month, day)).months
days_since = relativedelta(datetime.now(), datetime(year, month, day)).days
secs_since = relativedelta(datetime.now(), datetime(year, month, day)).seconds


print("\n\n\nIts been %s years, %s months, %s days & %s seconds since your birth." %(years_since, months_since, days_since, secs_since))
