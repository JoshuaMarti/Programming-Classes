# loop_count = 0
# user_loop_count = int(input("How many loops would you like to run?"))
# while loop_count < user_loop_count or loop_count == user_loop_count:
#     print (f"Loop Count is: {loop_count}")
#     loop_count = loop_count + 1

#7.2, as of 221024. I am aware that it is possible for there to be a female or nonbinary president, but last I checked, Joseph Biden was a Mr.
waiting_for_correct_input = False
while waiting_for_correct_input == False:
    entry = input("What is the last name of the current President of the United States of America: ")
    if entry.lower() == "biden":
        waiting_for_correct_input = True
        print (f"Correct. Mr. {entry.title()} is the current President.")
    else: print(f"Incorrect. {entry} is not the current president. Please try again.")
