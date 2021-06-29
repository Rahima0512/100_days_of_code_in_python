f_name1=str(input("Enter your first name\t"))
l_name1=str(input("Enter your last name\t"))
def func_output(f_name,l_name):
    if f_name=="" and l_name=="":
        return "You did not provide any input"
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(func_output(f_name1,l_name1))

#Days in a month
def is_leap(year):
    is_leap_year = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
                is_leap_year=True
            else:
                print("Not leap year.")
                is_leap_year = False
        else:
            print("Leap year.")
            is_leap_year = True
    else:
        print("Not leap year.")
        is_leap_year = False
    return is_leap_year


def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_it_leap=is_leap(year)
    if month==2:
        if(is_it_leap==True):
            days=29
            return days
        else:
            days=28
            return days
    elif month>=1 and month<=12:
        days=month_days[month-1]
        return days
    else:
        return "Wrong input"

# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
