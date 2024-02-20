print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is her name? ")

def calculate_love_score(name1, name2):
    
    words_to_count = ["TRUE", "LOVE"]
    
    counts = {}
    
    for word in words_to_count:
        word_count = 0
        for letter in word:
            word_count += name1.upper().count(letter)
            word_count += name2.upper().count(letter)
        counts[word] = word_count
    
    love_score = int(str(counts["TRUE"]) + str(counts["LOVE"]))
    return love_score


love_score = calculate_love_score(name1, name2)


if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together like rice and beans.")
else:
    print(f"Your score is {love_score}.")
