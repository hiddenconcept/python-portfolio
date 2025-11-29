import time

print("Loading.", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(.5)
print(".", end="", flush=True)

time.sleep(1)

print("")
print("")


print("Hello & Welcome to my age calculator!")

#input(" What is your age?")
#input("Do you know how many months that is ?")
#input("Do you know the time you were born in 24 hours?")

import datetime


age_years = int(input("What year were you born in?"))

while True:
   choice  = input("What would you like to find out? Days, Months, Minutes, Seconds or ALL: ").strip().upper()

    if choice == "MONTHS":
        current_year = datetime.now().year
        birth_year = current_year - age_years
        age_months = age_years * 12
        print("You chose Months.")
        print(f"You are approximately {age_months} months old.")
        break  # stops the while loop

    elif choice == "Days":
            age_days = age_years *12 * 365
            current_year = datetime.now().year
            birth_year = current_year - age_years
            print("You choose days")
            print(f"You are approximately  {age_days}old in Days")
            break



        elif choice == "Minutes":
            age_minutes = age_years *12 * 365 * 60
            current_year = datetime.now().year
            birth_year = current_year - age_years
            print("You choose minutes")
            print(f"You are approximately  {age_minutes}old in Minutes")
            break

        elif choice == "Seconds":
                    age_seconds = age_years *12 * 365 * 24 * 60 * 60
                    current_year = datetime.now().year
                    birth_year = current_year - age_years
                    print("You choose seconds")
                    print(f"You are approximately  {age_seconds}old in Seconds")
                    break

    else:
        print(f"Invalid choice. Please select: Days, Months, Minutes, Seconds or ALL\n")


#important information
#Days = (Current Year - Birth Year) x 365.25 + (Current Month - Birth Month) x 30.4 + (Current Day - Birth Day)
# 86400 seconds in 1 day
# 1440 minutes in a day
# 365 days in a year 365.25
# 1461 days including 1 loop year  every 4 years

