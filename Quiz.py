print("Welcome to Quiz")
print("You will be asked a series of questions")
print("Answer the questions correctly to win the prize")
print("Good Luck")

questions = [
    "1. What is the capital of Japan?",
    "2. Which element has the chemical symbol 'O'?",
    "3. What is the largest mammal on Earth?",
    "4. In which year did the Titanic sink?",
    "5. Who wrote 'Romeo and Juliet'?",
    "6. What is the currency of India?",
    "7. What is the boiling point of water in Celsius?",
    "8. Which gas makes up the majority of Earth's atmosphere?",
    "9. What is the speed of light in a vacuum?",
    "10. How many continents are there in the world?"
]

answers = [
    "Tokyo",
    "Oxygen",
    "Blue Whale",
    "1912",
    "William Shakespeare",
    "Indian Rupee",
    "100 degrees",
    "Nitrogen",
    "299,792 kilometers per second",
    "7"
]

scores = [0] * len(questions)

for i, question in enumerate(questions):
    print(question)
    if i == 0:
        options = ["a. Tokyo", "b. Beijing", "c. Seoul", "d. Bangkok"]
    elif i == 1:
        options = ["a. Oxygen", "b. Gold", "c. Silver", "d. Carbon"]
    elif i == 2:
        options = ["a. Elephant", "b. Giraffe", "c. Blue Whale", "d. Dolphin"]
    elif i == 3:
        options = ["a. 1905", "b. 1912", "c. 1923", "d. 1931"]
    elif i == 4:
        options = ["a. Charles Dickens", "b. Jane Austen", "c. William Shakespeare", "d. Mark Twain"]
    elif i == 5:
        options = ["a. Dollar", "b. Euro", "c. Yen", "d. Indian Rupee"]
    elif i == 6:
        options = ["a. 0 degrees", "b. 50 degrees", "c. 100 degrees", "d. 212 degrees"]
    elif i == 7:
        options = ["a. Oxygen", "b. Nitrogen", "c. Carbon dioxide", "d. Hydrogen"]
    elif i == 8:
        options = ["a. 100,000 kilometers per second", "b. 299,792 kilometers per second", "c. 500,000 kilometers per second", "d. 1 million kilometers per second"]
    elif i == 9:
        options = ["a. 5", "b. 6", "c. 7", "d. 8"]

    for option in options:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").lower()
    if user_answer == "a" and answers[i].lower() == "tokyo":
        scores[i] = 10000
        print("Correct!")
        print("You won", scores[i])
    elif user_answer == "b" and answers[i].lower() == "oxygen":
        scores[i] = 50000
        print("Correct!")
        print("You won", scores[i])
    elif user_answer == "c" and answers[i].lower() == "blue whale":
        scores[i] = 100000
        print("Correct!")
        print("You won", scores[i])
    elif user_answer == "d" and answers[i].lower() == "1912":
        scores[i] = 5000
        print("Correct!")
        print("You won", scores[i])
    elif user_answer == "c" and answers[i].lower() == "william shakespeare":
        scores[i] = 20000
        print("Correct!")
        print("You won", scores[i])
    elif user_answer == "c" and answers[i].lower() == "indian rupee":
        scores[i] = 30000
        print("Correct!")
        print("You won", scores[i])
    elif user_answer == "c" and answers[i].lower() == "100 degrees":
        scores[i] = 15000
        print("Correct!")
        print("You won", scores[i])
    elif user_answer == "b" and answers[i].lower() == "nitrogen":
        scores[i] = 25000
        print("Correct!")
        print("You won", scores[i])
    elif user_answer == "b" and answers[i].lower() == "299,792 kilometers per second":
        scores[i] = 40000
        print("Correct!")
        print("You won", scores[i])
    elif user_answer == "c" and answers[i].lower() == "7":
        scores[i] = 3000
        print("Correct!")
        print("You won", scores[i])
    else:
        print("Incorrect!")

# Total score
total_score = sum(scores)
print("Your total score is", total_score)