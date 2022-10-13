#Exercise 2.1, Long Formatted String
#Programming Building Blocks, 220920
age = input("What is your Age? ")
fn = input("What is your First Name? ")
hobby = input("What is your Favorite Hobby? ")
exercise = input("What is your Favorite Exercise? ")

output = f"""
Hi {fn}. Glad yo meet you.
You are not too old - only {age} years old.
I also like to {hobby} and
{exercise} is my favorite as well"""

print(output)