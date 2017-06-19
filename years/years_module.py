import datetime


def years(age):
    now = datetime.datetime.now()
    current_year = now.year
    yearstoremain = 99 - age
    year_100 = current_year + yearstoremain
    return year_100


def main():
    try:
        name = input("What is your name?\n")
    except TypeError:
        print("Please, enter your name!")
    try:
        age = float(input("How old are you?\n"))
    except TypeError:
        print("Please, enter your age!")
    age_input = round(years(age))
    print("Dear", name, "you will be 100 years old in the year of", age_input, ":) .")


if __name__ == '__main__':
    main()
