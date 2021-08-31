# Write a program that prompts the user to enter a temperature in degrees Fahrenheit
# (i.e. 75, 78.3, -10.5, etc.). Then convert the temperature to degrees Celsius according to the formula:
# °C = (°F - 32) x 5/9
# Then print a message according to the following logic:
# If the temperature (Celsius) is less than or equal to -15.0 print:
#  “It’s (temp) degrees Celsius, Let’s get out of here!”
# If the temperature is higher than -15.0 but less than or equal to 0.0 then print:
#  “It’s (temp) degrees Celsius, Get your boots and gloves!”
# If the temperature is higher than 0.0 but less than or equal to 15.0 then print:
# “It’s (temp) degrees Celsius, I have my sweater!”
# If the temperature is higher than 15.0 then print:
# “It’s (temp) degrees Celsius, It is BBQ time!!”
# Replace (temp) by the actual temperature in degrees Celsius. Do not worry about the look of the
#  temperature result (i.e. 24.530000). For this question practice the use of elif statement. You can
#  round the result if you want, by using -> round(your_number,2)

print("\nF to C converter: \n")
tempF = input("Please enter a temp in Fahrenheit: ");
tempC = (int(tempF) - 32) * (5/9);

if tempC <= -15:
    print("It's " + str(tempC) + " degrees Celsius, Let's get out of here!");
    
elif tempC > -15 and tempC <= 0:
    print("It's " + str(tempC) + " degrees Celsius, Get your boots and gloves!");
    
elif tempC > 0 and tempC <= 15:
    print("It's " + str(tempC) + " degrees Celsius, I have my sweater!");
    
else:
    print("It's " + str(tempC) + " degrees Celsius, it's BBQ time!");


