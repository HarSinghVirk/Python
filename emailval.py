# Email validation Using RegEx
## Conditions:
# a - z
# 0 - 9
# . _ occurance (time 1)
# @ only 1
# . 2, 3 place
import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input('Enter your Email : ')

if  re.search(email_condition, user_email):
    print(' Right Email ')
else:
    print(' Wrong Email ')