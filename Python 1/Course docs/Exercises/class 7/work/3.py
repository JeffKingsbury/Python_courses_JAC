# 3) Write a simple script that divides a number (integer) by zero. Can you trap the exception and
# print a suitable message?


try:
    2 / 0
except Exception as e:
    print('The following error occurred:', e);
else:
    print('success')