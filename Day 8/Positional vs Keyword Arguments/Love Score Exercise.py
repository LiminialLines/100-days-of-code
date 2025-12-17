
love1 = input("What is your name?")
love2 = input(f"{love1}, what is the name of your lover?")
total_love = (love1 + love2).lower()
def calculate_love_score(love1,love2):
    love_score = 0
    for letter in total_love:
        if letter in "true":
            love_score +=1
        if letter in "love":
            love_score += 1
    print(f"Your love score is {love_score}")
calculate_love_score(love1,love2)