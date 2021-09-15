# 1) Write a program that defines the following list:
# countries = ["Canada", "Russia", "Mexico", "Poland"]
# 1.1 Print the list
# 1.2 Reverse the list and print it
# 1.3 Sort the list and print it
# 1.4 Copy the countries list to a new list countries_02
# 1.5 delete the last element from countries_02
# 1.6 Pop the first element from countries and save it into a variable called OneCountry, print
# OneCountry
# 1.7 Append the element "Spain" to the countries list
# 1.8 Extend countries with countries_02, and print countries
# 1.9 Find out how many times "Mexico" is found in the list, print the result.

countries = ["Canada", "Russia", "Mexico", "Poland"];

#1.1
print(countries);
#1.2
# print(countries[::-1]); would work if you just want to print it in reverse, but not store it that way.
countries.reverse()
print(countries)
#1.3
countries.sort();
print(countries);
#1.4
countries_02 = list(countries);
#1.5
del(countries_02[-1]);
#1.6
OneCountry = countries.pop(0)
print(OneCountry);
#1.7
countries.append("Spain");
#1.8
countries.extend(countries_02);
#1.9
MexicoCount = 0;
for x in countries:
    if x == 'Mexico':
        MexicoCount += 1;      
print(MexicoCount);        
