import re


r_p = re.compile('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
string = input()
if r_p.match(string):
    print("Good to go")
else:
    print("make sure to include an Uppercase and a Lowercase letter along with a Special charanter with min length of 6 and max length of 20")
