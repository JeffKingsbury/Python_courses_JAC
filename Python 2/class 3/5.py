# 5) (JSON exercise) Create a list of dictionaries with 5 countries, their capital, and approx.
# population(of the capital)
# Sample entry:
# {‘Country’: ‘Canada’, ‘Capital’:’Ottawa’, ‘Population’: 883,391}
# Write the dictionary to a json format file.
# Check the contents of the file in notepad or other text editor.
# Read the file back into your script and parse with json.
# Print the contents from the resulting dictionary. (key and value)

import json;

countries = [{"Country":"Canada", "Capital":"Ottawa", "Population":883391},
             {"Country":"United States of America", "Capital":"Washington DC", "Population":692683},
             {"Country":"Mexico", "Capital":"Mexico City", "Population":8885000},
             {"Country":"United Kingdom", "Capital":"London", "Population":9000000},
             {"Country":"China", "Capital":"Beijing", "Population":21540000}];

with open('py2_Class3_Ex5.json', 'w') as outfile:
    json.dump(countries, outfile, indent=4, separators=(',',':'));
    
importJson = open('py2_Class3_Ex5.json', 'r');

parsedJson = json.load(importJson);
for x in parsedJson:
    for i in x:
        print(i, x[i])