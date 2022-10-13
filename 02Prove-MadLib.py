import datetime
hourNow=(datetime.datetime.now().hour)

#Greeting determination based on time of day
if hourNow<12:wlcm="Good morning!"
elif hourNow<18:wlcm="Good afternoon!"
else :wlcm="Good evening!"

print (f"{wlcm} Please enter the following to generate your story, and do not conjugate\n")
adv1 = input("Adverb: ")
adj1 = input("Adjective: ")
animal = input("Animal: ")
verb1 = input("Verb: ")
exclamation = input("Exclamation: ")
said = input("Said, Yelled, Yelped, Hollered, etc.: ")
verb2 = input("Verb: ")
v2 = 0
for i in verb2:
    v2 = v2+1

if v2 % 2 == 0:
    repeat = "over and over"
elif v2 % 2 != 0: repeat = "again and again"

ppron = input("Possessive Pronoun: ")
noun = input("Noun: ")
verb3 = input("Verb: ")

output = f"""The other day, I was really in trouble. It all started when I saw a {adv1.lower()}
{adj1.lower()} {animal.lower()} {verb1.lower()} down the hallway. "{exclamation.title()}!" I {said.lower()}. But all
I could think to do was to {verb2.lower()} {repeat}. Miraculously,
that caused it to stop, but not before it tried to {verb3.lower()}
right in front of {ppron.lower()} {noun.lower()}."""

print ("\nYour story has been successfully generated! Enjoy.\n")
print(output)