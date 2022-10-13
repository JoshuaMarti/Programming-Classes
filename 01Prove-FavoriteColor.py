import datetime
hourNow=(datetime.datetime.now().hour)

#Greeting determination based on time of day
if hourNow<12:wlcm="Top o' the mornin' to ya!"
elif hourNow<17:wlcm="Good afternoon!"
else :wlcm="Why are you still awake? I strongly recommend going to bed soon. Still, I'm glad you made time for me :-)"
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(f"{wlcm} What is your name?")
fn=input("\n\n   ")
print(f"\n\nIt's nice to meet you, {fn}! What's your favorite color?")
fc=input("\n\n  ")
colorMatch=0
if fc=="cyan":colorMatch=1
elif fc=="Cyan":colorMatch=1
elif fc=="blue":colorMatch=1
elif fc=="Blue":colorMatch=1

if colorMatch==1:
    print("\nHey,",fc,"is my favorite color too!")
elif colorMatch==0:
    print("\nThat's neat,",fc,"is a cool color, though my personal favorite is probably Cyan.")

#Load farewell and execute
ta1="           ██▄ █╬█ █╬█ ╬╬ █ ██▄ ███ █╬█ ███"
ta2="           █▄█ █▄█ █╬█ ╬╬ █ █╬█ █▄█ █▄█ █╬█"
ta3="           █▄█ ╬█╬ ███ ╬╬ █ ███ █╬█ █╬█ █▄█"
ta4=""
ta5=""

print(f"Well, it's been good chatting with you, {fn}! I've got to get going though. Hope the rest of your day goes well, and enjoy your time here!")
print(f"\n\033[46m\n{ta1}\n{ta2}\n{ta3}\n{ta4}\n{ta5}\033[0m")