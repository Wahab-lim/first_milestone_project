def main():
    questions = [
        {
            "question": "1. What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n(d) 6\n",
            "answer": "b"
        },
        {
            "question": "2. What color is the sky on a clear day?\n(a) Red\n(b) Blue\n(c) Green\n(d) Yellow\n",
            "answer": "b"
        },
        {
            "question": "3. How many legs does a spider have?\n(a) 6\n(b) 7\n(c) 8\n(d) 9\n",
            "answer": "c"
        },
        {
            "question": "4. What sound does a cow make?\n(a) Meow\n(b) Bark\n(c) Moo\n(d) Quack\n",
            "answer": "c"
        },
        {
            "question": "5. What is the opposite of 'hot'?\n(a) Warm\n(b) Cold\n(c) Cool\n(d) Boiling\n",
            "answer": "b"
        }
    ]
    

    score = 0

    for question in questions:
        user_answer = input(question["question"]).strip().lower()
        # user_answer = input("Enter your option >").strip().lower()
        
        if (user_answer == question["answer"].lower()):
            score += 1

    
    print(f"\nYour total score is {score} out of {len(questions)}")



main()