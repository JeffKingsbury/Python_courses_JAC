import datetime;
year = int(datetime.datetime.today().year)
name = input("What is your name? ");
print("Hello, " + name + ".");
birth_year = input("What year were you born? ");
try:
    val = int(birth_year)
except ValueError:
    birth_year = input("What year were you born? ");

ans = year - int(birth_year)
print("So you're " + str(ans) + " years old?")