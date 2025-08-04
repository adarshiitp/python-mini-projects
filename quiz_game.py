questions = [
    {
        "question": "What is the capital of India?",
        "options": [" a) Delhi"," b) Mumbai"," c) Kolkata"," d) Lucknow"],
        "answer": "a"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": [" a) Earth", " b) Venus", " c) Mars", " d) Jupiter"],
        "answer": "c"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": [" a) Atlantic", " b) Indian", " c) Arctic", " d) Pacific"],
        "answer": "d"
    },
    {
        "question": "Who wrote the national anthem of India?",
        "options": [" a) Rabindranath Tagore", " b) Mahatma Gandhi", " c) Subhash Chandra Bose", " d) APJ Abdul Kalam"],
        "answer": "a"
    },
    {
        "question": "Which is the smallest prime number?",
        "options": [" a) 0", " b) 1", " c) 2", " d) 3"],
        "answer": "c"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": [" a) O2", " b) CO2", " c) H2O", " d) HO"],
        "answer": "c"
    },
    {
        "question": "Who invented the light bulb?",
        "options": [" a) Alexander Graham Bell", " b) Thomas Edison", " c) Newton", " d) Tesla"],
        "answer": "b"
    },
    {
        "question": "Which programming language is known as snake case?",
        "options": [" a) Java", " b) Python", " c) C++", " d) HTML"],
        "answer": "b"
    },
    {
        "question": "How many continents are there?",
        "options": [" a) 5", " b) 6", " c) 7", " d) 8"],
        "answer": "c"
    },
    {
        "question": "Which number comes next in the sequence: 2, 4, 8, 16, __?",
        "options": [" a) 20", " b) 24", " c) 30", " d) 32"],
        "answer": "d"
    }

]

score = 0

print("Welcome to quiz game...\n")

for i,q in enumerate(questions,1):
    print(f"Q{i}: {q['question']}")
    for option in q['options']:
        print(option)
    student = input("Enter any one option a/b/c/d = ").lower()
    if student == q["answer"]:
        print("✅ Correct ! \n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is: {q['answer']})\n")

print("Quiz Completed...")
total_questions = len(questions)
print(f"Your Final Score is  : {score} / {total_questions} ")

if score == total_questions:
    print("Perfect , You are Genius")
if score > 7 :
    print("Very good")
if score >= 5:
    print("Good Job")
if score >0 :
    print("improve your  Study")
else :
    print("Try again...")
