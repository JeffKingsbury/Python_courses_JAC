# 4) Write a function that checks for Canadian Postal Codes.
# The postal code is a six-character code defined and maintained by Canada Post Corporation (CPC) for the
# purpose of sorting and delivering mail. The characters are arranged in the form ‘ANA NAN’, where ‘A’
# represents an alphabetic character and ‘N’ represents a numeric character (e.g., K1A 0T6). The postal
# code uses 18 alphabetic characters and 10 numeric characters. Postal codes do not include the letters D,
# F, I, O, Q or U, and the first position also does not make use of the letters W or Z.
# Hint: [ABCEGHJ-NPRSTVXY] checks for any of these characters. For this example no lower case characters. 

import re;
regex = '^[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTVWXYZ][\s-]?\d[ABCEGHJ-NPRSTVWXYZ]\d$';

postal = input('Please enter a Canadian postal code to see if it is valid: ');

check = re.search(regex, postal);

if str(check) != 'None':
    print('{} is a valid Canadian postal code.'.format(postal));
else:
    print('{} is an invalid Canadian postal code.'.format(postal));