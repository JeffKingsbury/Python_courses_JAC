# 4) (JSON exercise) Fetch the contents of the following URL (using urllib):
# http://www.groupce.com/python/json/json_comments.json
# and parse it using the json standard library.
# Print all the names that start with an ‘A’ and
# print the ‘count’, and the running total for the ‘count’.
# Hint: take a look at the json file so that you get an idea of its format. 


import urllib.request as ur;
import json;
jsonFile = ur.urlopen('http://www.groupce.com/python/json/json_comments.json');

parsedJson = json.load(jsonFile);
nameCount = 0;
aNameCount = 0;
print("The following names begin with the letter A, in the provided list:");
for x in parsedJson['comments']:
    nameCount += 1;
    if x['name'][:1].upper() == 'A':
        aNameCount +=1;
        print(x['name'])
        
print("There are {} total names on the provided list. {} of them start with the letter 'A'.".format(nameCount, aNameCount));